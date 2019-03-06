import sys
import os

from threading import Thread
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from MainWindow import *
from uniform import *
#from binomial import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.uniButton.clicked.connect(self.make_uniform_distr)
        
    def make_uniform_distr(self):
        path = os.getcwd()
        path += '\\uniform'
        proc = Thread(target = self.thread_target_uni, args=())
        proc.start()

    def thread_target_uni(self):
        len_of_distr = [100, 1000, 10000]
        for i in len_of_distr:
            unf = uniform_distribution(i)
            unf.math_exp_uni()
            unf.dispersion_uni()
            unf.write_to_file()
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
