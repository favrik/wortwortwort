#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import Qt, SIGNAL, pyqtSignature
from PyQt4.QtGui import QApplication, QWidget, QDesktopWidget

import sys
import wortwortwort

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

app = QApplication(sys.argv)
main_dialog = wortwortwort.ui.MainDialog()
main_dialog.show()
sys.exit(app.exec_())
