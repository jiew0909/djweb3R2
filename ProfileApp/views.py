from django.shortcuts import render,HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("<H1>Helloworld,This is My First Djange web </H1>"
                        "<H2> i love python</H2>")
def firstPage(request):
    return render(request,'FirsetPage.html')

def Secondpage(request):
    return render(request,'Secondpage.html')

def thirdpahe(request):
    return render(request,'thirdpahe.html')

def hnypage(request):
    return  render(request, 'hnypage.html')

def home (request):
    return render(request, 'home.html')

def testbt(request):
    return  render(request,'testbt.html')