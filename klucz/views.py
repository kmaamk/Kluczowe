from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm
from django.apps import apps
from .models import Question
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def get_queryset(self):
    return Question.question_objects.order_by("choice_text")

@login_required
def wybierz_kluczowe(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('klucz/potwierdzenie.html')

    else:
        form = QuestionForm()
    return render(request, 'klucz/kluczowe_my.html', {'form': form})


def potwierdzenie(request):
    return render(request, 'klucz/potwierdzenie.html')



def login_view(request):
    context = {}
    next=request.GET.get('next', '/error/')
      # render wypełnia http response contextem i dlatego jest szersza od http response
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user == None:
            return render(request, 'login2.html', {'redirect to': next})#render(request, 'login_error.html', context)
        else:
            login(request, user)
            return redirect('klucz/kluczowe_my.html')
    else:
        return render(request, 'login2.html', context)



def login_error(request):
    context = {}
    if not request.POST:
        return render(request, 'login2.html', context)  # render wypełnia http response contextem i dlatego jest szersza od http response
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user == None:
            return render(request, 'login_error.html', context)
        else:
            login(request, user)
            return redirect('klucz/kluczowe_my.html')



#metoda opisująca eksport csv - problem z wyciągnięciem wiersza dla aktualnego oddziału
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response



    #form = QuestionForm()
    #return render(request, 'klucz/wybierz_kluczowe.html', {'form': form})