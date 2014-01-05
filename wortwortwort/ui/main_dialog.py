import ui_timetrackerdialog
import selectproject

class WortwortwortMainDialog(QWidget,
        ui_timetrackerdialog.Ui_TimeTrackerDialog):

    def __init__(self, parent=None):
        super(WortwortwortMainDialog, self).__init__(parent)
        self.setupUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSignature("")
    def on_changeProjectPushButton_clicked(self):
        dialog = selectproject.SelectProject(parent=self)
        if dialog.exec_():
            self.setProject()
       
    def setProject(self):
        self.center()

