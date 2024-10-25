from django.urls import path
from .import views

urlpatterns=[
    path('fun1',views.fun1),
    path('fun2/<int:a>/<int:b>',views.fun2),
    path('demo',views.demo),
    path('display',views.display),
    path('user_reg',views.user_reg),
    path('edit_user/<id>',views.edit_user),
    path('delete_user/<id>',views.delete_user)
]