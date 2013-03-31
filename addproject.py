from __future__ import (
    division,
    print_function,
    unicode_literals
    )

from future_builtins import *

from PyQt4.QtCore import (
    Qt,
    SIGNAL,
    pyqtSignature
    )

from PyQt4.QtGui import (
    QApplication,
    QDialog
    )

from wortwortwort import projects

from wortwortwort.orm import (
    DBSession,
    Project,
    ProjectType,
    Config,
    )

import sys
import ui_addprojectdialog

class AddProject(QDialog, ui_addprojectdialog.Ui_AddProjectDialog):

    def __init__(self, parent=None):
        super(AddProject, self).__init__(parent)
        self.setupUi(self)
        self.types = DBSession.query(ProjectType).all()
        self.ProjectTypeComboBox.setModel(projects.ListModel(self.types))

    @pyqtSignature("int")
    def on_ProjectTypeComboBox_currentIndexChanged(self, index):
        project_type = self.types[index]
        if project_type.name == "CodebaseHQ":
            self.groupBox.show()
        else:
            self.groupBox.hide()

    def on_buttonBox_accepted(self):
        project_name = unicode(self.ProjectNameLineEdit.text())
        project_type = self.types[self.ProjectTypeComboBox.currentIndex()]

        if not project_name == "":
            project = Project(name=project_name)
            project.project_type = project_type
            project.config.append(Config(name="CBAUTY", value="SOME VALUE"))
            DBSession.add(project)
            DBSession.commit()
