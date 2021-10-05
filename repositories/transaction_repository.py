from pdb import run
from db.run_sql import run_sql
from operator import attrgetter
from models.transaction import Transaction
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, tag_id, merchant_id, date) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.tag.id, transaction.merchant.id, transaction.date]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (amount, tag_id, merchant_id, date) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.amount, transaction.tag.id, transaction.merchant.id, transaction.date, transaction.id]
    run_sql(sql, values)

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = tag_repository.select(result['tag_id'])
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(result['amount'], tag, merchant, result['date'], result['id'])
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['amount'], tag, merchant, row['date'], row['id'])
        transactions.insert(0, transaction)
    return transactions

def total_spending():
    total_spend = 0
    transactions = select_all()
    for transaction in transactions:
        total_spend += transaction.amount
    return total_spend

# def date_sort():
#     transactions = select_all()
#     dates = []
#     for transaction in transactions:
#         dates.append(transaction.date)
#     sorted_list = sorted(dates)
#     return sorted_list

def select_all_by_date():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY date DESC"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['amount'], tag, merchant, row['date'], row['id'])
        transactions.append(transaction)
    return transactions
        






        
