import sys
from PySide2.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PySide2.QtCore import QModelIndex

class FileSystemView(QWidget):
	def __init__(self, dir_path):
		super().__init__()
		# appWidth = 800
		# appHeight = 300
		self.setWindowTitle('File System Viewer')
		# self.setGeometry(300, 300, appWidth, appHeight)
        
		self.model = QFileSystemModel()
		self.model.setRootPath(dir_path)
		self.tree = QTreeView()
		self.tree.setModel(self.model)
		self.tree.setRootIndex(self.model.index(dirPath))
		self.tree.setColumnWidth(0, 250)
		self.tree.setAlternatingRowColors(True)

		layout = QVBoxLayout()
		layout.addWidget(self.tree)
		self.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dirPath = r'Z:\01 - L8 - back office\01 - L8 INBOX\chiyumi_hold'
	demo = FileSystemView(dirPath)
	demo.show()
	sys.exit(app.exec_())


# ################################################################################
# ## Form generated from reading UI file 'designerBUMxtP.ui'
# ##
# ## Created by: Qt User Interface Compiler version 5.15.1
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################

# import sys
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *



# class FileSystemView(object):
#     def __init__(self, dir_path):
#         super().__init__()

#     def setupUi(self, Form):
#         if not Form.objectName():
#             Form.setObjectName(u"Form")
#         Form.resize(400, 300)

#         self.model = QFileSystemModel()
#         self.model.setRootPath(dir_path)
#         self.tree = QTreeView()
#         self.tree.setModel(self.model)
#         self.tree.setRootIndex(self.model.index(dirPath))
#         self.tree.setColumnWidth(0, 250)
#         self.tree.setAlternatingRowColors(True)

#         layout = QVBoxLayout()
#         layout.addWidget(self.tree)
#         self.setLayout(layout)



#         self.retranslateUi(Form)

#         QMetaObject.connectSlotsByName(Form)
#     # setupUi

#     def retranslateUi(self, Form):
#         Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#     # retranslateUi


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dirPath = r'Z:\01 - L8 - back office\01 - L8 INBOX\chiyumi_hold'
#     demo = FileSystemView(dirPath)
#     demo.show()
#     sys.exit(app.exec_())