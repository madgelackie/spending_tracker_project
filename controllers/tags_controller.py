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
    tag = Tag(spending_type)
    tag_repository.save(tag)
    return redirect("/tags")
