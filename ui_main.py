# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainXCWhSj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 827)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edit_frame = QFrame(self.centralwidget)
        self.edit_frame.setObjectName(u"edit_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_frame.sizePolicy().hasHeightForWidth())
        self.edit_frame.setSizePolicy(sizePolicy)
        self.edit_frame.setFrameShape(QFrame.StyledPanel)
        self.edit_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.edit_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.edit_form = QFormLayout()
        self.edit_form.setObjectName(u"edit_form")
        self.projectNameLabel = QLabel(self.edit_frame)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        self.projectNameLabel.setMinimumSize(QSize(100, 0))

        self.edit_form.setWidget(0, QFormLayout.LabelRole, self.projectNameLabel)

        self.projectNameComboBox = QComboBox(self.edit_frame)
        self.projectNameComboBox.setObjectName(u"projectNameComboBox")

        self.edit_form.setWidget(0, QFormLayout.FieldRole, self.projectNameComboBox)

        self.itemTypeLabel = QLabel(self.edit_frame)
        self.itemTypeLabel.setObjectName(u"itemTypeLabel")

        self.edit_form.setWidget(1, QFormLayout.LabelRole, self.itemTypeLabel)

        self.itemTypeComboBox = QComboBox(self.edit_frame)
        self.itemTypeComboBox.setObjectName(u"itemTypeComboBox")

        self.edit_form.setWidget(1, QFormLayout.FieldRole, self.itemTypeComboBox)

        self.vendorNameLabel = QLabel(self.edit_frame)
        self.vendorNameLabel.setObjectName(u"vendorNameLabel")

        self.edit_form.setWidget(2, QFormLayout.LabelRole, self.vendorNameLabel)

        self.vendorNameComboBox = QComboBox(self.edit_frame)
        self.vendorNameComboBox.setObjectName(u"vendorNameComboBox")

        self.edit_form.setWidget(2, QFormLayout.FieldRole, self.vendorNameComboBox)

        self.invoiceNumberLabel = QLabel(self.edit_frame)
        self.invoiceNumberLabel.setObjectName(u"invoiceNumberLabel")

        self.edit_form.setWidget(3, QFormLayout.LabelRole, self.invoiceNumberLabel)

        self.invoiceNumberLineEdit = QLineEdit(self.edit_frame)
        self.invoiceNumberLineEdit.setObjectName(u"invoiceNumberLineEdit")

        self.edit_form.setWidget(3, QFormLayout.FieldRole, self.invoiceNumberLineEdit)

        self.amountLabel = QLabel(self.edit_frame)
        self.amountLabel.setObjectName(u"amountLabel")

        self.edit_form.setWidget(4, QFormLayout.LabelRole, self.amountLabel)

        self.amountLineEdit = QLineEdit(self.edit_frame)
        self.amountLineEdit.setObjectName(u"amountLineEdit")

        self.edit_form.setWidget(4, QFormLayout.FieldRole, self.amountLineEdit)

        self.paidLabel = QLabel(self.edit_frame)
        self.paidLabel.setObjectName(u"paidLabel")

        self.edit_form.setWidget(5, QFormLayout.LabelRole, self.paidLabel)

        self.paidCheckBox = QCheckBox(self.edit_frame)
        self.paidCheckBox.setObjectName(u"paidCheckBox")

        self.edit_form.setWidget(5, QFormLayout.FieldRole, self.paidCheckBox)

        self.qBEnteredLabel = QLabel(self.edit_frame)
        self.qBEnteredLabel.setObjectName(u"qBEnteredLabel")

        self.edit_form.setWidget(6, QFormLayout.LabelRole, self.qBEnteredLabel)

        self.qBEnteredCheckBox = QCheckBox(self.edit_frame)
        self.qBEnteredCheckBox.setObjectName(u"qBEnteredCheckBox")

        self.edit_form.setWidget(6, QFormLayout.FieldRole, self.qBEnteredCheckBox)

        self.label = QLabel(self.edit_frame)
        self.label.setObjectName(u"label")

        self.edit_form.setWidget(7, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.edit_frame)
        self.label_2.setObjectName(u"label_2")

        self.edit_form.setWidget(7, QFormLayout.FieldRole, self.label_2)


        self.verticalLayout.addLayout(self.edit_form)

        self.buttonBox = QDialogButtonBox(self.edit_frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignRight)

        self.pushButton = QPushButton(self.edit_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(193, 0))

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.edit_frame, 1, 0, 1, 1)

        self.file_explorer_widget = QWidget(self.centralwidget)




        self.file_explorer_widget = QWidget(self.centralwidget)
        self.file_explorer_widget.setObjectName(u"file_explorer_widget")
        sizePolicy.setHeightForWidth(self.file_explorer_widget.sizePolicy().hasHeightForWidth())
        self.file_explorer_widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.file_explorer_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout_2.addWidget(self.file_explorer_widget, 0, 0, 1, 1)




        self.viewer_widget = QWidget(self.centralwidget)
        self.viewer_widget.setObjectName(u"viewer_widget")
        sizePolicy.setHeightForWidth(self.viewer_widget.sizePolicy().hasHeightForWidth())
        self.viewer_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.viewer_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout_2.addWidget(self.viewer_widget, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 936, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.projectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.itemTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Item Type", None))
        self.vendorNameLabel.setText(QCoreApplication.translate("MainWindow", u"Vendor Name", None))
        self.invoiceNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
        self.amountLabel.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.paidLabel.setText(QCoreApplication.translate("MainWindow", u"Paid", None))
        self.qBEnteredLabel.setText(QCoreApplication.translate("MainWindow", u"QB Entered", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Final File Name", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send to Project Folder", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

