from django.shortcuts import render

# Create your views here.


def entropy(request):
    return render(request, 'calculator/upload_csv.html')