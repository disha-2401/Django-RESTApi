import io

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import StudentSerialiser
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerialiser(stu)
            # JsonRender = JSONRenderer().render(serializer.data)
            # return HttpResponse(JsonRender, content_type='application/json')
            return JsonResponse(serializer.data, safe=False)
        stu = Student.objects.all()
        serializer = StudentSerialiser(stu, many=True)
        # JsonRender = JSONRenderer().render(serializer.data)
        # return HttpResponse(JsonRender, content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerialiser(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'object created'}
        #     json_data = JSONRenderer().render(res)
        #     return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)
    elif request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerialiser(stu, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'object updated'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)
    elif request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'object deleted'}
        json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)