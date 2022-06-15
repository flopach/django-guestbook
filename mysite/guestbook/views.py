from django.shortcuts import render,redirect
from django.http import HttpResponse

#from .forms import EntryForm
#from .models import guestentry

# Create your views here.



"""
def index(request):
    entries = guestentry.objects.all()
    context = {'entries' : entries}

    return render(request, 'guestbook/index.html',context=context)



def addentry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)


        if form.is_valid():
            new_entry = guestentry(entry_text=request.POST["entry_text"])
            new_entry.save()
            return redirect('index')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'guestbook/addentry.html',context=context)
"""