from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('Register/',views.register_user,name='register'),
    path('record/<int:pk>',views.customer_record,name='record'),
    path('delete_record/<int:pk>',views.customer_delete,name='delete_record'),
    path('add_record/',views.customer_add,name='add_record')
    
]
