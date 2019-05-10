from PyQt5 import QtWidgets, QtGui, QtCore
from Prediction_UI import Ui_MainWindow
import cv2


class mywindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(mywindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.importImage.clicked.connect(self.on_btn_import_clicked)

    def on_btn_import_clicked(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "OpenFile", ".", "Image Files(*.jpg *.jpeg *.png)")[0]
        if len(filename):
            self.img = cv2.imread(filename)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # Change channel
            x = self.img.shape[1]  # Get the size of the image
            y = self.img.shape[0]
            zoom = 1  # zoom of the image
            frame = QtGui.QImage(self.img, x, y, QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(frame)
            item = QtWidgets.QGraphicsPixmapItem(pix)  # make the pix map
            item.setScale(zoom)
            scene = QtWidgets.QGraphicsScene()  # to fit the scene of the UI
            scene.addItem(item)
            self.ui.originalVIew.setScene(scene)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
