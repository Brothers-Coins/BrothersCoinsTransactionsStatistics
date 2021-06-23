from typing import List

from src.controller.output_manager import OutputManager
from src.model.transaction.bank_transactions import BankTransactions
from src.model.transaction.transaction import Transaction


class StatisticsGenerator:
    def __init__(self, bank_transactions: BankTransactions):
        self.__transactions = bank_transactions.transactions
        self.__transactions_sell = self.__transactions_sell()
        self.__transactions_buy = self.__transactions_buy()
        self.__last_date = bank_transactions.last_date

    def __transactions_sell(self) -> List["Transaction"]:
        return list(filter(lambda transaction: transaction.value < 0, self.__transactions))

    def __transactions_buy(self) -> List["Transaction"]:
        return list(filter(lambda transaction: transaction.value > 0, self.__transactions))

    @staticmethod
    def sum_transactions(transactions: List["Transaction"]):
        return sum([transaction.value for transaction in transactions])

    def __get_list_transactions_sell_by_number_days(self, number_days: int):
        list_all_transactions_sells_by_days = []
        stop_loop = False
        current_index = 0
        while not stop_loop:
            current_transaction = self.__transactions_sell[current_index]
            list_transactions_of_period = [current_transaction]
            iterable_index = current_index
            while True:
                iterable_index += 1
                try:
                    next_transaction = self.__transactions_sell[iterable_index]
                except IndexError:
                    stop_loop = True
                    break
                else:
                    date_resulted = list_transactions_of_period[0].date - next_transaction.date
                    if date_resulted.days < number_days:
                        list_transactions_of_period.append(next_transaction)
                    else:
                        current_index = iterable_index
                        list_all_transactions_sells_by_days.append(list_transactions_of_period)
                        break
        return list_all_transactions_sells_by_days

    @staticmethod
    def __average_list_transaction(sum_transactions_by_period, amount):
        return sum(sum_transactions_by_period) / amount

    @staticmethod
    def __generate_sum_transactions_of_period(transactions_selled_per_period: list) -> list:
        list_sums = []
        for list_transaction in transactions_selled_per_period:
            transaction_list_value = []
            for transaction in list_transaction:
                transaction_list_value.append(transaction.abs_value)
            list_sums.append(sum(transaction_list_value))
        return list_sums

    def __take_revel_tc(self):
        revel_tcs = []
        qtde_transactions = 0
        for transaction in self.__transactions_sell:
            if transaction.player_name == "Revel Rookstayer":
                revel_tcs.append(transaction.abs_value)
                self.__transactions_sell.remove(transaction)
                qtde_transactions += 1
        return revel_tcs, qtde_transactions

    def calculate(self):
        revel_tcs, amount_transactions_revel = self.__take_revel_tc()
        total_revel_tcs = sum(revel_tcs)
        purchased_value = self.sum_transactions(self.__transactions_sell)
        value_sold = abs(self.sum_transactions(self.__transactions_buy))
        sellings_by_month = self.__get_list_transactions_sell_by_number_days(30)
        sellings_by_week = self.__get_list_transactions_sell_by_number_days(7)
        sellings_by_day = self.__get_list_transactions_sell_by_number_days(1)
        number_of_months = len(sellings_by_month)
        number_of_weeks = len(sellings_by_week)
        number_of_days = len(sellings_by_day)
        sum_transactions_selled_per_month = self.__generate_sum_transactions_of_period(sellings_by_month)
        sum_transactions_selled_per_week = self.__generate_sum_transactions_of_period(sellings_by_week)
        sum_transactions_selled_per_day = self.__generate_sum_transactions_of_period(sellings_by_day)
        monthly_average_selled = self.__average_list_transaction(sum_transactions_selled_per_month, number_of_months)
        week_average_selled = self.__average_list_transaction(sum_transactions_selled_per_week, number_of_weeks)
        day_average_selled = self.__average_list_transaction(sum_transactions_selled_per_day, number_of_days)

        OutputManager.generate_output(sum_transactions_selled_per_day, sum_transactions_selled_per_week,
                                      sum_transactions_selled_per_month, amount_transactions_revel,
                                      total_revel_tcs, purchased_value,
                                      value_sold,
                                      monthly_average_selled, week_average_selled, day_average_selled,
                                      str(self.__last_date))
