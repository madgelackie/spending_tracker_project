from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

# show all transactions
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.total_spending()
    return render_template("transactions/index.html", transactions=transactions, total_spend=total)

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
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, tag, merchant)
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
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, tag, merchant, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")


