import pandas as pd
from .forms import ExcelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .excel_to_db import count, result_name
from .serizalizers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

def add_excel_file(request):
    if request.method == 'POST':
        excel_form = ExcelForm(request.POST, files=request.FILES)
        if excel_form.is_valid():
            trophy = excel_form.save(commit=False)
            trophy.save()
            messages.success(request, 'Файл добавлен')
            #return redirect('admin')
        else:
            messages.error(request, 'Введен неверный формат данных')
    else:
        excel_form = ExcelForm()
    return render(request,
                      'add_excel_file.html',
                      {'excel_form': excel_form,
                       })

@api_view(['GET'])
def home(request):
    client_obj = Client.objects.all()
    serializer = ClientSerializer(client_obj,many=True)
    return Response({'status':200, 'payload':serializer.data})


@api_view(['GET'])
def client_summary(request):
    return Response({'status': 200, 'summary': count})


@api_view(['GET'])
def clients_list(request):
    return Response({'status': 200, 'client': result_name})