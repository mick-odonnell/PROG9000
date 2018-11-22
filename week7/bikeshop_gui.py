from PyQt5 import uic, QtWidgets
import sys


class ShopWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShopWidget, self).__init__()
        uic.loadUi('bike_shop.ui', self)
        self.btn_submit.clicked.connect(self.btn_push)


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



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ShopWidget()
    window.show()
    sys.exit(app.exec_())
