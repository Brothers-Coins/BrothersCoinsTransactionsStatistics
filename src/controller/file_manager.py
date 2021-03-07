import json
from abc import ABC
from typing import List, Tuple


class FileManager:
    __metaclass__ = ABC
    __base_transactions_path = '../data/input/transactions_'

    @staticmethod
    def __get_transctions_from_file(type_caracter: str) -> List:
        with open(FileManager.__base_transactions_path + type_caracter + '.json') as arq:
            return json.load(arq)["transactions"]

    @staticmethod
    def get_transactions() -> "Tuple":
        return FileManager.__get_transctions_from_file('a'), FileManager.__get_transctions_from_file('b')

    @staticmethod
    def output_text(amount_transactions_revel, total_revel_tcs, purchased_value, value_sold,
                    monthly_average_selled, week_average_selled,
                    day_average_selled, date):
        string = 'Data da última transação capturada: ' + date + '\n\n'
        string += '=========== REVEL ===========\n'
        string += f'Revel: {total_revel_tcs}\n'
        string += f'Quantidade de vezes: {amount_transactions_revel}\n'
        string += '=========== VENDAS E COMPRA ===========\n'
        string += f'Quantidade total comprada: {purchased_value}\n'
        string += f'Quantidade total vendida: {value_sold}\n'
        string += '-----------------------------------------\n'
        string += f'Média mensal vendida: {round(monthly_average_selled)}\n'
        string += f'Média semanal vendida: {round(week_average_selled)}\n'
        string += f'Média diária vendida: {round(day_average_selled)}\n'
        with open('../data/output_statistics.txt', 'w', encoding='utf8') as arq:
            arq.write(string)
