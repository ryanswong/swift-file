# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\menubar_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 60, 361, 221))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 47))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        self.actionpaste.setObjectName("actionpaste")
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionsave)
        self.menuedit.addAction(self.actioncopy)
        self.menuedit.addAction(self.actionpaste)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionnew.triggered.connect(lambda: self.clicked("new was clicked"))
        self.actionsave.triggered.connect(lambda: self.clicked("save was clicked"))
        self.actioncopy.triggered.connect(lambda: self.clicked("copy was clicked"))
        self.actionpaste.triggered.connect(lambda: self.clicked("paste was clicked"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionnew.setStatusTip(_translate("MainWindow", "create a new file"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave.setStatusTip(_translate("MainWindow", "save a file"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actioncopy.setStatusTip(_translate("MainWindow", "copy file"))
        self.actioncopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionpaste.setText(_translate("MainWindow", "paste"))
        self.actionpaste.setStatusTip(_translate("MainWindow", "paste file"))
        self.actionpaste.setShortcut(_translate("MainWindow", "Ctrl+V"))



    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
