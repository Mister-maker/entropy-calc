from django.shortcuts import redirect, render, redirect
from math import log2

# Create your views here.

from .models import EntropyCalc
from .forms import EntropyCalcForm


def entropy(string,size):
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
        form.save()

        return redirect('entropy')

    context = {
        'form': form
    }

    return render(request, 'calculator/index.html', context)


def entropy(request):
    entropy = EntropyCalc.objects.all()

    for item in entropy:
        print(item.csv_file.path)

        with open(item.csv_file.path) as f:
            print(f.read)
            string= f.read()

    # n= len(string)
    # countentropy=0
    # # w= int(input("Enter the window size: "))
    # w= n-99
    # size=w
    # for i in range(n):
    #     if i+w>n:
    #         break
    #     countentropy+=1
    # count=0
    # with open("output.csv", 'w') as wr:
    #     for i in range(countentropy):
    #         wr.write(str(entropy(string[i:w], size))+"\n")
    #         w+=1

    return render(request, 'calculator/upload_csv.html')
   