from PyQt5 import QtWidgets
import sys
from qtdesigner import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Addition.clicked.connect(self.clicked)
        self.ui.Subtraction.clicked.connect(self.clicked)
        self.ui.Multiplication.clicked.connect(self.clicked)
        self.ui.Division.clicked.connect(self.clicked)


    def clicked(self):
        sender = self.sender() 
        result = 0 
        if sender.text() == "Addition": # type: ignore
            result = int(self.ui.Number_1.text()) + int(self.ui.lineEdit_2.text())
            self.ui.lbl_Result.setText(str(result)) # changes the text in the current lable to new message
        elif sender.text() == "Subtraction": # type: ignore
            result = int(self.ui.Number_1.text()) - int(self.ui.lineEdit_2.text())
            self.ui.lbl_Result.setText(str(result)) # changes the text in the current lable to new message
        elif sender.text() == "Multiplication": # type: ignore
            result = int(self.ui.Number_1.text()) * int(self.ui.lineEdit_2.text())
            self.ui.lbl_Result.setText(str(result)) # changes the text in the current lable to new message
        elif sender.text() == "Division": # type: ignore
            result = int(self.ui.Number_1.text()) / int(self.ui.lineEdit_2.text())
            self.ui.lbl_Result.setText(str(result)) # changes the text in the current lable to new message
      


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())


app()