
from django.urls import path
from employee import views


app_name = "employee"

urlpatterns = [
    path('',views.home,name='home'),  
    path('userregister/',views.userregister,name='userregister'),  
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name="userlogout"),    
    path('userlist/',views.userlist,name='userlist'),  
    path('userleave/',views.userleave,name="userleave"),
    path('userdelete/<int:id>',views.userdelete,name="userdelete"),
    path('userupdate/<int:id>',views.userupdate,name="userupdate"),
    path('usernewpassword/',views.usernewpassword,name="usernewpassword"),   
    path('usermakepassword/<int:id>',views.usermakepassword,name="usermakepassword"),   
    path('userapplyleave/<int:id>',views.userapplyleave,name="userapplyleave"),
    # path('new/',views.new,name="new"),   

    
]


