from django.shortcuts import render,redirect
from mysqlcrud1app.forms import UserForm,User
from django.http import HttpResponse


# Create your views here.
def insert(request):
    if request.method == 'POST':

        fm=UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("<h2>Data inserted in Database</h2>")
    else:
        fm=UserForm()
        return render(request,'index.html',{'form':fm})

def show(request):
    users=User.objects.all()
    return render(request ,'show.html',{'users':users})

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    user=User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})

def update(request,id):
    user=User.objects.get(id=id)
    fm=UserForm(request.POST,instance=user)
    if fm.is_valid():
        fm.save()
        return redirect('/show')
    return render(request,'edit.html',{'form':fm})