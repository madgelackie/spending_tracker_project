from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.limit import Limit
import repositories.limit_repository as limit_repository
import repositories.transaction_repository as transaction_repository

limits_blueprint = Blueprint("limits", __name__)

@limits_blueprint.route("/limits")
def show_all():
    limits = limit_repository.select_all()
    return render_template("/limits/index.html", all_limits=limits)

@limits_blueprint.route("/limits/new")
def new_limit():
    return render_template("/limits/new.html")

@limits_blueprint.route("/limits", methods=['POST'])
def set_limits():
    spending_limit = request.form['spending-limit']
    notification_point = request.form['notification-point']
    limit = Limit(spending_limit, notification_point)
    limit_repository.save(limit)
    total = transaction_repository.total_spending()
    return render_template("/index.html", total_spend=total, limit=limit)



