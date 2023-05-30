import sys
import time

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

# import mouth
import photograph
# import result as res
import train
from qt import Ui_MainWindow
from workpiece import work

# result = res.Result()
photograph = photograph.PhotoGraph()
# mouth = mouth.Mouth()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.timer_camera = QTimer()  # 初始化定时器

        self.timer_camera.timeout.connect(self.show_camera)

        # show = cv2.resize(work.image, (480, 320))
        show = cv2.cvtColor(work.win_image, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(showImage))

        self.record = 1

        self.ButtonStart.setStyleSheet(
            "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}")

        self.ButtonTrain.setStyleSheet(
            "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}")

        self.ButtonData.setStyleSheet(
            "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}"
        )

        self.ButtonExit.setStyleSheet(
            # "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}"
        )

        self.ButtonSmall.setStyleSheet(
            # "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}"
        )

        self.StartReturn.setStyleSheet(
            "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}"
        )

        self.photoRun.setStyleSheet(
            "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}"
        )

        self.photoReturn.setStyleSheet(
            "QPushButton{font: 75 28pt 'Agency FB'}"
            "QPushButton{background-color: rgb(242,171,57);}"
            "QPushButton:hover{background-color: rgb(228,182,96);}"
            "QPushButton:pressed{background-color: rgb(255,217,84);}"
        )

        self.ButtonStart.clicked.connect(self.StartFrame)
        self.StartReturn.clicked.connect(self.mainWindow)

        self.ButtonExit.clicked.connect(self.Win_close)

        self.ButtonTrain.clicked.connect(self.Train)

        self.ButtonData.clicked.connect(self.photoWindow)

        work.threadRead.start()
        work.threadCheckFace.start()
        work.threadCheckMouth.start()
        work.threadTrain.start()

        self.timer_camera.start(30)

        self.photo.hide()
        self.FrameStart.hide()

        self.photoReturn.clicked.connect(self.mainWindow)

        self.photoRun.clicked.connect(self.PhotoRun)


        self.photoLabel.setPixmap(QPixmap.fromImage(showImage))

    def StartFrame(self):
        self.FramevfMain.hide()
        self.FrameVideo.hide()
        self.FrameText.hide()
        self.FrameStart.show()

        self.StartReturn.hide()
        print("开始窗口")
        # work.threadCheckFace.start()
        # work.threadCheckMouth.start()
        work.check = True





    def show_camera(self):
        show = cv2.cvtColor(work.win_image, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))
        self.photoLabel.setPixmap(QPixmap.fromImage(showImage))
        self.StartLabel.setPixmap(QPixmap.fromImage(showImage))
        if work.resultActive != '' and work.resultCheck != '':
            QMessageBox.information(self, "提示", f"检测结果:\n姓名为:{work.resultCheck}\n活体检测结果:\n{work.resultActive}",
                                    QMessageBox.Yes)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

            self.textEdit.append(f"\n第{self.record}条记录\n检测结果:{work.resultCheck},{work.resultActive}\n")


            self.record = self.record+1
            work.resultActive = ''
            work.resultCheck = ''
            self.StartReturn.show()

        if work.trainResult != '':
            self.textEdit.append(f"\n第{self.record}条记录\n{work.trainResult}\n")

            self.record = self.record + 1
            work.trainResult = ''



    def Win_close(self):

        work.stop = False
        self.close()

    def photoWindow(self):
        self.FramevfMain.hide()
        self.FrameVideo.hide()
        self.FrameText.hide()
        self.photo.show()
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("请输入姓名...")

    def mainWindow(self):
        self.FramevfMain.show()
        self.FrameVideo.show()
        self.FrameText.show()
        self.photo.hide()
        self.FrameStart.hide()
        work.check = False

    def Train(self):
        # train.train()
        # work.new_result()
        if work.agree  == True:
            print("正在执行训练")
            work.trainResult = "训练正在执行中,请不要重复操作"
            return

        work.agree = True
        # self.textEdit.append(f"\n第{self.record}条记录\n成功更新数据\n")
        # self.record = self.record + 1

    def PhotoRun(self):
        if self.lineEdit.text() != "":
            work.name = self.lineEdit.text()
            # print(self.lineEdit.text())
            photograph.run()
            self.textEdit.append(f"\n第{self.record}条记录\n成功录入 {self.lineEdit.text()} 的信息\n")
            self.record = self.record + 1
        else:
            # print(self.lineEdit.text)
            QMessageBox.information(self, "提示", "请在上方输入你的名字",
                                    QMessageBox.Yes)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认


if __name__ == '__main__':
    # 测试,拍照
    # photograph.run()
    # 测试训练
    # train.train()
    # 测试模型
    # result.run(cap)
    # 张嘴识别
    # mouth.run(cap)
    # 初始化APP
    app = QApplication(sys.argv)
    # 创建窗口
    win = MainWindow()
    # 绘制窗口
    win.show()
    # 循环绘制
    sys.exit(app.exec_())

    work.cap.release()
    cv2.destroyAllWindows()
