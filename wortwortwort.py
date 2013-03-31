#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import Qt, SIGNAL, pyqtSignature
from PyQt4.QtGui import QApplication, QWidget, QDesktopWidget

import sys
import ui_timetrackerdialog
import selectproject

from wortwortwort import orm


MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class WortwortwortMainDialog(QWidget,
        ui_timetrackerdialog.Ui_TimeTrackerDialog):

    def __init__(self, parent=None):
        super(WortwortwortMainDialog, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.setup_database()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setup_database(self):
        self.orm = orm.Manager()

    @pyqtSignature("")
    def on_changeProjectPushButton_clicked(self):
        dialog = selectproject.SelectProject(parent=self)
        if dialog.exec_():
            self.setProject()
       
    def setProject(self):
        self.center()

 

app = QApplication(sys.argv)
main_dialog = WortwortwortMainDialog()
main_dialog.show()
sys.exit(app.exec_())
 
