import json
import os

import cv2
import numpy as np


class user:
    def __init__(self, name):
        self.name = name
        self.face = []

    def data_source(self):
        filePath = './resource/' + self.name
        datas = os.listdir(filePath)
        for data in datas:
            image = cv2.imread(filePath + '/' + data)
            result_face, rect = self.looking(image)
            down_points = (213, 213)
            resized_down = cv2.resize(result_face, down_points, interpolation=cv2.INTER_LINEAR)

            print(self.name + "/" + data)
            self.face.append(resized_down)

    def label_get(self, num):
        self.data_source()
        self.label = np.array([num for i in range(len(self.face))])

    def __str__(self):
        return self.name

    def looking(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_detector = cv2.CascadeClassifier(
            "./data/model/haarcascade_frontalface_default.xml")
        faces = face_detector.detectMultiScale(gray, 1.2, 6)
        # 如果未检测到面部，则返回原始图像
        if (len(faces) == 0):
            return gray, None
        # 目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高
        (x, y, w, h) = faces[0]
        # 返回图像的脸部部分
        return gray[y:y + w, x:x + h], faces[0]


# class Train:
#     def __init__(self):
#         self.name_dic = {}
def train():
    name_dic = {}
    filePath = './resource/'
    names = os.listdir(filePath)
    i = 0
    for name in names:
        name_dic[i] = user(name)
        name_dic[i].label_get(i)
        i += 1

    for k, v in name_dic.items():
        print(k, v)

    print("混合数据ing")
    x = name_dic[0].face
    y = name_dic[0].label
    for k, v in name_dic.items():
        if v == 0:
            continue
        x = np.concatenate((x, name_dic[k].face), axis=0)
        y = np.concatenate((y, name_dic[k].label), axis=0)

    index = [i for i in range(len(y))]  # test_data为测试数据

    np.random.seed(1)
    np.random.shuffle(index)  # 打乱索引
    train_data = x[index]
    train_label = y[index]

    print("开始训练")
    # 分类器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(train_data, train_label)
    # 保存训练数据
    recognizer.write('./data/default_train.yml')

    res_dic = {}
    for k, v in name_dic.items():
        res_dic[k] = v.name
        print(k, v)

    print(res_dic)
    with open("./data/data.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(res_dic, ensure_ascii=False, indent=4))
    print("训练成功")


# if __name__ == "__main__":
#     name_dic = {}
#     filePath = './resource/'
#     names = os.listdir(filePath)
#     i = 0
#     for name in names:
#         name_dic[i] = user(name)
#         name_dic[i].label_get(i)
#         i += 1
#
#     for k, v in name_dic.items():
#         print(k, v)
#
#     print("混合数据ing")
#     x = name_dic[0].face
#     y = name_dic[0].label
#     for k, v in name_dic.items():
#         if v == 0:
#             continue
#         x = np.concatenate((x, name_dic[k].face), axis=0)
#         y = np.concatenate((y, name_dic[k].label), axis=0)
#
#     index = [i for i in range(len(y))]  # test_data为测试数据
#
#     np.random.seed(1)
#     np.random.shuffle(index)  # 打乱索引
#     train_data = x[index]
#     train_label = y[index]
#
#     print("开始训练")
#     # 分类器
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.train(train_data, train_label)
#     # 保存训练数据
#     recognizer.write('./data/default_train.yml')
#
#     res_dic = {}
#     for k, v in name_dic.items():
#         res_dic[k] = v.name
#         print(k, v)
#
#     print(res_dic)
#     with open("./data/data.json", 'w', encoding='utf-8') as f:
#         f.write(json.dumps(res_dic, ensure_ascii=False, indent=4))
#     print("训练成功")
