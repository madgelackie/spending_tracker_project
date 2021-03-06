from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.limit_repository as limit_repository

transactions_blueprint = Blueprint("transactions", __name__)

# show all transactions with conditional loops to manage spending limit notificication feature
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.total_spending()
    limit = limit_repository.select_last()
    near_limit = False
    if total >= limit.notification_point:
        near_limit = True
    over_limit = False
    if total > limit.spending_limit:
        near_limit = False
        over_limit = True
    on_limit = False
    if total == limit.spending_limit:
        near_limit = False
        over_limit = False
        on_limit = True
    return render_template("transactions/index.html", transactions=transactions, total_spend=total, near_limit=near_limit, over_limit=over_limit, on_limit=on_limit)

# show all transactions sorted by date
@transactions_blueprint.route("/transactions/sortby_date")
def transactions_by_date():
    transactions = transaction_repository.select_all_by_date()
    total = transaction_repository.total_spending()
    return render_template("transactions/date.html", transactions=transactions, total_spend=total)

# show all transactions sorted by amount
@transactions_blueprint.route("/transactions/sortby_amount")
def transactions_by_amount():
    transactions = transaction_repository.select_all_by_amount()
    total = transaction_repository.total_spending()
    return render_template("transactions/amount.html", transactions=transactions, total_spend=total)

# takes user to form to add new transaction
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transactions/new.html", all_tags=tags, all_merchants=merchants)

# route after pressing submit on 'add new transaction' page, to pull info from the form
@transactions_blueprint.route("/transactions", methods=['POST']) 
def create_transaction():
    amount = request.form['amount']
    tag_id = request.form['spending_type']
    merchant_id = request.form['merchant']
    date = request.form['date']
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, tag, merchant, date)
    transaction_repository.save(transaction)
    return redirect('/transactions')

# takes user to form of selected transaction, to edit transaction
@transactions_blueprint.route("/transactions/<id>/edit", methods=['GET', 'POST'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("/transactions/edit.html", transaction=transaction, all_tags=tags, all_merchants=merchants)

# updates the task edited in /transactions/edit form
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    amount = request.form['amount']
    tag_id = request.form['tag']
    merchant_id = request.form['merchant']
    date = request.form['date']
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, tag, merchant, date, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")


