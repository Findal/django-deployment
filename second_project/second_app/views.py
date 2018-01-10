from django.shortcuts import render
from second_app.forms import RegisterInterest


def index(request):
    return render(request, "second_app/index.html")


def users(request):
    form = RegisterInterest()

    if request.method == "POST":
        form = RegisterInterest(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form is invalid")
    return render(request, 'second_app/users.html',{'form':form})


def help(request):
    my_dict = {'page_content': "Hello I am from the second app"}
    return render(request, 'second_app/help.html', context=my_dict)

# Create your views here.

