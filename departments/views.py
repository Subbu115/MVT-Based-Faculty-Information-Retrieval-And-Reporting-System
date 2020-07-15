from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from departments.forms import DepartmentForm
from django.http.response import HttpResponseRedirect



# Create your views here.
from departments.models import Department


def insert_dept(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            return HttpResponseRedirect('/departments')
    if request.method == 'GET':
        return render(request, 'insertdept.html')
