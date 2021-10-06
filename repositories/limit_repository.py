from pdb import run
from db.run_sql import run_sql
from models.limit import Limit

def save(limit):
    sql = "INSERT INTO limits (spending_limit, notification_point) VALUES ( %s, %s) RETURNING id"
    values = [limit.spending_limit, limit.notification_point]
    results = run_sql(sql, values)
    id = results[0]['id']
    limit.id = id
    return limit

def delete_all():
    sql = "DELETE FROM limits"

def update(limit):
    sql = "UPDATE limits SET (spending_limit, notification_point) = ( %s, %s) WHERE id = %s"
    values = [limit.spending_limit, limit.notification_point]
    run_sql(sql, values)

def select(id):
    limit = None
    sql = "SELECT * FROM limits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        limit = Limit(result['spending_limit'], result['notification_point'], result['id'])
    return limit

def select_all():
    limits = []
    sql = "SELECT * FROM limits"
    results = run_sql(sql)
    for row in results:
        limit = Limit(row['spending_limit'], row['notification_point'], row['id'])
        limits.append(limit)
    return limits

def select_last():
    limit = None
    sql = "SELECT * FROM limits ORDER BY id DESC limit 1"
    result = run_sql(sql)[0]
    if result is not None:
        limit = Limit(result['spending_limit'], result['notification_point'], result['id'])
    return limit
