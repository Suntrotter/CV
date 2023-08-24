from django.contrib import admin
from django.urls import path, include
from resume.urls import urlpatterns
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns)),
    path('profiles/', include(urlpatterns)),
    path('image/', views.update_photo),
    path('update_aboutme/', views.update_aboutme),
    path('update_skills/', views.update_skills),
    path('update_education/', views.update_education),
    path('update_projects', views.update_projects)
]
