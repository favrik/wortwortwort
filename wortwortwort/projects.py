from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import platform

from PyQt4.QtCore import (QAbstractListModel, QDataStream, QFile,
        QIODevice, QModelIndex, QRegExp, QSize, QString, QVariant, Qt,
        SIGNAL)
from PyQt4.QtGui import (QApplication, QColor, QComboBox, QLineEdit,
        QSpinBox, QStyle, QStyledItemDelegate, QTextDocument, QTextEdit)


class ListModel(QAbstractListModel):
    
    def __init__(self, items):
        super(ListModel, self).__init__()
        self.items = items

    def rowCount(self, index=QModelIndex()):
        return len(self.items)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        return QVariant("Name")

    def data(self, index, role=Qt.DisplayRole):
        if (not index.isValid() or
            not (0 <= index.row() < len(self.items))):
            return QVariant()

        if role == Qt.DisplayRole:
            return QVariant(self.items[index.row()].name)








