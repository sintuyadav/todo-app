from django.urls import path
from .import views

urlpatterns = [
    path('',views.alltodos, name ='alltodos'),
    path('list/new',views.t_list, name='t_list'),
    path('task/<int:pk>/delete/',views.post_delete,name='post_delete'),
    path('update/<int:pk>/',views.update, name="update"),
    #path('task/<int:pk>',views.update, name='update')    
    ]