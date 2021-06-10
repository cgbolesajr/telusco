from django.shortcuts import render

# Create your views here.
def home(request):

    context = {'name': 'maw'}
    return render(request, 'calc/home2.html', context)


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = val1 + val2
    context = {'result': res}
    return render(request, 'calc/result.html', context)
