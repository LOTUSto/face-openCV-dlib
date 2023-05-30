import math

import cv2
import dlib
from imutils import face_utils

# from workpiece import work


# 计算两个坐标的距离
def euclidian_distance(p1, p2):
    diff_x = abs(p2[0] - p1[0])
    diff_y = abs(p2[1] - p1[1])
    return math.sqrt(diff_x * diff_x + diff_y * diff_y)


class Mouth:
    def __init__(self):
        # 使用 Dlib 的正面人脸检测器 frontal_face_detector
        self.detector = dlib.get_frontal_face_detector()

        # 脸部关键点预测器
        self.predictor = dlib.shape_predictor("./data/dlib/shape_predictor_68_face_landmarks.dat")

        # self.cap = work.cap

    def run(self,cap):
        print("开始mouth")
        # cap = cv2.VideoCapture(0)  # 这是选择打开自己的摄像头

        fps = cap.get(cv2.CAP_PROP_FPS)  # 获取摄像头或者视频帧率


        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        (mouth_lower, mouth_upper) = (48, 60)

        ACTIVATION_RATIO = 1.8

        color = (0, 0, 255)
        actived = False
        result = []
        sum = 0
        j = 0
        fras = 0

        status = False
        sec_status = False
        count_status = 0

        while (True):

            # if (fras >= count):
            #     break

            ret, frame = cap.read()
            # 使用 detector 检测器来检测图像中的人脸
            faces = self.detector(frame, 1)

            if (len(faces) > 0):
                for (i, face) in enumerate(faces):

                    fx = face.left()
                    fy = face.top()

                    # 确定面部区域的面部地标，然后将面部标志（x，y）坐标转换成NumPy阵列
                    # 使用predictor来计算面部轮廓
                    shape = self.predictor(frame, face)
                    shape = face_utils.shape_to_np(shape)

                    left = (shape[48, 0], shape[48, 1])
                    right = (shape[54, 0], shape[54, 1])

                    top = (shape[51, 0], shape[51, 1])
                    bottom = (shape[57, 0], shape[57, 1])

                    diff_h = euclidian_distance(top, bottom)
                    diff_w = euclidian_distance(left, right)

                    ratio = round(diff_w / diff_h, 5)

                    cv2.line(frame, left, right, color)
                    cv2.line(frame, top, bottom, color)

                    # 绘制嘴巴的点
                    for (x, y) in shape[mouth_lower:mouth_upper]:
                        cv2.circle(frame, (x, y), 1, color, -3)
                    if ratio >= ACTIVATION_RATIO:  # mouth shut & not talking
                        sec_status = True
                        # print("闭着嘴巴")
                        result.append(0)

                    else:
                        sec_status = False
                        # print("张开嘴巴")
                        result.append(1)


            else:
                cv2.putText(frame, "no face", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            cv2.waitKey(1)
            if status != sec_status:
                count_status += 1
                status = sec_status

            fras = fras + 1

            if count_status > 5 and fras < 100:
                # print("动态识别通过")
                return "动态识别通过"
                # return True
            if fras > 60:
                # print("动态识别未通过")
                # return False
                return "动态识别...未通过"
                # break

        # cv2.destroyAllWindows()
        # cv2.destroyWindow('result')
        print("结束mouth")



if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    mouth = Mouth()
    mouth.run(cap)
#
#     # 使用 Dlib 的正面人脸检测器 frontal_face_detector
#     detector = dlib.get_frontal_face_detector()
#
#     # 脸部关键点预测器
#     predictor = dlib.shape_predictor("./data/dlib/shape_predictor_68_face_landmarks.dat")
#
#     cap = cv2.VideoCapture(0)  # 这是选择打开自己的摄像头
#
#     fps = cap.get(cv2.CAP_PROP_FPS)  # 获取摄像头或者视频帧率
#     print(fps)
#     # count = int(cap.get(7))  # 总帧数
#     # print("总帧数",count)
#
#
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     # print(width,height)
#     # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # codec
#     # # cv2.VideoWriter( filename, fourcc, fps, frameSize )
#     # out = cv2.VideoWriter('C:/Users/一只会飞的猫/Desktop/test/output.mp4', fourcc, fps, (width, height))
#
#     # (mouth_lower, mouth_upper) = face_utils.FACIAL_LANDMARKS_68_IDXS['mouth']
#     (mouth_lower, mouth_upper) = (48, 60)
#
#     ACTIVATION_RATIO = 1.8
#
#     color = (0, 0, 255)
#     actived = False
#     result = []
#     sum = 0
#     j = 0
#     fras = 0
#
#     while (True):
#
#         # if (fras >= count):
#         #     break
#
#         ret, frame = cap.read()
#         # 使用 detector 检测器来检测图像中的人脸
#         faces = detector(frame, 1)
#
#         if (len(faces) > 0):
#             # 判断每6帧的张开嘴巴的次数大于2次，判断为在说话，可以自己修改
#             if fras > 6 and len(result) > 6:
#                 for i in range(j, j + 6):
#                     sum = sum + result[i]
#                 # print(sum)
#                 if sum > 2:
#                     # print("talking")
#                     actived = True
#                 else:
#                     actived = False
#                 sum = 0
#                 j = j + 1
#             for (i, face) in enumerate(faces):
#                 # color = (0, 0, 255)
#                 # print("人脸位置：",face,"当前帧：",current_frame,"颜色为：",color)
#                 # print("人脸数 / faces in all：", len(faces))
#                 # print(face) [(161, 76) (546, 461)]
#                 # fx, fy, fw, fh=face
#                 fx = face.left()
#                 fy = face.top()
#
#                 # 确定面部区域的面部地标，然后将面部标志（x，y）坐标转换成NumPy阵列
#                 # 使用predictor来计算面部轮廓
#                 shape = predictor(frame, face)
#                 shape = face_utils.shape_to_np(shape)
#
#                 left = (shape[48, 0], shape[48, 1])
#                 right = (shape[54, 0], shape[54, 1])
#
#                 top = (shape[51, 0], shape[51, 1])
#                 bottom = (shape[57, 0], shape[57, 1])
#
#                 diff_h = euclidian_distance(top, bottom)
#                 diff_w = euclidian_distance(left, right)
#
#                 ratio = round(diff_w / diff_h, 5)
#
#                 cv2.line(frame, left, right, color)
#                 cv2.line(frame, top, bottom, color)
#
#                 cv2.putText(frame, "ratio: %s" % ratio, (0, height - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color)
#                 # 绘制嘴巴的点
#                 for (x, y) in shape[mouth_lower:mouth_upper]:
#                     cv2.circle(frame, (x, y), 1, color, -3)
#
#                 if actived:
#                     cv2.putText(frame, "talking", (fx + 20, fy - 30), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0), 1)
#
#                 if ratio >= ACTIVATION_RATIO:  # mouth shut & not talking
#                     # print("闭着嘴巴")
#                     result.append(0)
#                     # color = (0, 0, 255)  # red
#                     cv2.putText(frame, "shut ", (fx + 20, fy + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#                 else:
#                     # print("张开嘴巴")
#                     result.append(1)
#                     # color = (0, 255, 0)  # green
#                     # cv2.putText(frame, "open", (fx+20, fy+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#
#         else:
#             cv2.putText(frame, "no face", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
#
#         fras = fras + 1
#         print("当前帧", fras)
#         # 显示图像
#         cv2.imshow('frame', frame)
#         # 写入视频
#         # out.write(frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # When everything done, release the capture
#     cap.release()
#     cv2.destroyAllWindows()
