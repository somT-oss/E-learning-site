from django.shortcuts import render
from django.contrib import messages 
from .form import UserRegistrationForm

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.method)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f"Account has been successfully created for {username}!")
            form.save()
            return redirect('courses/home')
    else:
        form = UserRegistrationForm()

    context = {
        "register_form": form,
    }

    return render(request, 'register.html', context)


# Create your views here.
