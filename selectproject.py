from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog, QWidget, QDesktopWidget)
import sys
import ui_selectprojectdialog

class SelectProject(QDialog,
        ui_selectprojectdialog.Ui_SelectProjectDialog):

    def __init__(self, parent=None):
        super(SelectProject, self).__init__(parent)
        self.setupUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


