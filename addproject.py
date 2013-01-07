from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog)
import sys
import ui_addprojectdialog

class AddProject(QDialog, ui_addprojectdialog.Ui_AddProjectDialog):

    def __init__(self, parent=None):
        super(AddProject, self).__init__(parent)
        self.setupUi(self)
        
        self.ProjectTypeComboBox.addItems(['CodeBaseHQ'])
        self.ProjectTypeComboBox.addItems(['Custom'])


