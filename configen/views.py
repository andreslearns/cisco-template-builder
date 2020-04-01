from django.shortcuts import render

def index(request):
    return render(request, 'configen/index.html' )

def dhcp(request):
    return render(request, 'configen/dhcp.html' )


def addip(request):
    return render(request, 'configen/addip.html' )
