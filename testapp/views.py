from django.shortcuts import render
from testapp.forms import ItemAddForm

# Create your views here.
def index(request):
    return render(request,'testapp/home.html')
def additem(request):
    form=ItemAddForm()
    response=render(request,'testapp/additem.html',{'form':form})
    if request.method=='POST':
        form=ItemAddForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['itemname']
            quantity=form.cleaned_data['quantity']
            response.set_cookie(name,quantity,180)
            # return index(request)
    return response

def displayitem_view(request):
    return render(request,'testapp/showitems.html')
