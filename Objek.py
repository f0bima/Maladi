import cv2
import math
import fungsi
import PID

xtengah = 320
ytengah = 480
target = 0
KP = 0.5
KI = 0
KD = 0
pid = PID.PID(KP, KI, KD)
pid.SetPoint = target
pid.setSampleTime(0)


class Objek:
    def __init__(self, src, lower, upper):
        self.image = src
        self.hsv_upper = upper
        self.hsv_lower = lower
        self.frame = None
        self.jarak = 0
        self.targetpwm = 0

    def tracking(self):
        ret, self.frame = self.image.read()
        self.frame = cv2.flip(self.frame, 1)
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.bilateralFilter(hsv, 5, 175, 175)
        color_mask = cv2.inRange(hsv, self.hsv_lower, self.hsv_upper)
        self.jarak = 0
        self.targetpwm = 0
        '''erode = cv2.erode(color_mask, None, iterations=2)
        dilate = cv2.dilate(erode, None, iterations=10)

        kernelopen = np.ones((5, 5))
        kernelclose = np.ones((20, 20))

        maskopen = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernelopen)
        maskclose = cv2.morphologyEx(maskopen, cv2.MORPH_CLOSE, kernelclose)'''

        _, contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnts in contours:
            area = cv2.contourArea(cnts)

            if area > 5000:
                ((x, y), radius) = cv2.minEnclosingCircle(cnts)

                cv2.circle(self.frame, (int(x), int(y)), int(radius), (0, 140, 255), 2)
                self.jarak = math.pow(math.pow(180 - int(x), 2) + math.pow(150 - int(y), 2), 1 / 2.0)
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

                cv2.putText(self.frame, "OBJ 1 " + str(posisi),
                            (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0, 2), 2)

                # draw a red line
                cv2.line(self.frame, (xtengah, ytengah), (int(x), int(y)), (255, 0, 0), 4)

                pid.update(posisi)
                self.targetpwm = round(pid.output, 3)

        # return targetpwm, jarak

    def getcamera(self):
        return self.frame

    def getjarak(self):
        return self.jarak

    def getpwm(self):
        return self.targetpwm
