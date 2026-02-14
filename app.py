from flask import Flask, render_template, request, redirect, url_for, flash
from bank import Bank

app = Flask(__name__)
app.secret_key = "supersecretkey"

bank = Bank()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        owner = request.form["owner"]
        balance = float(request.form["balance"])
        try:
            bank.create_account(owner, balance)
            flash(f"Account {owner} created!")
        except ValueError as e:
            flash(str(e))
        return redirect(url_for("index"))
    return render_template("index.html", accounts=bank.accounts.values())

@app.route("/account/<owner>", methods=["GET", "POST"])
def account(owner):
    try:
        acc = bank.get_account(owner)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("index"))

    if request.method == "POST":
        action = request.form["action"]
        amount = float(request.form["amount"])
        try:
            if action == "deposit":
                acc.deposit(amount)
            elif action == "withdraw":
                acc.withdraw(amount)
            elif action == "transfer":
                to_owner = request.form["to_owner"]
                acc.transfer(bank.get_account(to_owner), amount)
            bank.save()
            flash("Operation successful")
        except ValueError as e:
            flash(str(e))
        return redirect(url_for("account", owner=owner))

    return render_template("account.html", account=acc, accounts=bank.accounts.values())

if __name__ == "__main__":
    app.run(debug=True)
