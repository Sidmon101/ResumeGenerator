from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict={"name":"Sidharth"}
    return render(request,'templatesApp/firstTemplate.html',context=myDict )
def renderEmployee(request):
    myDict={"id":1,"name":"Sidharth","salary":70000}
    return render(request,'templatesApp/employeeTemplate.html',myDict)