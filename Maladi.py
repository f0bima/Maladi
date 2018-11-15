import cv2
import numpy as np
import math
import fungsi
import Setting as Set
import PID
import serial


x=1
ser = serial.Serial('COM4', 9600)

target = 0
KP = 2
KI = 0
KD = 0
pid = PID.PID(KP, KI, KD)
pid.SetPoint = target
pid.setSampleTime(0)

xtengah = 320
ytengah = 480
camera = cv2.VideoCapture(0)

while(True):
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.bilateralFilter(hsv, 5, 175, 175)

    '''colorbola_lower = np.array(Set.color_lower, np.uint8)
    colorbola_upper = np.array(Set.color_upper, np.uint8)'''

    color_mask = cv2.inRange(hsv, Set.color_lower, Set.color_upper)

    erode = cv2.erode(color_mask, None, iterations=2)
    dilate = cv2.dilate(erode, None, iterations=10)
    
    kernelopen = np.ones((5, 5))
    kernelclose = np.ones((20, 20))

    maskopen = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernelopen)
    maskclose = cv2.morphologyEx(maskopen, cv2.MORPH_CLOSE, kernelclose)

    _, contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnts in contours:
        area = cv2.contourArea(cnts)

        if area > 5000:
            ((x, y), radius) = cv2.minEnclosingCircle(cnts)

            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 140, 255), 2)
            # panjanggaris = math.pow(math.pow(180 - int(x), 2) + math.pow(150 - int(y), 2), 1 / 2.0)
            panjang_x = math.pow(math.pow(xtengah - int(x), 2) + math.pow(ytengah - ytengah, 2), 1 / 2.0)
            panjang_y = math.pow(math.pow(xtengah - xtengah, 2) + math.pow(ytengah - int(y), 2), 1 / 2.0)

            if (int(y)) <= ytengah:
                if (int(x)) >= xtengah:
                    posisi = fungsi.sudut(panjang_x, panjang_y)
                else:
                    posisi = 0 - fungsi.sudut(panjang_x, panjang_y)
            else:
                if (int(x)) >= xtengah:
                    posisi = 180 - (fungsi.sudut(panjang_x, panjang_y))
                else:
                    posisi = 0 - 180 + (fungsi.sudut(panjang_x, panjang_y))

            '''cv2.putText(frame, "BOLA " + str(int(x)) + "," + str(int(y)),
                        (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 140, 255, 2), 2)'''
            cv2.putText(frame, "OBJ 1 " + str(posisi),
                        (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0, 2), 2)
            '''cv2.putText(frame, "OBJ 1 " + str(panjang_y),
                        (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 140, 255, 2), 2)'''

            # draw a red line
            cv2.line(frame, (xtengah, ytengah), (int(x), int(y)), (255, 0, 0), 4)

            pid.update(posisi)
            targetPwm = round(pid.output,3)
            ser.write((str(targetPwm)).encode())
            print(targetPwm)


            # print(int(x - radius), int(y - radius), area)

    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
