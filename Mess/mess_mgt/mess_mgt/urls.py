
from django.contrib import admin
from django.urls import path
from  mess_app import views

urlpatterns = [
    path("admin/", admin.site.urls),




    path('base', views.index, name='base'),
    path('memberlist/', views.memberlist, name= 'memberlist'),
    path('join_mess/', views.joinmess, name='join_mess'),
    path('memberinfo/<int:mem>/', views.memberinfo, name='memberinfo'),
    path('upmember/<int:upmem_id>/', views.upmember, name='upmember'),
    path('mealing/', views.mealing1, name='mealing' ),
    path('editmeal/<int:meal_id>/', views.editmeal, name= 'editmeal'),
    path('delmeal/<int:meal_id>/', views.delmeal, name='delmeal'),
    path('delmem/<int:upmem_id>/', views.delmeam, name='delmem'),


    path('test/',views.test,name='test'),
    


    path('', views.userlogin, name= 'user_login'),
    path('register/', views.registrer, name='register'),
    path('logout/', views.user_logout, name='logout'),


 



]

