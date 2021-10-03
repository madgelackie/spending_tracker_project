from pdb import run
from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, active) VALUES ( %s, %s ) RETURNING id"
    values = [merchant.name, merchant.active]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def update(merchant):
    sql = "UPDATE merchant SET (merchant.name, merchant.active) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.active, merchant.id]
    run_sql(sql, values)

def select(id):
    merchant = None
    sql = "SELECT * FROM merchant WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['active'], result['id'])
    return merchant