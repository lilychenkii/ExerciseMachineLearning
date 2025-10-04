import pandas as pd

class MyStatistic:
    def find_orders_within_range(self, df, minValue, maxValue, sortType=True):
        order_totals = df.groupby('OrderID').apply(
            lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
        ).reset_index(name='Sum')

        filtered_orders = order_totals[
            (order_totals['Sum'] >= minValue) & (order_totals['Sum'] <= maxValue)
        ]

        filtered_orders = filtered_orders.sort_values(by='Sum', ascending=sortType)

        return filtered_orders.reset_index(drop=True)
