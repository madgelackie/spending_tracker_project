from flask import Flask, render_template, request, redirect
from flask import Blueprint
from db.run_sql import run_sql
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# show all tags and edit/deactivate button
@tags_blueprint.route("/tags")
def show_all():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", all_tags=tags)

# form to add new tag
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")

# create new tag once form submitted
@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    spending_type = request.form['tag']
    active = request.form['active']
    if request.form['active'] == 'yes':
        active = True
    elif request.form['active'] == 'no':
        active = False
    tag = Tag(spending_type, active)
    tag_repository.save(tag)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/edit", methods=['GET', 'POST'])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("/tags/edit.html", tag=tag)

@tags_blueprint.route("/tags/<id>", methods=['POST'])
def update_tag(id):
    spending_type = request.form['spending-tag']
    active = request.form['active']
    tag = Tag(spending_type, active, id)
    tag_repository.update(tag)
    return redirect("/tags")
