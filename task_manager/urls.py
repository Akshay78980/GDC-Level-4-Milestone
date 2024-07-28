from django.contrib import admin
from django.urls import path, include
from tasks import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", views.get_task_manager_form, name='Task manager form'),
    path('add-task/', views.add_task, name='Add Task'),
    path('delete-task/<int:id>/', views.delete_taskno, name="Delete Specifc Task"),
    path('complete_task/<int:index>/', views.mark_completed, name="Mark completed"),
    path('completed_tasks/', views.render_completed_tasks, name="View completed tasks"),
    path('all_tasks/',views.render_all_tasks, name='Render all tasks')
    # Add all your views here
]
