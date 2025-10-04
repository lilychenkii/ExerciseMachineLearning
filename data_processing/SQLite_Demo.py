import sqlite3
import pandas as pd

def load_data():
    try:
        conn = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        print("DB Connected")
        invoice_line = pd.read_sql_query("SELECT * FROM InvoiceLine;", conn)
        invoice = pd.read_sql_query("SELECT * FROM Invoice;", conn)
        customer = pd.read_sql_query("SELECT * FROM Customer;", conn)
        conn.close()
        print("SQLite Connection Closed")
        return invoice_line, invoice, customer
    except sqlite3.Error as error:
        print("Error occurred:", error)
        return None, None, None

invoice_line, invoice, customer = load_data()
def top_invoices_by_value(invoice_line, invoice, min_value, max_value, top_n):
    merged = invoice_line.merge(invoice, on="InvoiceId")
    total_per_invoice = merged.groupby('InvoiceId')['UnitPrice'].sum().reset_index(name='Total')
    filtered = total_per_invoice[
        (total_per_invoice['Total'] >= min_value) &
        (total_per_invoice['Total'] <= max_value)
    ]
    result = filtered.sort_values(by='Total', ascending=False).head(top_n)
    return result
def top_customers_by_invoice_count(invoice, top_n):
    count_per_customer = invoice.groupby('CustomerId').size().reset_index(name='InvoiceCount')
    result = count_per_customer.sort_values(by='InvoiceCount', ascending=False).head(top_n)
    return result
def top_customers_by_invoice_value(invoice, top_n):
    total_per_customer = invoice.groupby('CustomerId')['Total'].sum().reset_index()
    result = total_per_customer.sort_values(by='Total', ascending=False).head(top_n)
    return result

if invoice_line is not None:
    print("\n(1) TOP 5 Invoice giá trị từ 10 → 30:")
    print(top_invoices_by_value(invoice_line, invoice, 10, 30, 5))

    print("\n(2) TOP 5 khách hàng có nhiều Invoice nhất:")
    print(top_customers_by_invoice_count(invoice, 5))

    print("\n(3) TOP 5 khách hàng có tổng Invoice cao nhất:")
    print(top_customers_by_invoice_value(invoice, 5))

