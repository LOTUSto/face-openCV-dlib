import cv2 as cv

from workpiece import work


class Count:
    def __init__(self):
        self.i = 0
        self.label = 0


class PhotoGraph():
    def __init__(self):
        self.co = Count()
        self.name = "test"
        self.cap = work.cap

    def mkdir(self, path):
        import os
        path = path.strip()
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False

    def face_detect_demo(self, img, co: Count):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_detect = cv.CascadeClassifier(
            './data/model/haarcascade_frontalface_default.xml')
        face = face_detect.detectMultiScale(gray, 1.5, 1)
        for x, y, w, h in face:
            # cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
            # result = img[y:y + w, x:x + h]
            if co.label < 20:
                self.mkdir(f"./resource/{self.name}")
                # cv.imwrite(f"./resource/{name}/{co.i}.jpg",result)
                cv.imwrite(f"./resource/{self.name}/{co.i}.jpg", img)
                co.i += 1
                co.label += 1
        # cv.imshow('result',img)

    def run(self):
        # co = Count()
        # self.name = input("请输入拍摄的人名_:")
        #
        # # cap = cv.VideoCapture(0)
        #
        # flag, img = self.cap.read()
        # print("按Q键确认,开始录入人脸信息")
        # while True:
        #     flag, img = self.cap.read()
        #     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #     face_detect = cv.CascadeClassifier(
        #         'C:/Users/LOTUS/Desktop/python/OpenCV/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml')
        #     face = face_detect.detectMultiScale(gray, 1.3, 3)
        #     for x, y, w, h in face:
        #         cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        #     cv.imshow('photoGraph', img)
        #
        #     if ord('q') == cv.waitKey(5):
        #         break
        self.name = work.name
        flag, img = self.cap.read()
        while True:
            flag, frame = self.cap.read()
            if not flag:
                break
            self.face_detect_demo(frame, self.co)

            if self.co.label >= 20:
                print(f"姓名为{self.name}的人脸信息以录入完成")
                break

            # cv.imshow("su",face)

        # self.cap.release()
        cv.destroyAllWindows()

if __name__ == '__main__':
    photo = PhotoGraph()
    photo.run()
