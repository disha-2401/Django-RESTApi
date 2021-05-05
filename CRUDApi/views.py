import io

from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# old method not model based function
@csrf_exempt
def student_api(request):
    # when user wants to get info of specific student or all student
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            # JsonRender = JSONRenderer().render(serializer.data)
            # return HttpResponse(JsonRender, content_type='application/json')
            return JsonResponse(serializer.data, safe=False)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # JsonRender = JSONRenderer().render(serializer.data)
        # return HttpResponse(JsonRender, content_type='application/json')
        return JsonResponse(serializer.data, safe=False)
    # when user wnats to add student in database
    elif request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'object created'}
            #     json_data = JSONRenderer().render(res)
            #     return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)
    # when user wants to update student info in database
    elif request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'object updated'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)
    # when user wants to delete a student object based on id
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


# class based view Model serializer
@method_decorator(csrf_exempt, name='dispatch')
class ModelBased(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            # JsonRender = JSONRenderer().render(serializer.data)
            # return HttpResponse(JsonRender, content_type='application/json')
            return JsonResponse(serializer.data, safe=False)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # JsonRender = JSONRenderer().render(serializer.data)
        # return HttpResponse(JsonRender, content_type='application/json')
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        print("post called")
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'object created'}
            #     json_data = JSONRenderer().render(res)
            #     return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'object updated'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors, safe=False)

    def delete(self, request, *args, **kwargs):
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