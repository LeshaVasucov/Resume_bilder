from django.urls import path
from resume_creator import views
urlpatterns = [
    path("resume-create", views.ResumeCreateView, name="resume-create"),
    path("", views.ResumeListView, name="resume-list")
]
