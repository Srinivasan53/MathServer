from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
path('admin/', admin.site.urls), 
path('powerofthelamp/',views.powerbulb,name="powerofthelamp"),
 path('',views.powerbulb,name="powerofthelamp")
] 
