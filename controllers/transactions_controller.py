from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

@transactions_blueprint.route("/transactions/new")
def add_transaction():
    return render_template("transactions/new.html")

@transactions_blueprint.route("/transactions/edit")
def edit_transaction():
    return render_template("transactions/edit.html")
