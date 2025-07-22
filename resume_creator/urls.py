from django.urls import path
from resume_creator import views
urlpatterns = [
    path("resume-create", views.ResumeCreateView, name="resume-create"),
    path("", views.ResumeListView, name="resume-list"),
    path("resume-file-get<int:pk>",views.ResumeFileCreateView, name="resume-file-get"),
    path("<int:pk>", views.ResumeDetails , name="resume-details"),
    path("attachment-create<int:pk>/<str:category>", views.ResumeAttachmentCreateView, name="attachment-create"),
    path("attachment-details<int:pk>/<int:id>", views.AttachmentDetails, name="attachment-details"),
    path("resume-file-load<int:pk>", views.ResumeFileLoadView, name="resume-file-load")
]
