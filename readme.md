# Create your first Django Guestbook

## Django Create Project

```
django-admin startproject mysite
cd mysite
python manage.py startapp guestbook
```

**Projects vs. apps**

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


## Django Create simple Page

1. Create View in app/views.py:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

2. Add URL in app/urls.py

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

## Django connect App in project

1. Include App URLs in project URLs in project/urls.py

```
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

2. Add App from app/apps.py in project/settings.py

```
INSTALLED_APPS = [
    'challenge.apps.ChallengeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Now:

```
python manage.py makemigrations challenge
python manage.py migrate
```

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. 

3. Create Superuser:

```
python manage.py createsuperuser --username=admin --email=admin
```

## Django Templates

Create folders for page templates: `guestbook/templates/guestbook/

index.html

```
<html>
  <head>
    <title>Guest Book</title>
  </head>

  <body>

    <h1>Guestbook</h1>
    <p><a href="">Add entry</a></p>

    

  </body>
</html>
```

addentry.html

```
<html>
  <head>
    <title>Guest Book</title>
  </head>

  <body>

    <h1>Guestbook</h1>

    

  </body>
</html>
```

Create new views:

```
def index(request):
    return render(request, 'guestbook/index.html')

def addentry(request):
    return render(request, 'guestbook/addentry.html')
```

Add according URL in urls.py:

```
path('addentry', views.addentry,name="addentry"),
```

## Django Create Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. 

```
class guestentry(models.Model):
    entry_text = models.CharField(max_length=200)
    entry_date = models.DateTimeField('date published')
```

Then make the model modifiable in the admin interface:

```
from .models import guestentry

# Register your models here.
admin.site.register(guestentry)
```

```
makemigrations guestbook
migrate
```

## Create a Form

Create forms.py in app folder

```
from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea())
```

## Add Entry: Bring everything together

views.py

```
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
```

addentry.html

```
<form method="POST" action="{% url 'addentry' %}">
      {% csrf_token %}
      {{ form.as_p }}              
      <button type="submit">Add Entry</button>
</form>
```

## View Entries: Bring everything together

views.py

```
def index(request):
    entries = guestentry.objects.all()
    context = {'entries' : entries}

    return render(request, 'guestbook/index.html',context=context)
```



addentry.html

```
<form method="POST" action="{% url 'addentry' %}">
      {% csrf_token %}
      {{ form.as_p }}              
      <button type="submit">Add Entry</button>
    </form>
```


**Done**!