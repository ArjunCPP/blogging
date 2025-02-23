from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
# Create your views here.
def register(request):
   
    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
           
            username= form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}!')
            return redirect('blog-home')   
        else:
            messages.warning(request,f'invalid credentials')       
    else:
        form =UserCreationForm()

    return render(request,'users/register.html',{'form':form})