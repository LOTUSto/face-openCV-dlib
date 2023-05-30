# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1281, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1284, 801))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(251,230,216,1), stop:1 rgba(15,124,190,1));\n"
"border-radius:80px")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-radius:80px")
        self.centralwidget.setObjectName("centralwidget")
        self.FramevfWindow = QtWidgets.QFrame(self.centralwidget)
        self.FramevfWindow.setGeometry(QtCore.QRect(940, 0, 351, 41))
        self.FramevfWindow.setStyleSheet("background-color:rgb(122,164,178);\n"
"border-radius:10px")
        self.FramevfWindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramevfWindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramevfWindow.setObjectName("FramevfWindow")
        self.ButtonSmall = QtWidgets.QPushButton(self.FramevfWindow)
        self.ButtonSmall.setGeometry(QtCore.QRect(150, 10, 93, 28))
        self.ButtonSmall.setStyleSheet("background-color:rgb(250,179,91);\n"
"border-radius:10px")
        self.ButtonSmall.setObjectName("ButtonSmall")
        self.ButtonExit = QtWidgets.QPushButton(self.FramevfWindow)
        self.ButtonExit.setGeometry(QtCore.QRect(252, 7, 91, 31))
        self.ButtonExit.setStyleSheet("background-color:rgb(250,179,91);\n"
"border-radius:10px;")
        self.ButtonExit.setObjectName("ButtonExit")
        self.FramevfMain = QtWidgets.QFrame(self.centralwidget)
        self.FramevfMain.setGeometry(QtCore.QRect(20, 50, 261, 711))
        self.FramevfMain.setStyleSheet("background-color:rgba(122,164,178,0.5);\n"
"border-radius:16px\n"
"")
        self.FramevfMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramevfMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramevfMain.setObjectName("FramevfMain")
        self.ButtonStart = QtWidgets.QPushButton(self.FramevfMain)
        self.ButtonStart.setGeometry(QtCore.QRect(10, 20, 241, 241))
        self.ButtonStart.setStyleSheet("background-color:rgb(250,179,91);\n"
"font: 75 28pt \"Agency FB\";\n"
"border-radius:80px;\n"
"")
        self.ButtonStart.setObjectName("ButtonStart")
        self.ButtonTrain = QtWidgets.QPushButton(self.FramevfMain)
        self.ButtonTrain.setGeometry(QtCore.QRect(20, 320, 221, 171))
        self.ButtonTrain.setStyleSheet("background-color:rgb(250,179,91);\n"
"border-radius:40px;\n"
"font: 75 28pt \"Agency FB\";")
        self.ButtonTrain.setObjectName("ButtonTrain")
        self.ButtonData = QtWidgets.QPushButton(self.FramevfMain)
        self.ButtonData.setGeometry(QtCore.QRect(20, 520, 221, 151))
        self.ButtonData.setStyleSheet("background-color:rgb(250,179,91);\n"
"border-radius:40px;\n"
"font: 75 28pt \"Agency FB\";")
        self.ButtonData.setObjectName("ButtonData")
        self.FrameText = QtWidgets.QFrame(self.centralwidget)
        self.FrameText.setGeometry(QtCore.QRect(330, 50, 221, 711))
        self.FrameText.setStyleSheet("background-color:rgb(122,164,178);\n"
"border-radius:80px")
        self.FrameText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameText.setObjectName("FrameText")
        self.textBrowser = QtWidgets.QTextBrowser(self.FrameText)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 181, 551))
        self.textBrowser.setStyleSheet("background:white;\n"
"border-radius:10px")
        self.textBrowser.setObjectName("textBrowser")
        self.FrameVideo = QtWidgets.QFrame(self.centralwidget)
        self.FrameVideo.setGeometry(QtCore.QRect(580, 50, 701, 711))
        self.FrameVideo.setStyleSheet("background-color:rgba(122,164,178,0.4);\n"
"border-radius:80px")
        self.FrameVideo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameVideo.setObjectName("FrameVideo")
        self.label = QtWidgets.QLabel(self.FrameVideo)
        self.label.setGeometry(QtCore.QRect(50, 30, 621, 651))
        self.label.setStyleSheet("background-color:rgb(250,179,91);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.photo = QtWidgets.QFrame(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(50, -180, 1221, 1051))
        self.photo.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0))")
        self.photo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.photo.setObjectName("photo")
        self.photoLabel = QtWidgets.QLabel(self.photo)
        self.photoLabel.setGeometry(QtCore.QRect(230, 240, 731, 641))
        self.photoLabel.setStyleSheet("background-color:rgba(0, 248, 248,0.3)")
        self.photoLabel.setText("")
        self.photoLabel.setObjectName("photoLabel")
        self.photoRun = QtWidgets.QPushButton(self.photo)
        self.photoRun.setGeometry(QtCore.QRect(970, 440, 231, 91))
        self.photoRun.setStyleSheet("border-radius:20px;\n"
"font: 75 18pt \"Agency FB\";\n"
"background-color:rgb(255, 255, 0)")
        self.photoRun.setObjectName("photoRun")
        self.photoReturn = QtWidgets.QPushButton(self.photo)
        self.photoReturn.setGeometry(QtCore.QRect(980, 700, 221, 91))
        self.photoReturn.setStyleSheet("border-radius:40px;\n"
"font: 75 22pt \"Agency FB\";\n"
"background-color:rgb(255, 255, 0)")
        self.photoReturn.setObjectName("photoReturn")
        self.lineEdit = QtWidgets.QLineEdit(self.photo)
        self.lineEdit.setGeometry(QtCore.QRect(980, 360, 201, 71))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"font: 75 16pt \"Agency FB\";")
        self.lineEdit.setObjectName("lineEdit")
        self.FrameStart = QtWidgets.QFrame(self.centralwidget)
        self.FrameStart.setGeometry(QtCore.QRect(10, 10, 1261, 791))
        self.FrameStart.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 192, 203, 0.7), stop:1 rgba(252, 177, 170, 0.6))")
        self.FrameStart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameStart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameStart.setObjectName("FrameStart")
        self.StartReturn = QtWidgets.QPushButton(self.FrameStart)
        self.StartReturn.setGeometry(QtCore.QRect(50, 30, 151, 71))
        self.StartReturn.setStyleSheet("background-color:rgb(250,179,91);\n"
"border-radius:20px;\n"
"font: 75 16pt \"Agency FB\";")
        self.StartReturn.setObjectName("StartReturn")
        self.eye = QtWidgets.QLabel(self.FrameStart)
        self.eye.setGeometry(QtCore.QRect(1041, 144, 161, 541))
        self.eye.setStyleSheet("background-color:rgb(0, 255, 127);\n"
"font: 75 48pt \"Agency FB\";")
        self.eye.setObjectName("eye")
        self.face = QtWidgets.QLabel(self.FrameStart)
        self.face.setGeometry(QtCore.QRect(40, 140, 161, 541))
        self.face.setStyleSheet("background-color:rgb(0, 255, 127);\n"
"font: 75 48pt \"Agency FB\";")
        self.face.setObjectName("face")
        self.StartLabel = QtWidgets.QLabel(self.FrameStart)
        self.StartLabel.setGeometry(QtCore.QRect(261, 44, 741, 651))
        self.StartLabel.setStyleSheet("background-color:rgb(245,245,220);")
        self.StartLabel.setText("")
        self.StartLabel.setObjectName("StartLabel")
        self.FramevfMain.raise_()
        self.FrameText.raise_()
        self.FrameVideo.raise_()
        self.photo.raise_()
        self.FrameStart.raise_()
        self.FramevfWindow.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonSmall.setText(_translate("MainWindow", "最小化"))
        self.ButtonExit.setText(_translate("MainWindow", "退出"))
        self.ButtonStart.setText(_translate("MainWindow", "开始"))
        self.ButtonTrain.setText(_translate("MainWindow", "训练数据"))
        self.ButtonData.setText(_translate("MainWindow", "拍照"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">操作记录:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">----------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.photoRun.setText(_translate("MainWindow", "拍照/保存"))
        self.photoReturn.setText(_translate("MainWindow", "返回"))
        self.StartReturn.setText(_translate("MainWindow", "返回"))
        self.eye.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">动</p><p align=\"center\">态</p><p align=\"center\">识</p><p align=\"center\">别</p></body></html>"))
        self.face.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">人</p><p align=\"center\">脸</p><p align=\"center\">检</p><p align=\"center\">测</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
