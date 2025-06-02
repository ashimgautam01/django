
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student,Department
from .serializers import StudentSerializer,DepartmentSerializer

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)











@api_view(['POST','GET'])
def department(request):
    if request.method=='GET':
        depart=Department.objects.all()
        serializer=DepartmentSerializer(depart,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        add_depart=DepartmentSerializer(data=request.data)
        if add_depart.is_valid():
            add_depart.save()
            return Response(add_depart.data,status=200)
        return Response(add_depart.data,status=400)
        
