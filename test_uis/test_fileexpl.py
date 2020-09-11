from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
import sys


class Myview(QtWidgets.QMainWindow):
    def __init__(self):
        super(Myview, self).__init__()
        model = QtWidgets.QFileSystemModel()
        model.setRootPath('C:\Myfolder')
        view = QtWidgets.QTreeView()
        view.setModel(model)
        self.setCentralWidget(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myview = Myview()
    myview.show()
    sys.exit(app.exec_())
