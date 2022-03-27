from django.shortcuts import redirect, render, redirect
from django.conf import settings
from math import log2
import os
from os.path import abspath

# Create your views here.

from .models import EntropyCalc
from .forms import EntropyCalcForm


def entropy_read(string,size):
    n= len(string)
    count=0
    for i in range(n):
        if string[i]=='1':
            count+=1

    return abs(-(count/size)*(log2(count/size)))


def home(request):
    # create object of forms
    form = EntropyCalcForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # save the form data to model
        obj = form.save(commit=False)
        obj.save()

        print("this is your file in form", obj.csv_file)


        with open(obj.csv_file.path) as f:
            print(f.read)
            string= f.read()

        n = len(string)
        countentropy=0
        w = n-99
        size=w
        for i in range(n):
            if i+w>n:
                break
            countentropy+=1
        count=0

        with open(obj.csv_file.path, 'w') as wr:
            for i in range(countentropy):
                wr.write(str(entropy_read(string[i:w], size))+"\n")
                w+=1
        
        obj.url = abspath(wr.name)
        obj.save()

        # print("This is wr", abspath(wr.name))

        return redirect('entropy')

    context = {
        'form': form
    }

    return render(request, 'calculator/index.html', context)


def entropy(request):
    entropy_obj = EntropyCalc.objects.all()
    
    context = {
        'entropy_obj': entropy_obj
    }

    return render(request, 'calculator/result_csv.html', context)
   