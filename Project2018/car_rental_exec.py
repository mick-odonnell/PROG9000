from PyQt5 import uic, QtWidgets
import sys
from datetime import datetime as dt

from gui import Ui_MainWindow
import rental_objects as ro

class CarRental(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CarRental, self).__init__()
        self.setupUi(self)

        self.gb_dialog.setEnabled(False)

        self.pb_agent_select.clicked.connect(self.manage_agent_click)
        self.pb_customer_select.clicked.connect(self.manage_customer_click)



        # set default time for date/time pickers
        self.date_start.setDate(dt.now())
        self.date_start.setMinimumDate(dt.now())
        self.date_end.setDate(dt.now())
        self.date_end.setMinimumDate(dt.now())
        self.time_start.setTime(dt.now().time())
        self.time_end.setTime(dt.now().time())

        self.date_start.dateChanged.connect(self.manage_start_date_change)

        # ----------------------------------------------------
        # Load System Info
        # ----------------------------------------------------

        v_list = [{'regnum': "01-KK-12345",
                   'make': 'Volkswagen',
                   'model': 'Passat',
                   'efficiency': 30,
                   'seats': 5,
                   'daily_cost': 40,
                   'weekly_cost': 220,
                   'weekend_cost': 65,
                   'doors': 4},
                  {'regnum': "12-WD-12345",
                   'make': 'Peugeot',
                   'model': '406',
                   'efficiency': 30,
                   'seats': 4,
                   'daily_cost': 45,
                   'weekly_cost': 230,
                   'weekend_cost': 66},
                  {'regnum': "13-KK-145",
                   'make': 'Renault',
                   'model': 'Kangoo',
                   'efficiency': 32,
                   'seats': 2,
                   'daily_cost': 43,
                   'weekly_cost': 290,
                   'weekend_cost': 60}
                  ]

        self.shop_instance = ro.Shop_Manager(v_list)
    # ----------------------------------------------------
    # Manage User Interaction
    # ----------------------------------------------------

    def manage_agent_click(self):
        self.gb_dialog.setEnabled(True)
        self.tw_dialog.setCurrentIndex(0)
        self.gb_user_management.setEnabled(False)
        self.op_message("You entered Agent Portal")

    def manage_customer_click(self):
        self.gb_dialog.setEnabled(True)
        self.tw_dialog.setCurrentIndex(1)
        self.gb_user_management.setEnabled(False)
        self.op_message("You entered Customer Portal")

    def op_message(self, op_str):
        self.le_op_message.clear()
        self.le_op_message.setText(op_str)

    def manage_start_date_change(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CarRental()
    window.show()
    sys.exit(app.exec_())