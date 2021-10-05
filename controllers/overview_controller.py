from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.transaction_repository as transaction_repository


overview_blueprint = Blueprint("overview", __name__)

@overview_blueprint.route("/")
def show_overview():
    return render_template("/index.html")



    

