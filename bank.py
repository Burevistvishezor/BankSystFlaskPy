import json
import os
from datetime import datetime


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.log("deposit", amount)
        return True

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.log("withdraw", amount)
        return True

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)
        self.log("transfer", amount, to_account.owner)

    def log(self, type_op, amount, to_owner=None):
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": type_op,
            "amount": amount
        }
        if to_owner:
            entry["to"] = to_owner
        self.transactions.append(entry)

    def info(self):
        return {"owner": self.owner, "balance": self.balance, "transactions": self.transactions}


class Bank:
    def __init__(self, data_file="accounts.json"):
        self.accounts = {}  # owner: BankAccount
        self.data_file = data_file
        self.load()

    def create_account(self, owner, balance=0):
        if owner in self.accounts:
            raise ValueError("Account exists")
        self.accounts[owner] = BankAccount(owner, balance)
        self.save()

    def get_account(self, owner):
        if owner not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[owner]

    def save(self):
        data = {}
        for owner, acc in self.accounts.items():
            data[owner] = {
                "balance": acc.balance,
                "transactions": acc.transactions
            }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
            for owner, info in data.items():
                acc = BankAccount(owner, info["balance"])
                acc.transactions = info.get("transactions", [])
                self.accounts[owner] = acc
