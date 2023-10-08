import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('VideoLab\Video2.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))


sensores_activados = [False, False, False]
sensores_inversos = [False, False, False] 
contador_entrada = 0
contador_salida = 0
contador_sala = 0

linea1 = 60
linea2 = 100
linea3 = 140

altura =100

def verificacion(c):
    a=c-5
    b=c+5
    if a < (x+w) < b:
        cv2.line(frame, (c, frame.shape[0]-altura), (c, 120), (0, 0, 0), 4)
        return True
    else:
        return False



while True:
    ret, frame = cap.read()
    if ret == False: break

    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    
    frame = imutils.resize(frame, height=300)
    #-------------------------------------------
    area_pts = np.array([[10, 120], [10, frame.shape[0]-altura], [150, frame.shape[0]-altura], [150, 120]])
    #-------------------------------------------
    imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
    image_area = cv2.bitwise_and(frame, frame, mask=imAux) 
    #-------------------------------------------
    fgmask = fgbg.apply(image_area)
    _,fgmask = cv2.threshold(fgmask, 254, 255, cv2.THRESH_BINARY)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=2)
    #-------------------------------------------  
    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > 500 and area < 2500:
        #if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
            #-------------------------------------------
            sensor1 = verificacion(linea1)
            sensor2 = verificacion(linea2)
            sensor3 = verificacion(linea3)
            #-------------------------------------------
            if sensor1:
                if sensores_inversos[1] and sensores_inversos[2]:
                    sensores_inversos[0] = True
                    print('Reversa 3 activado')
                else:
                    sensores_activados[0] = True
                    print('Sensor 1 activado')
            #-------------------------------------------   
            if sensor2:
                if sensores_activados[0]:
                    sensores_activados[1] = True
                    print('Sensor 2 activado')
                elif sensores_inversos[2]:
                    sensores_inversos[1] = True
                    print('Reversa 2 activado')
            #-------------------------------------------
            if sensor3:
                if sensores_activados[0] and sensores_activados[1]:
                    sensores_activados[2] = True
                    print('Sensor 3 activado')
                else:
                    sensores_inversos[2] = True
                    print('Reversa 1 activado')
            #-------------------------------------------
            if sensores_activados == [True, True, True]:
                contador_entrada += 1
                print('Sensores Activos, procede a contar y borrar')
                sensores_activados = [False, False, False]
            elif sensores_inversos == [True, True, True]:
                contador_salida += 1
                print(f'CONTADOR SALIDA: {contador_salida}')
                sensores_inversos = [False, False, False]
            contador_sala = contador_entrada - contador_salida
    
    
    #-------------------------------------------  
    cv2.drawContours(frame, [area_pts], -1, (255, 0, 255), 2)    
    cv2.line(frame, (linea1, frame.shape[0]-altura), (linea1, 120), (255, 0, 255), 1)
    cv2.line(frame, (linea2, frame.shape[0]-altura), (linea2, 120), (255, 0, 255), 1)
    cv2.line(frame, (linea3, frame.shape[0]-altura), (linea3, 120), (255, 0, 255), 1)
    
    cv2.putText(frame, 'CONTADOR ENTRADA: ' + str(contador_entrada), (2, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, 'CONTADOR SALIDA:   ' + str(contador_salida), (2, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, 'CONTADOR SALON:   ' + str(contador_sala), (2, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)    
    cv2.imshow('frame',frame)
    cv2.imshow('fgmask',fgmask) 
    
    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()