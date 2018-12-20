import Objek
import cv2
import Setting as Set


camera = cv2.VideoCapture(0)
bola = Objek.Objek(camera, Set.color_lower, Set.color_upper)

while 1:
    bola.tracking()
    print(bola.getpwm(), ", ", bola.getjarak())
    cv2.imshow("Camera", bola.getcamera())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
