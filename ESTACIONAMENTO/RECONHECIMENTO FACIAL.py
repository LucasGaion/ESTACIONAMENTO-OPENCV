import cv2
import mediapipe as mp
from numpy import imag, true_divide



#Inicializar opencv e o media pip
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils
rosto_conhecidos = []
nomes_dos_rostos = []


    


while True:
    #Ler as informações da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break

    #Reconhecer os rostos que alim dentro
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #desenhar no rosto na imagem
            desenho.draw_detection(frame, rosto)
    cv2.imshow("Rostos na Webcam", frame)

    



    #Quando apertar ESC, para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()