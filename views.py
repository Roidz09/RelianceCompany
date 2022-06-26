from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def login(request):
    context = {'login': Employee.objects.all()}
    return render(request, "employee_register/login.html", context)

def logout(request):
    context = {'logout': Employee.objects.all()}
    return render(request, "employee_register/logout.html", context)

def Login_form(request):
    context = {'Login_form': Employee.objects.all()}
    return render(request, "employee_register/Login_form.html", context)

def About(request):
    context = {'About': Employee.objects.all()}
    return render(request, "employee_register/About.html", context)

def home(request):
    context = {'home': Employee.objects.all()}
    return render(request, "employee_register/home.html", context)

def homepage(request):
    context = {'home2': Employee.objects.all()}
    return render(request, "employee_register/homepage.html", context)
    
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else: 
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html",{'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


