import cv2
import numpy as np

HTTP = 'http://'
IP_ADDRESS = '192.168.248.177'
URL =  HTTP + IP_ADDRESS + ':4747/video'


def main():
    print("[ droidcam.py ] - Initializing...")
    cap = cv2.VideoCapture(URL)
    if cap.isOpened() is not True:
        print ('Not opened.')
        print ('Please ensure the following:')
        print ('1. DroidCam is not running in your browser.')
        print ('2. The IP address given is correct.')

    # Connection successful. Proceeding to display video stream.
    while cap.isOpened() is True:
        _, frame = cap.read()

        # # Turning your frames into grayscale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('frame',frame)
        # cv2.imshow('gray',gray)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
        #contornos, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame, contornos, -1, (0, 255, 0), 3)
        #cv2.imshow('th', th)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()