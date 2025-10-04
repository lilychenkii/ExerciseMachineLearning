from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

from Review.MainWindow_ListProducts import Ui_MainWindow


class MainWindow_ListProductsExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        super().setupUi(MainWindow)
    def showWindow(self):
        self.MainWindow.show()
    def load_products(self,lp):
        self.tableWidgetProduct.setRowCount(0)
        for i in range (0,len(lp.products)):
            p=lp.products[i]
            number_row=self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(number_row)
            self.tableWidgetProduct.setItem(number_row,0,QTableWidgetItem(p.id))
            self.tableWidgetProduct.setItem(number_row,1,QTableWidgetItem(p.name))
            self.tableWidgetProduct.setItem(number_row,2,QTableWidgetItem(str(p.quantity)))
            self.tableWidgetProduct.setItem(number_row,3,QTableWidgetItem(str(p.price)))
