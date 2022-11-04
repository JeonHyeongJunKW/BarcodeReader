
import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
qrDecoder = cv2.QRCodeDetector()
start_time = time.time()
sum_time =0
sum_count =0

while True:
    ref, frame = cap.read()

    cv2.imshow("QR extractor",frame)
    extract_start_time = time.time()
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(frame)
    current_time = time.time()
    c_time = (current_time - extract_start_time)
    sum_time += c_time
    sum_count +=1
    if len(data)>0:
        print("\r time : {:.2f} (s), mean extraction time : {:.3f} (s), QR code Data : {}".format(current_time-start_time, sum_time/sum_count, data),end=' ')
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()