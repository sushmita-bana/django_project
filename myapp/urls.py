from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page,name='home'),
    path('register/',views.register_page,name='register'),
    path('walkin/',views.walkins_page,name='walkin'),
    path('calling_page/',views.calling_page),
    path('calling_list/',views.calling_list,name ='calling_list'),
    path('counselling/',views.counselling),
    path('joining/',views.joining, name='joining'),
    path('update/',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete'),
    path('current_students<id>/',views.current_students,name='current_students'),
    path('current_students_update/',views.current_student_update,name="current_student_update"),
    path('students/<id>',views.students,name='students'),
   
]