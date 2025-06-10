from django.shortcuts import render , HttpResponse
from resume_creator.models import Resume
from resume_creator.forms import ResumeForm
from django.contrib.auth.decorators import login_required
from fpdf import FPDF
# Create your views here.
def ResumeListView(request):
    user = request.user.id
    print(user)
    resumes = Resume.objects.filter(creator=user)
    
    context = {
        "resumes" : resumes
    }
    return render(request, "resume_creator/resume_list.html", context)

@login_required
def ResumeCreateView(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.text = form.cleaned_data.get("text")
            resume.pict = form.cleaned_data.get("pict")
            resume.creator = request.user
            resume.save()
            return HttpResponse("succeed", status=200)
    else:
        form = ResumeForm()
        return render(request, "resume_creator/resume_form.html", context={ "form" : form })
    
def ResumeFileCreateView(request):
    user = request.user
    