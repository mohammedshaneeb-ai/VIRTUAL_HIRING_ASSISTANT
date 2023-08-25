from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('/job_post/', views.job_post, name='job_post'),
    path('update_job/<int:job_id>/', views.update_job, name='update_job'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    


]