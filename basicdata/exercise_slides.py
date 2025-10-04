import pandas as pd

def filter_and_sort_orders_from_file(file_path, minValue, maxValue, sortType=True):
    df = pd.read_csv(file_path)

    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='Sum')

    filtered_orders = order_totals[
        (order_totals['Sum'] >= minValue) & (order_totals['Sum'] <= maxValue)
    ]

    filtered_orders = filtered_orders.sort_values(by='Sum', ascending=sortType)

    return filtered_orders.reset_index(drop=True)


if __name__ == "__main__":
    file_path = '../dataset/SalesTransactions/SalesTransactions.csv'

    min_val = float(input("Nhập giá trị min: "))
    max_val = float(input("Nhập giá trị max: "))
    sort_type = input("Sort tăng dần? (True/False): ").strip().lower() == "true"

    result = filter_and_sort_orders_from_file(file_path, min_val, max_val, sort_type)
    print(result)
