from django.core.paginator import Paginator
from django.shortcuts import render
from .models import UserAnswer
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
from apps.opencvdjango.models import UserEntry


def index(request):
    context = {}
    filtered_quiz = UserEntry.objects.all()
    paginator = Paginator(filtered_quiz, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['object_list'] = page_obj
    return render(request, "index.html", context)


def quiz(request):
    return render(request, "quiz.html")

#
# def webcam_feed(request):
#     return StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')
#
#
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
#         self.videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640, 480), True)
#         queryset=UserEntry.objects.all()
#         for instance in queryset:
#             self.hrs = instance.video_time
#             self.mins = instance.video_sec
#         print("database oku",self.hrs)
#         print("database oku",self.mins)
#         print("database oku",self.mins)
#         self.totalsecs = 3600 * self.hrs + 30 * self.mins
#
#     def __del__(self):
#             self.video.release()
#
#     def get_frame(self):
#         success, image = self.video.read()
#         self.videoWriter.write(image)
#
#         ret, jpeg = cv2.imencode('.jpg', image)
#
#         self.totalsecs -= 1
#         if self.totalsecs == 0:
#             print("video time over")
#             self.videoWriter.release()
#             return jpeg.tobytes()
#
#         return jpeg.tobytes()
# def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
#
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def upload_file(request):
    file = request.FILES.get('file')
    fss=FileSystemStorage()
    filename=fss.save(file.name,file)
    url=fss.url(filename)
    print ("******************")
    print (fss)
    print(file.name)
    print(url)
    print(file)
    print(filename)
    print("******************")
    UserAnswer.objects.create(header="test",doc=file)
    

    return JsonResponse({"url":url})

  	