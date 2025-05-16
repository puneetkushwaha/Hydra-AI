from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("Hydra")
        MainWindow.resize(1440, 900)
        MainWindow.setWindowTitle("HYDRA AI")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: black;")

        self.label = QtWidgets.QLabel(self.centralwidget)
        label_width = 800
        label_height = 600

        window_width = 1440
        window_height = 900
        pos_x = (window_width - label_width) // 2 + 30 
        pos_y = (window_height - label_height) // 2

        self.label.setGeometry(QtCore.QRect(pos_x, pos_y, label_width, label_height))
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: transparent;") 
        self.label.setScaledContents(False)  

        image_path = "Hydra/utils/images/hydra_image.jpeg"

        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print(f"Failed to load image (pixmap is null): {image_path}")
                self.label.setText("Failed to load background image.")
                self.label.setStyleSheet("color: white; font-size: 24px; background-color: black;")
            else:
                scaled_pixmap = pixmap.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.label.setPixmap(scaled_pixmap)
        else:
            print(f"Image not found at: {image_path}")
            self.label.setText("Background image not found.")
            self.label.setStyleSheet("color: white; font-size: 24px; background-color: black;")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 91))
        self.label_2.setText("")
        self.label_2.setStyleSheet("background-color: transparent;")

        initiating_possible_paths = [
            "Hydra/utils/images/initiating.gif",
            "C:/Users/Puneet/Desktop/YourProject/Hydra/utils/images/initiating.gif",
            "./Hydra/utils/images/initiating.gif"
        ]

        self.movie2 = None
        for path in initiating_possible_paths:
            if os.path.exists(path):
                movie = QtGui.QMovie(path)
                if movie.isValid():
                    self.movie2 = movie
                    self.label_2.setMovie(self.movie2)
                    self.movie2.start()
                    break

        if self.movie2 is None or not self.movie2.isValid():
            print("Initiating GIF not found or invalid. Showing placeholder text.")
            self.label_2.setText("Initiating GIF not found.")
            self.label_2.setStyleSheet("color: white; font-size: 16px; background-color: transparent;")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1180, 800, 101, 51))
        self.pushButton.setStyleSheet(
            "background-color: rgb(0, 170, 255);"
            "font: 75 18pt \"MS Shell Dlg 2\";"
            "color: white;"
            "border-radius: 10px;"
        )
        self.pushButton.setText("Run")
        self.pushButton.clicked.connect(self.run_function)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 800, 101, 51))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 0, 0);"
            "font: 75 18pt \"MS Shell Dlg 2\";"
            "color: white;"
            "border-radius: 10px;"
        )
        self.pushButton_2.setText("Exit")
        self.pushButton_2.clicked.connect(QtWidgets.qApp.quit)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(640, 30, 291, 61))
        self.textBrowser.setStyleSheet(
            "font: 75 16pt \"MS Shell Dlg 2\";"
            "background-color: transparent;"
            "color: white;"
            "border-radius: none;"
        )

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(930, 30, 291, 61))
        self.textBrowser_2.setStyleSheet(
            "font: 75 16pt \"MS Shell Dlg 2\";"
            "background-color: transparent;"
            "color: white;"
            "border-radius: none;"
        )

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1000, 500, 431, 281))
        self.textBrowser_3.setStyleSheet(
            "font: 11pt \"MS Shell Dlg 2\";"
            "background-color: transparent;"
            "color: white;"
        )

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

    def run_function(self):
        self.textBrowser_3.setText("🧠 HYDRA is now running...\nAwaiting your command.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
