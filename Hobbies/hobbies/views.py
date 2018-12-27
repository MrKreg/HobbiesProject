from django.shortcuts import render, redirect

def who_am_i(request):
    return render(request,'index.html')

def about_me(request):
    return render(request,'about.html')

def contact_me(request):
    return render(request,'contacts.html')

def view_404(request, exception):
    return redirect('/')