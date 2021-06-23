from matplotlib import pyplot as plt
from typing import List

from src.controller.file_manager import FileManager


class OutputManager:
    @staticmethod
    def generate_output(sum_transactions_selled_per_day, sum_transactions_selled_per_week,
                        sum_transactions_selled_per_month, amount_transactions_revel,
                        total_revel_tcs, purchased_value,
                        value_sold,
                        monthly_average_selled, week_average_selled, day_average_selled,
                        date):
        OutputManager._print_on_screen(sum_transactions_selled_per_day, sum_transactions_selled_per_week,
                                       sum_transactions_selled_per_month)
        OutputManager._generate_graphs(sum_transactions_selled_per_day, sum_transactions_selled_per_week,
                                       sum_transactions_selled_per_month)
        FileManager.output_text(amount_transactions_revel, total_revel_tcs, purchased_value, value_sold,
                                monthly_average_selled, week_average_selled,
                                day_average_selled, date)

    @staticmethod
    def _print_on_screen(sum_transactions_selled_per_day, sum_transactions_selled_per_week,
                         sum_transactions_selled_per_month):
        print(f'Soma de vendas por dia: {sum_transactions_selled_per_day}')
        print(f'Soma de vendas por semana: {sum_transactions_selled_per_week}')
        print(f'Soma de vendas por mês: {sum_transactions_selled_per_month}')

    @staticmethod
    def _generate_graphs(sum_transactions_selled_per_day, sum_transactions_selled_per_week,
                         sum_transactions_selled_per_month):
        OutputManager._generate_days_graph(sum_transactions_selled_per_day)
        plt.figure()
        OutputManager._generate_week_graph(sum_transactions_selled_per_week)
        plt.figure()
        OutputManager._generate_month_graph(sum_transactions_selled_per_month)
        plt.show()

    @staticmethod
    def _generate_days_graph(sum_transactions_selled_per_day):
        OutputManager._generate_graph(xlabel='Número de dias', ylabel='Vendas por dia',
                                      title='Número de vendas por dia',
                                      data=sum_transactions_selled_per_day, color='blue')

    @staticmethod
    def _generate_week_graph(sum_transactions_selled_per_week):
        OutputManager._generate_graph(xlabel='Número de semanas', ylabel='Vendas por semana',
                                      title='Número de vendas por semana',
                                      data=sum_transactions_selled_per_week, color='green')

    @staticmethod
    def _generate_month_graph(sum_transactions_selled_per_month):
        OutputManager._generate_graph(xlabel='Número de meses', ylabel='Vendas por mês',
                                      title='Número de vendas por mês',
                                      data=sum_transactions_selled_per_month, color='red')

    @staticmethod
    def _generate_graph(xlabel: str, ylabel: str, title: str, data: List[int], color: str):
        eixo_x = [i + 1 for i in range(len(data))]
        eixo_y = data
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.plot(eixo_x, eixo_y, color=color)
