from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

# import models
from django.contrib.auth.models import User
from app1.models import Mobile,Todo

# import decorators
from django.contrib.auth.decorators import login_required

# import masseges
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('todo')
        else:
            messages.info(request,'username,password is not matching')
            return redirect('signin')
    return render(request,'signin.html')

def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirmpassowrd = request.POST['confirmpassword']
        users = User.objects.all()
        for user in users:
            temp = str(user)
            if username == temp:
                messages.info(request,'user :'+ username +' is already exist')
                return redirect('signup')
        if password == confirmpassowrd:
            person = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
            Mobile.objects.create(mobile=mobile,uid_id=person.id)
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request,'signup.html')

@login_required(login_url='signin')
def todo(request):
    data = Todo.objects.filter(uid_id=request.user.id)
    if request.method == 'POST':
        todo_item = request.POST['todoitem']
        due = request.POST['due']
        current_user_id = request.user.id
        Todo.objects.create(todo_items=todo_item,due=due,uid_id=current_user_id)
        data = Todo.objects.filter(uid_id=current_user_id)
        return render(request,'todolist.html',{'data':data})
    return render(request,'todolist.html',{'data':data})

@login_required(login_url='signin')
def edit(request,id):
    if request.method == "POST":
        todo_item = request.POST['todoitem']
        due = request.POST['due']
        if todo_item and due:
            Todo.objects.filter(id=id).update(todo_items=todo_item,due=due)
            return redirect('todo')
        if todo_item:
            Todo.objects.filter(id=id).update(todo_items=todo_item)
            return redirect('todo')
        if due:
            Todo.objects.filter(id=id).update(due=due)
            return redirect('todo')
    return render(request,'edit.html')
@login_required(login_url='signin')
def delete(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('todo')
@login_required(login_url='signin')
def finished(request,id):
    Todo.objects.filter(id=id).update(status='finished')
    return redirect('todo')
@login_required(login_url='signin')
def finished_data(request):
    data = Todo.objects.filter(uid_id=request.user.id)
    return render(request,'finished.html',{'data':data})

@login_required(login_url='signin')
def finishedDelete(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('finished_data')

def signout(request):
    logout(request)
    return redirect('signin')