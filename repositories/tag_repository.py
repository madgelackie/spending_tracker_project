from pdb import run
from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (spending_type, active) VALUES ( %s, %s ) RETURNING id"
    values = [tag.spending_type, tag.active]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def update(tag):
    sql = "UPDATE tags SET (tag.spending_type, tag.active) = (%s, %s) WHERE id = %s"
    values = [tag.spending_type, tag.active, tag.id]
    run_sql(sql, values)

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['spending_type'], result['active'], result['id'])
    return tag
