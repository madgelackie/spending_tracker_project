from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def show_all():
    merchants = merchant_repository.select_all()
    return render_template("/merchants/index.html", all_merchants=merchants)

@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("/merchants/new.html")

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form['name']
    active = request.form['active']
    if request.form['active'] == 'yes':
        active = True
    elif request.form['active'] == 'no':
        active = False
    merchant = Merchant(name, active)
    merchant_repository.save(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET', 'POST'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("/merchants/edit.html", merchant=merchant)

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    active = request.form['active']
    merchant = Merchant(name, active, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")