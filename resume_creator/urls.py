from django.urls import path
from resume_creator import views
urlpatterns = [
    path("resume-create", views.ResumeCreateView, name="resume-create"),
    path("", views.ResumeListView, name="resume-list"),
    path("resume-file-get<int:pk>",views.ResumeFileCreateView, name="resume-file-get"),
    path("<int:pk>", views.ResumeDetails , name="resume-details"),
    path("attachment-create<int:pk>", views.ResumeAttachmentCreateView, name="attachment-create"),
]
