from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.shortcuts import redirect
from django.views.decorators import gzip
from requests import request
from reconocimiento import camara
from reconocimiento.camara import FaceDetect
import cv2
import threading
import imutils
import os
from unipath import Path

# @gzip.gzip_page
def vista_camara(request):
    try:

        carpeta = Path('.', 'face_detection_model\prueba')
        if carpeta.isdir():
            print("el directorio existe")
        else:
            carpeta.mkdir()
            print("el directorio se acaba de crear satisfactoriamente")
        print(carpeta)

        VideoCamara().__init__(request)

        # print("############################################################################")
        # print("Usted esta siendo grabado............")
        # print("############################################################################")


        # return StreamingHttpResponse(request, 'reconocimiento/reconocimiento.html')
        # return StreamingHttpResponse(gen(VideoCamara()), content_type='multipart/x-mixed-replace; boundary=frame')
        # return render(request, 'reconocimiento/reconocimiento.html')
        # return render(request, 'home.html')
    except:
        pass
    # return render(request, 'reconocimiento/reconocimiento.html')
    # return render(request, 'home.html')
    return render(request, 'reconocimiento/reconocimiento.html')

def vista_finalizar_reconocimiento(request):
    return render(request, "inventario/catalogo.html")

class VideoCamara(object):
    def __init__(self):
        ##################################Configuracion de camara
        # self.usuario = usuario
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()
        print("Toma de fotografias terminado")
        # vista_finalizar_reconocimiento(self.usuario)
    
    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        ###############################Creacion carpeta con nombre de usuario
        personName = 'prueba'
        dataPath='C:/Users/asana/Desktop/Data_openCV'
        personPath = dataPath + '/' + personName
        if not os.path.exists(personPath):
            print('Carpeta creada: ',personPath)
            os.makedirs(personPath)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        count = 0
        
        while True:
            (self.grabbed, self.frame) = self.video.read()

            ##########################Almacenamiento de fotos
            # print("############################################################################")
            # print("Foto tomada............")
            # print("############################################################################")
            ret, frame = self.video.read()
            if ret == False: break
            frame =  imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()

            faces = faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
                count = count + 1
            cv2.imshow('frame',frame)

            k =  cv2.waitKey(1)
            if k == 27 or count >= 300:
                # print("Toma de fotografias terminado")
                break
            

    
def gen(camara):
    while True:
        frame = camara.get_frame()
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')