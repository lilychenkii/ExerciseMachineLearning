from PyQt6.QtWidgets import QApplication, QMainWindow

from Review.MainWindow_ListProductsExt import MainWindow_ListProductsExt
from Review.product import Product
from Review.products import ListProduct

app=QApplication([])
qmain=QMainWindow()
my_window=MainWindow_ListProductsExt()
my_window.setupUi(qmain)
lp=ListProduct()
lp.add_product(Product("p1",'Coca',10,15))
lp.add_product(Product("p2",'Pepsi',20,18))
lp.add_product(Product("p3",'Fanta',15,12))
lp.add_product(Product("p4",'Sprite',12,10))
my_window.load_products(lp)
my_window.showWindow()
app.exec()