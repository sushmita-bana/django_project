from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import response
from .models import registered_people,joining_people


# Create your views here.
def main_page(request):
    return render(request,'main_page.html')

def register_page(request):

    if request.method =="POST":
        registered_people.objects.create(Name=request.POST['name'],Mobile=request.POST['mobile'],Email= request.POST['email'],Course=request.POST['course'],Source=request.POST['source'],LeadStatus=request.POST['lead'],DemoDate=request.POST['date'],Counsler=request.POST['counsler'],Remarks=request.POST['remarks'])
        return redirect('home')
        #return render(request,'walkin.html')
    else:    
        return render(request,'register.html')

def walkins_page(request):
    all_data=registered_people.objects.all
    print(all_data)
    return render(request,'walkin.html',{'data':all_data})

def calling_page(request):
    if request.method=="POST":
        status=request.POST['lead']
        date=request.POST['date']
        filter_data=registered_people.objects.filter(LeadStatus=status,DemoDate=date)
        
        return render(request,"calling_list.html",{'data':filter_data})

    else:
        return render(request,"calling_page.html")

def calling_list(request):
    
    
    return render(request,'calling_list.html')

def counselling(request):
    if request.method=="POST":
        date=request.POST['date']
        course=request.POST['course']
        coun_data=registered_people.objects.filter(DemoDate=date,Course=course)

        return render (request,'counselling_list.html',{'data':coun_data})
    else:
        return render(request,"counselling.html")

def joining(request):
    
    if request.method =="POST":
        joining_people.objects.create(Name=request.POST['name'],Course=request.POST['course'],DateOfJoining=request.POST['date_join'],DateOfCompletion=request.POST['date_complete'],Instructor=request.POST['instructor'],Mobile=request.POST['mobile'],Email= request.POST['email'],Remarks=request.POST['remarks'])
        return redirect('current_students')
        #return render(request,'walkin.html')
    else:    
        return render(request,'joining.html')
    

def update(request):
    
    if request.method=="POST":
        name=request.POST['name']
        date=request.POST['willing_date']
        registered_people.objects.filter(Name=name).update(DemoDate=date)
        return redirect ('walkin')
    else:
        return render (request,'update.html')

def delete(request,id):
    registered_people.objects.get(id=id).delete()
    print(id)
    

    return redirect('walkin')

def current_students(request):
    all_data=joining_people.objects.all
    
    return render(request,'current_students.html',{'data':all_data})

def current_student_update(request):

    if request.method=="POST":
        name=request.POST['name']
        completion_date=request.POST['date_complete']
        joining_people.objects.filter(Name=name).update(DateOfCompletion=completion_date)
        return redirect ("current_students")
    else:
        return render (request,'current_student_update.html')

def students(request,id):
    
    all_data=joining_people.objects.get(id=id)
    return render(request,'students.html',{'data':all_data})






        





  