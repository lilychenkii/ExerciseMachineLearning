from Review.product import Product
from Review.products import ListProduct

lp=ListProduct()
lp.add_product(Product("p1",'Coca',10,15))
lp.add_product(Product("p2",'Pepsi',20,18))
lp.add_product(Product("p3",'Fanta',15,12))
lp.add_product(Product("p4",'Sprite',12,10))
lp.print_products()