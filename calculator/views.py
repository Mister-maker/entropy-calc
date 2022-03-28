from django.shortcuts import redirect, render, redirect
from django.conf import settings
from math import log2, pow
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


sum=0

def probabilty(string, windowsize, q):
    global sum
    n= len(string)
    count_1=0
    count_0=0
    for i in range(n):
        if string[i]=='1':
            count_1+=1
        else:
            count_0+=1

    prob_0= pow(count_0/windowsize, q)
    prob_1= pow(count_1/windowsize, q)
    prob_0_1 = prob_0+ prob_1
    s= (1/(q-1))*(1-prob_0_1)
    sum+=s
    return s


def home(request):
    # create object of forms
    form = EntropyCalcForm(request.POST or None, request.FILES or None)
    obj_public = None

    if form.is_valid():
        # save the form data to model
        obj = form.save(commit=False)
        obj.save()

        if (obj.calculate == 'shannon'):
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
        else:
            # reading content of file
            with open(obj.csv_file.path) as f:
                # print(f.read())
                string= f.read()


            # taking input of window size  
            n= len(string)
            countentropy=0
            # w= int(input("Enter the window size: "))
            w= n-99
            size=w
            power= 2
            for i in range(n):
                if i+w>n:
                    break
                countentropy+=1
            count=0
            with open(obj.csv_file.path, 'w') as wr:
                for j in range(2, 5):
                    wr.write(f"Entropy with q = {j}\n")
                    for i in range(countentropy):
                        wr.write(str(probabilty(string[i:w], size, j))+"\n")
                    wr.write(f'The average is {sum/countentropy}\n\n')

        obj_public = obj

    context = {
        'form': form,
        'object': obj_public
    }

    return render(request, 'calculator/index.html', context)


def entropy(request):
    entropy_obj = EntropyCalc.objects.all()

    context = {
        'entropy_obj': entropy_obj
    }

    return render(request, 'calculator/result_csv.html', context)
   