from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.transaction_repository as transaction_repository
import repositories.limit_repository as limit_repository

overview_blueprint = Blueprint("overview", __name__)

@overview_blueprint.route("/")
def show_overview():
    limit = limit_repository.select_last()
    print (limit)
    total = transaction_repository.total_spending()
    print (limit.spending_limit)
    print (total)
    return render_template("/index.html", total_spend=total, limit=limit)




    

