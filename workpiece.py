import cv2

from threading import Thread

import mouth as mu
import result as res
import train as Tr

# result = res.Result()
# photograph = photograph.PhotoGraph()
# mouth = mouth.Mouth()

class Work:
    def __init__(self):
        self.colour = (0, 0, 255)

        self.cap = cv2.VideoCapture(0)
        flag, frame = self.cap.read()
        self.image = frame
        self.threadRead = Thread(target=self.read)

        self.result = res.Result()

        self.mouth = mu.Mouth()

        self.threadCheckMouth = Thread(target=self.checkMouth)

        self.threadCheckFace = Thread(target=self.checkFace)

        self.agree = False
        self.threadTrain = Thread(target=self.new_result)
        self.trainResult = ''


        self.win_image = cv2.resize(self.image, (640, 470))

        self.stop = True

        self.check = False

        self.name = ''

        self.resultCheck = ''
        self.resultActive = ''



    def style(self):
        pass

    def read(self):
        while self.stop:
            _,self.image = self.cap.read()
            self.win_image = cv2.resize(self.image, (640, 470))

    def checkFace(self):
        print("线程checkMouth开始")
        while self.stop:
            # self.result.run(self.image)
            if self.check:
                # print("checkMouth")
                self.resultCheck = self.result.run(self.cap)
                print("self.resultCheck:",self.resultCheck)
                self.check = False
        # cv2.destroyAllWindows()
        # while self.check == False:
        #     pass
        #
        # self.result.run(self.cap)
        #
        print("线程checkMouth结束")



    def checkMouth(self):
        print("线程checkFace开始")
        # while self.check == False:
        #     pass
        while self.stop:
        # self.mouth.run(self.cap,self.image)
            if self.check:
                self.resultActive = self.mouth.run(self.cap)
                print("self.resultActive: ",self.resultActive)
                self.check = False
        # self.mouth.run(self.cap)

        print("线程checkFace结束")

    def new_result(self):
        while self.stop:
            if self.agree:
                print("work开始训练")
                Tr.train()
                self.result = res.Result()
                print("work训练成功")
                self.trainResult = "成功训练数据"
                self.agree = False


work = Work()


if __name__ == '__main__':
    print(work.check)
