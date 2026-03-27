
from django.shortcuts import render
# from .models import *
# from django.core.mail import EmailMessage
# from django.views.decorators import gzip
# from django.http import StreamingHttpResponse
# import cv2
# import threading
# import pyaudio

# @gzip.gzip_page
# def index(request):
#     # try:
#     #     # cam = VideoCamera()
#     #     audio = Audio()
#     #     return StreamingHttpResponse(create(audio), content_type="multipart/x-mixed-replace;boundary=frame")
#     # except:
#     #     pass
#     return render(request, 'live.html')


# # # class VideoCamera(object):
# # #     def __init__(self):
# # #         self.video = cv2.VideoCapture(0)
# # #         (self.grabbed, self.frame) = self.video.read()
# # #         threading.Thread(target=self.update, args=()).start()

# # #     def __del__(self):
# # #         self.video.release()

# # #     def get_frame(self):
# # #         image = self.frame
# # #         _, jpeg = cv2.imencode('.jpeg', image)
# # #         return jpeg.tobytes()

# # #     def update(self):
# # #         while True:
# # #             (self.grabbed, self.frame) = self.video.read()

# # class Audio(object):
# #     def __init__(self):
# #         self.FORMATIN = pyaudio.paInt16
# #         self.CHANNELS = 2
# #         self.RATE = 44100
# #         self.CHUNK = 1024  
# #         self.FORMATOUT = pyaudio.paFloat32 
# #         audio = pyaudio.PyAudio()

# #         self.stream = audio.open(format=self.FORMATIN, channels=self.CHANNELS,
# #                         rate=self.RATE, input=True, input_device_index=0,
# #                         frames_per_buffer=self.CHUNK)

# #         self.streamOut = audio.open(format=self.FORMATOUT, channels=self.CHANNELS,
# #                        rate=self.RATE, output=True, input_device_index=0,
# #                        frames_per_buffer=self.CHUNK)
                       
# #     def get_frame(self):
# #         sound = self.stream.read(self.CHUNK)
# #         print(sound)
# #         return sound

# # # def gen(camera):
# # #     while True:
# # #         frame = camera.get_frame()
# # #         yield (b'--frame\r\n'
# # #                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# # def create(mic):
# #     while True:
# #         soundframe = mic.get_frame()
# #         mic.streamin.write(soundframe)



#  start live now 

def index(request):
    
    return render(request, "index.html")

