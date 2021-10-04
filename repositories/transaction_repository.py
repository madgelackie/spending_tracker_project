from pdb import run
from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, tag_id, merchant_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.tag.id, transaction.merchant.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"

def update(transaction):
    sql = "UPDATE transactions (amount, tag_id, merchant_id) WHERE id = %s"
    values = [transaction.amount, transaction.tag.id, transaction.merchant.id, transaction.id]
    run_sql(sql, values)

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['amount'], tag, merchant, row['id'])
        transactions.insert(0, transaction)
    return transactions




        
