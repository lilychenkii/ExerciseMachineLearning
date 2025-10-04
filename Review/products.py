class ListProduct:
    def __init__(self):
        self.products=[]
    def add_product(self,p):
        self.products.append(p)

    def sort_by_price_desc(self):
        # Sort products by price in descending order
        n = len(self.products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.products[j].price < self.products[j + 1].price:
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]

    def sort_by_price_asc_and_quantity_desc(self):
        # Sort products by price (ascending) and quantity (descending if prices are equal)
        n = len(self.products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (self.products[j].price > self.products[j + 1].price or
                        (self.products[j].price == self.products[j + 1].price and
                         self.products[j].quantity < self.products[j + 1].quantity)):
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]

    def print_products(self):
        # Print products without sorting
        for p in self.products:
            print(p)