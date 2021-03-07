from typing import List

from src.controller.file_manager import FileManager
from src.controller.statistics.statistics_generator import StatisticsGenerator
from src.model.date.date import Date
from src.model.transaction.bank_transactions import BankTransactions
from src.model.transaction.transaction import Transaction


class AppManager:

    @staticmethod
    def __convert_file_transctions_to_transactions(list_json_transactions: List) -> List["Transaction"]:
        return [
            Transaction(transaction["id"], transaction["value"], transaction["player"],
                        Date(date_dict=transaction["date"]))
            for transaction in list_json_transactions
        ]

    @staticmethod
    def __get_bank() -> BankTransactions:
        transactions_json = FileManager.get_transactions()
        transactions_list_a = AppManager.__convert_file_transctions_to_transactions(transactions_json[0])
        transactions_list_b = AppManager.__convert_file_transctions_to_transactions(transactions_json[1])
        bank = BankTransactions(transactions_list_a)
        bank.add_list_transaction(transactions_list_b)
        return bank

    @staticmethod
    def start():
        bank = AppManager.__get_bank()
        statistics = StatisticsGenerator(bank)
        statistics.calculate()