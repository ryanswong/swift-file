import sys
import platform
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow
from file_explorer_widget import FileSystemView

# # IMPORT FUNCTIONS
# from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.file_explorer_widget = FileSystemView

        ## TOGGLE/BURGUER MENU
        ########################################################################

        ## PAGES
        ########################################################################



        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())