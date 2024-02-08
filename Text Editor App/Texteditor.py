from PyQt5 import QtWidgets
import sys
from editui import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.Save_file.clicked.connect(self.clicked)
        self.ui.Open_file.clicked.connect(self.clicked)
        self.ui.Redo.clicked.connect(self.clicked)
        self.ui.Undo.clicked.connect(self.clicked)


    def clicked(self):
        sender = self.sender()
        if sender.text() == "Save File": # type: ignore
            filepath = "Text Editor App\\SavedFiles\\" 
            text_file = open(f"{filepath}{self.ui.File_Name.text()}.txt","w+") # converts the text
            text_file.write(self.ui.Workspace.toPlainText())
                 
        elif sender.text() == "Open File": # type: ignore
            #finds the file using the file name types on the top, converts the text into the textbox
            filepath_2 = "Text Editor App\\SavedFiles\\" + self.ui.File_Name.text() + ".txt"
            contents = open(filepath_2, "r") 
            file_content = contents.read()
            self.ui.Workspace.setPlainText(file_content)

        elif sender.text() == "Undo": # type: ignore
            self.ui.Workspace.undo()
        elif sender.text() == "Redo": # type: ignore
            self.ui.Workspace.redo()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())


app()