# Event Manager

Api built using djando a python framework at pycon18 and instructed by Mashood Rastogar.

Steps to get started...

1. Install Python 3.x
2. Install Pip
3. `pip install virtualenv` (to create a virtual env for using python)
4. `virtualenv -p python3 env`
5. `source ./env/bin/activate`
6. `python --version`
7. `pip install django`
8. `django-admin startproject eventmanager`
9. `pip freeze > requirements.txt`
10. `python manage.py runserver` (to start djando server not static assets)
11. `python manage.py startapp event` (to create a djando app)
12. `python manage.py migrate`
13. `python manage.py createsuperuser --email admin@admin.com --username admin`
14. Enter password and enter y when asked to bypass the security.
15. Goto settings.py and in INSTALLED_APPS list add this in the end 'event' (event is the name of the app from step 11)
16. Goto event/models.py and create you models
```
class Event(models.Model):
  title=models.CharField(max_length=30)
  description=models.CharField(max_length=30)
```
17. `python manage.py makemigrations && python manage.py migrate` (to make the change in db for the new model)
18. Now to make the admin panel available for the model, register the model in admin.
```
from .models import Event

admin.site.Register(Event)
```
19. `pip install djangorestframework` (to install the rest api framework)
20. whenever we install new module, we need to tell django about it so goto settings.py and 'rest_framework' in INSTALLED_APPS array.
21. First we need to create serializer for the model so create new file in event folder name serializer.py and enter below code.
```
from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('title', 'description')

def validate_title(self, attrs, source):
    value = attrs[source]
    if "django" not in value:
        return False
    else:
        True
```
22. now we need to create view for the response of api and map the serializer and model so goto views.py and enter below code.
```
from rest_framework import viewsets
from .models import Event
from .serializer import EventSerializer

class EventView(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
```
23. Final step to add router and handle the url and map the view so open the urls.py file and enter below code.
```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import EventView

router = DefaultRouter()
router.register('events', EventView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
```