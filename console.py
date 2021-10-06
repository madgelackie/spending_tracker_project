import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

tag_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

tag1 = Tag('food')
tag_repository.save(tag1)

tag2 = Tag('subscriptions')
tag_repository.save(tag2)

tag3 = Tag('healthcare')
tag_repository.save(tag3)

tag4 = Tag('tournament fees')
tag_repository.save(tag4)

tag5 = Tag('clothing', False)
tag_repository.save(tag5)


merchant1 = Merchant('Supermercado', True)
merchant_repository.save(merchant1)

merchant2 = Merchant('Nurse Joy', True)
merchant_repository.save(merchant2)

merchant3 = Merchant('Brock')
merchant_repository.save(merchant3)

merchant4 = Merchant('Pokédex')
merchant_repository.save(merchant4)

merchant5 = Merchant("Aina's Kitchen", False)
merchant_repository.save(merchant5)

transaction1 = Transaction(2500, tag1, merchant1, '20200115')
transaction_repository.save(transaction1)

transaction2 = Transaction(300, tag2, merchant4, '20210205')
transaction_repository.save(transaction2)

transaction3 = Transaction(1000, tag4, merchant3, '20210629')
transaction_repository.save(transaction3)


pdb.set_trace()


