#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QWidget, QDesktopWidget)

import sys
import ui_timetrackerdialog
import selectproject
import addproject

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class WortwortwortDialog(QWidget, ui_timetrackerdialog.Ui_TimeTrackerDialog):

    def __init__(self, parent=None):
        super(WortwortwortDialog, self).__init__(parent)
        self.setupUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSignature("")
    def on_changeProjectPushButton_clicked(self):
        dialog = selectproject.SelectProject(self)
        if dialog.exec_():
            self.setProject()
       
    def setProject(self):
        self.center()

    @pyqtSignature("")
    def on_AddProjectPushButton_clicked(self):
        dialog = addproject.AddProject(self)
        if dialog.exec_():
            self.refreshProjectList()
            
    def refreshProjectList(self):
        self.center()


app = QApplication(sys.argv)
form = WortwortwortDialog()
form.show()
sys.exit(app.exec_())
 
