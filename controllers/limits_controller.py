from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.limit import Limit
import repositories.limit_repository as limit_repository

limits_blueprint = Blueprint("limits", __name__)

@limits_blueprint.route("/", methods=['POST'])
def set_limits():
    print(request.form)
    spending_limit = request.form['spending-limit']
    notification_point = request.form['notification-limit']
    limit = Limit(spending_limit, notification_point)
    limit_repository.save(limit)
    return render_template("/index.html", limit=limit)



