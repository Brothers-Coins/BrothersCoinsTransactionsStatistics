from typing import List
from src.model.singleton import Singleton
from src.model.transaction.transaction import Transaction
import operator

class BankTransactions:
    __metaclass__ = Singleton

    def __init__(self, transactions: "List[Transaction]"):
        self.__transactions = transactions
        self.__last_date = transactions[0].date

    def add(self, transaction: Transaction):
        self.__transactions.append(transaction)

    def add_list_transaction(self, transactions: List["Transaction"]):
        last_date_of_transaction = transactions[0].date
        self.__last_date = last_date_of_transaction if last_date_of_transaction > self.__last_date else self.__last_date
        self.__transactions.extend(transactions)
        self.__transactions.sort(key=operator.attrgetter('date'), reverse=True)

    @property
    def transactions(self) -> List["Transaction"]:
        return self.__transactions

    @property
    def last_date(self):
        return self.__last_date
