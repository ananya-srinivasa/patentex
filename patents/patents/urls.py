from django.contrib import admin
from django.urls import path
from members import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginPage,name='login'),
    path('create/',views.Createpage,name='create'),
    path('login/', login_required(views.LoginPage), name='login'),
    path('agent_reg/',views.AgentSignupPage,name ='agent_signup'),
    path('home/',views.HomePage,name='home'),
    path('organisation/', views.OrganisationPage, name='organisation'),
    path('logout/',views.LogoutPage,name='logout'),
    


    
]