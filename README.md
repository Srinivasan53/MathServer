# Ex.05 Design a Website for Server Side Processing
## Date:03.12.24

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html


<html>
<head>
<style>

.edge
 { display:flexbox;
    margin-top: 150px;
    margin-bottom:auto;
    margin-left: auto;
    margin-right: auto;
    border-style:groove;
    border-color: yellow;
   background-color: rgb(25, 260, 80);
    padding-top: 60px;
    padding-right: 55px;
    padding-bottom: 65px;
    padding-left: 70px;
    width: 30%;
    flex-direction: column;
    
  }
  body{
    background-color: paleturquoise;
  }
div.formelt
{
    font-size: 100%;
   color:brown ;
  
    
}
div.box
{
  color: red;
  text-align: center;
  font-style:initial;
  
}
input
{
  padding: 20px;
  border:0rch;
  border-radius: 4px;
  width: 40%;
  align-items: center;
}
</style>
</head>
<body>
    <div class="edge">
        <div class="box">
            <h1>POWER OF THE LAMP</h1>
            <form method="POST">
                {% csrf_token %}
            </div>
            <h2>Srinivasan S (24005090)</h2>
                <div class="formelt">
                    <br>
                    Intensity : <input type="text" name="Intensity" value="{{I}}"></input>(at W/m <sup> 2 </sup>) <br>
                </div>
                <div class="formelt">
                    <br>
                    Resistance : <input type="text" name="Resistance" value="{{R}}"></input>(at ohm)<br>

                </div>
                
                <div  class="formelt">
                    <br>
                    <input type="submit" value="click"></input><br>
                </div>
                <div class="formelt">
                    <br>
                power : <input type="text" name="power" value="{{power}}"></input>(at watt)<br>
                </div>
 
            </form>
    </div>
</body>

</html>

views.py

from django.shortcuts import render 
def powerbulb(request): 
    context={} 
    context['power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistanc=',R) 
        power = (int(I) * int(I)) *int(R) 
        context['power'] = power 
        context['I'] = I
        context['R'] = R 
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

    urls.py

    from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
path('admin/', admin.site.urls), 
path('powerofthelamp/',views.powerbulb,name="powerofthelamp"),
 path('',views.powerbulb,name="powerofthelamp")
]
```
## SERVER SIDE PROCESSING:
![alt text](<Screenshot (689).png>)

## HOMEPAGE:
![alt text](<Screenshot (688).png>)

## RESULT:
The program for performing server side processing is completed successfully.
