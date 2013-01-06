from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog)
import sys
import ui_selectprojectdialog
import addproject

class SelectProject(QDialog,
        ui_selectprojectdialog.Ui_SelectProjectDialog):

    def __init__(self, parent=None):
        super(SelectProject, self).__init__(parent)
        self.setupUi(self)

    @pyqtSignature("")
    def on_AddProjectPushButton_clicked(self):
        dialog = addproject.AddProject(self)
        if dialog.exec_():
            self.refreshProjectList()

    def refreshProjectList(self):
        self.center()

