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

from wortwortwort.orm import (
    DBSession,
    Project,
    )

class SelectProject(QDialog,
        ui_selectprojectdialog.Ui_SelectProjectDialog):

    def __init__(self, parent=None):
        super(SelectProject, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ProjectListView.setModel(
            projects.ListModel(DBSession.query(Project).all()))


    @pyqtSignature("")
    def on_AddProjectPushButton_clicked(self):
        dialog = addproject.AddProject(parent=self)
        if dialog.exec_():
            self.refreshProjectList()

    def refreshProjectList(self):
        self.center()

