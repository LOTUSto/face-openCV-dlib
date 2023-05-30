import json

import cv2

# from workpiece import work


class Result:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('./data/default_train.yml')  # 读取前文训练的结果

        self.load_dict = {}
        # 此函数识别图像中的人物并在脸部周围绘制一个矩形及其人名
        with open("./data/data.json", 'r', encoding='UTF-8') as f:
            self.load_dict = json.load(f)
        print(self.load_dict)
        self.facelabel = [i for i in self.load_dict.values()]  # 人物名

        self.count = {}
        self.count["not find"] = 0
        for i in self.facelabel:
            self.count[i] = 0;
        print(self.facelabel)

        # self.cap = work.cap

    # 人脸检测函数
    def face_detect_demo(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_detector = cv2.CascadeClassifier(
            "./data/model/haarcascade_frontalface_default.xml")
        faces = face_detector.detectMultiScale(gray, 1.2, 3)
        # 如果未检测到面部，则返回原始图像
        if (len(faces) == 0):
            return gray, (0, 0, 0, 0)
        # 目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高
        (x, y, w, h) = faces[0]
        # 返回图像的脸部部分
        return gray[y:y + w, x:x + h], faces[0]

    # 根据给定的人脸（x，y）坐标和宽度高度在图像上绘制矩形
    def draw_rectangle(self, img, rect):
        (x, y, w, h) = rect  # 矩形框
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    # 根据给定的人脸（x，y）坐标写出人名
    def draw_text(self, img, text, x, y):
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 0), 2)

    def predict(self, image):
        # 生成图像的副本，保留原始图像
        img = image.copy()
        # 检测人脸区域
        face, rect = self.face_detect_demo(img)  # face_detect_demo前面的人脸检测函数
        # print(rect)=[x,y,w,h]
        # 预测人脸名字
        label = self.recognizer.predict(face)
        # print(label)  # label[0]为名字，label[1]可信度数值越低，可信度越高（
        if label[1] <= 41:
            # 获取由人脸识别器返回的相应标签的人名
            label_text = self.facelabel[label[0]]
            self.count[self.facelabel[label[0]]] += 1

            # 在检测到的脸部周围画一个矩形
            self.draw_rectangle(img, rect)
            # 标出预测的人名
            self.draw_text(img, label_text, rect[0], rect[1])
            # 返回预测的图像
            return img
        else:
            # 在检测到的脸部周围画一个矩形
            self.draw_rectangle(img, rect)
            # 标出预测的人名
            self.draw_text(img, "not find", rect[0], rect[1])
            self.count["not find"] += 1
            # 返回预测的图像
            return img


    def run(self,cap):
        print("开始result")
        for k, v in self.count.items():
            self.count[k] = 0

        print(self.count)
        while True:
            flag, image = cap.read()

            stop = False
            # if not flag:
            #     break
            pred_img = self.predict(image)

            cv2.waitKey(3)
            # if ord('w') == cv2.waitKey(3):
            #     break
            for k,v in self.count.items():
                if k != "not find" and v > 15:
                    # print("检测成功,结果为",k)
                    stop = True
                    # cv2.destroyWindow('result')
                    return k

                if self.count["not find"] > 70:
                    # print("检测失败")
                    stop = True
                    # cv2.destroyWindow('result')
                    return "not find"

            if stop:
                break
        # self.cap.release()
        # cv2.destroyWindow ('result')
        print("结束result")





if __name__ == '__main__':
    # 导入训练结果
    cap = cv2.VideoCapture(0)
    result = Result()
    result.run(cap)

    count = 0
    while True:
        count += 1
        print(count)
        if count > 200:
            break
