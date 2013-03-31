from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog)
import sys
import ui_selectprojectdialog
import addproject

from wortwortwort import projects

class SelectProject(QDialog,
        ui_selectprojectdialog.Ui_SelectProjectDialog):

    def __init__(self, parent=None):
        super(SelectProject, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
#        self.ProjectListView.setModel(
#            projects.ListModel(parent.orm.project_types()))

    @pyqtSignature("")
    def on_AddProjectPushButton_clicked(self):
        dialog = addproject.AddProject(self.parent.orm.project_types(), parent=self)
        if dialog.exec_():
            self.refreshProjectList()

    def refreshProjectList(self):
        self.center()

