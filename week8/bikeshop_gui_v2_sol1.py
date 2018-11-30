from PyQt5 import uic, QtWidgets
import sys


class ShopWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShopWidget, self).__init__()
        uic.loadUi('bike_shop_v2.ui', self)
        
        self.btn_submit.clicked.connect(self.btn_push)
        
        self.le_username.textChanged.connect(self.le_username_changed)
        self.le_username.editingFinished.connect(self.le_username_disable)


    #----------------------------------
    # gui variables
    #----------------------------------

        self.basket = {}

    #----------------------------------
    # widget actions
    #----------------------------------
    def btn_push(self):
        if self.sb_quantity.value():
            self.basket[self.cb_item.currentText()] = self.sb_quantity.value()
            print('1')
        basket_str_op = ''
        for k, v in self.basket.items():
            basket_str_op += k + ":    " + str(v) + "\n"
        self.tb_basket.setPlainText(basket_str_op)
        
    def le_username_changed(self):
        self.btn_submit.setEnabled(True)
        self.btn_submit.setStyleSheet("background-color: green;")
        
    def le_username_disable(self):
        self.le_username.setReadOnly(True)
        self.le_username.setEnabled(False)
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ShopWidget()
    window.show()
    sys.exit(app.exec_())
