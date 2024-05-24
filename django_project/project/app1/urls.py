from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('todo/',views.todo,name='todo'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('finished/<int:id>',views.finished,name='finished'),
    path('finished_data/',views.finished_data,name='finished_data'),
    path('finishedDelete/<int:id>',views.finishedDelete,name='finishedDelete')
]
