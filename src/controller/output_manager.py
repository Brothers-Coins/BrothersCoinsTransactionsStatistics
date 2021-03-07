from src.controller.file_manager import FileManager


class OutputManager:
    @staticmethod
    def generate_output(revel_tcs, amount_transactions_revel, total_revel_tcs, purchased_value,
                                      value_sold, number_of_transactions_sell, number_of_transactions_buy,
                                      number_of_months,
                                      number_of_weeks, number_of_days, sum_transactions_selled_per_month,
                                      sum_transactions_selled_per_week, sum_transactions_selled_per_day,
                                      monthly_average_selled, week_average_selled, day_average_selled,
                                      date):
        FileManager.output_text(amount_transactions_revel, total_revel_tcs, purchased_value, value_sold,
                                monthly_average_selled, week_average_selled,
                                day_average_selled, date)
