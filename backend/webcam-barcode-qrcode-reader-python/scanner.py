import numpy as np
import cv2 as cv
import webbrowser
from multiprocessing.pool import ThreadPool
from collections import deque

import dbr
from dbr import *

import time

BarcodeReader.init_license("t0072oQAAAFlX29FNDgj6lDhXo9QR+59CQ5LXgKRGI3pGZZr5bnXiZB+nAL0Axli7E4OSsRHC6Pgh2OjQuLPZ7bIHArYzNgjTdSJC")
reader = BarcodeReader()

def process_frame(frame):
    results = None
    try:
        results = reader.decode_buffer(frame)
    except BarcodeReaderError as bre:
        print(bre)
    
    return results

def main():
    import sys
    try:
        fn = sys.argv[1]
    except:
        fn = 0
    cap = cv.VideoCapture(fn)

    threadn = 1 # cv.getNumberOfCPUs()
    pool = ThreadPool(processes = threadn)
    barcodeTasks = deque()

    while True:
        ret, frame = cap.read()
        while len(barcodeTasks) > 0 and barcodeTasks[0].ready():
            results = barcodeTasks.popleft().get()
            if results != None:
                for result in results:
                    points = result.localization_result.localization_points
                    cv.line(frame, points[0], points[1], (0,255,0), 2)
                    cv.line(frame, points[1], points[2], (0,255,0), 2)
                    cv.line(frame, points[2], points[3], (0,255,0), 2)
                    cv.line(frame, points[3], points[0], (0,255,0), 2)
                    a= cv.putText(frame, result.barcode_text, points[0], cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
                    print(result.barcode_text)
        if len(barcodeTasks) < threadn:
            task = pool.apply_async(process_frame, (frame.copy()))
            barcodeTasks.append(task)

        cv.imshow('Barcode & QR Code Scanner', frame)

        webbrowser.open(result.barcode_text)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    print('Done')


if __name__ == '__main__':
    main()
    cv.destroyAllWindows()
    