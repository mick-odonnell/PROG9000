from PyQt5 import uic, QtWidgets
import sys

class CarRental(QtWidgets.QMainWindow):
    def __init__(self):
        super(CarRental, self).__init__()
        uic.loadUi('gui_main.ui', self)

        self.gb_dialog.setEnabled(False)

        self.pb_agent_select.clicked.connect(self.manage_agent_click)
        self.pb_customer_select.clicked.connect(self.manage_customer_click)


    # ----------------------------------------------------
    # Manage User Interaction
    # ----------------------------------------------------

    def manage_agent_click(self):
        self.gb_dialog.setEnabled(True)
        self.tw_dialog.setCurrentIndex(0)

    def manage_customer_click(self):
        self.gb_dialog.setEnabled(True)
        self.tw_dialog.setCurrentIndex(1)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CarRental()
    window.show()
    sys.exit(app.exec_())