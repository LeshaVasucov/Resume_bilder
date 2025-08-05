from django.shortcuts import render , redirect
from django.http import FileResponse , HttpResponse
from resume_creator.models import Resume
from resume_creator.forms import ResumeForm, EducationForm, IndividualInfoForm, WorkExperienceForm, ProjectForm, CategoryFilterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from fpdf import FPDF
from time import time
# Create your views here.
def ResumeListView(request):
    user = request.user.id
    print(user)
    resumes = Resume.objects.filter(creator=user)
    
    context = {
        "resumes" : resumes
    }
    return render(request, "resume_creator/resume_list.html", context)

def ResumeDetails(request, pk):
    resume = Resume.objects.get(id=pk)
    category = request.GET.get("category", "")
    attachment_form = 0
    if category == "education" :
        attachment_form = EducationForm()
    elif category == "individual_info":
        attachment_form = IndividualInfoForm()
    elif category == "work_experience" :
        attachment_form = WorkExperienceForm()
    elif category == "project":
        attachment_form = ProjectForm()
    context = {
        "resume" : resume,
        "filter_form" : CategoryFilterForm(request.GET),
        "attachment_form" : attachment_form ,
        "category" : category
    }
    return render(request, "resume_creator/resume_details.html", context=context)

@login_required
def ResumeCreateView(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.text = form.cleaned_data.get("text")
            resume.creator = request.user
            resume.type = "base"
            resume.save()
            return redirect("resume-list")
    else:
        form = ResumeForm()
        return render(request, "resume_creator/resume_form.html", context={ "form" : form })
    
def ResumeAttachmentCreateView(request, pk, category):
    if request.method == "POST":
        if category == "education":
            form = EducationForm(request.POST, request.FILES)
        elif category == "individual_info":
            form = IndividualInfoForm(request.POST, request.FILES)
        elif category == "work_experience" :
            form = WorkExperienceForm(request.POST, request.FILES)
        elif category == "project":
            form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save()
            attachment.category = category
            resume = Resume.objects.get(id=pk)
            resume.attachments.add(attachment)
            if attachment:
                attachment.save()
            resume.save()
            
    return redirect("resume-details", pk=pk)

def AttachmentDetails(request, pk, id):
    resume = Resume.objects.get(id=pk)
    attachment = resume.attachments.get(id=id)
    context={
        "attachment" : attachment
    }
    
    return render(request, "resume_creator/attachment_details.html", context)

def ResumeFileCreateView(request, pk):
    resume = Resume.objects.get(id=pk)
    resume_text = resume.description
    fpath = f"media/documents/{request.user}_{time()}.pdf"

    pdf = FPDF()
    pdf.add_font('DejaVu', '', 'media/fonts/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.add_page()
    pdf.set_fill_color(r=0,g=0,b=0)
    pdf.rect(h=pdf.h, w=100, x=0, y=0, style="DF")
    pict_x, pict_y, pict_w = 10, 15, 50
    #аватарка 
    if resume.pict :
        pdf.image(resume.pict.path, x=pict_x, y=pict_y, w=pict_w)
    else:
        pdf.image("media/user.png", x=pict_x, y=pict_y, w=pict_w)

    #о себе
    pdf.set_xy(105,15)
    pdf.multi_cell(w=100, h=10, text= f'Про себе : \n{resume_text}',border=True)
    #проекты
    pdf.set_font('DejaVu', '', 12)
    for attachment in resume.attachments.all():
        if attachment.category == "project":
            pdf.set_xy(105,pdf.y+10)
            pdf.multi_cell(w=100, h=10, text= f'{attachment.project_name}\nІдея проекту : {attachment.project_idea}\nBикopиcтaнi технології : {attachment.used_technologies}\nGithub: {attachment.github}',border=True)
    #вложения attachments всякие
    pdf.set_text_color(236, 224, 113)
    attachment_x = 10
    pdf.set_y(70)
    pdf.set_font('DejaVu', '', 14)
    for attachment in resume.attachments.all():
        pdf.set_x(attachment_x)
        pdf.set_y(pdf.y+5)
        if attachment.category == "work_experience" :
            pdf.multi_cell(w=90, h=10, text=f"Досвід роботи : \nНазва роботи : {attachment.work_name} \nДосвід : {attachment.work_experience}", border=True)
        elif attachment.category == "education" :
            pdf.multi_cell(w=90, h=10, text=f'Освіта : \n{attachment.education}', border=True)
        elif attachment.category == "individual_info":
            pdf.multi_cell(w=90, h=10, text=f"Контактна інформація : \nНомер телефону : {attachment.phone_number} \nEmail : {attachment.email} \nАдреса : {attachment.address}", border=True)
        
    #создание
    pdf.output(fpath, 'F')
    print(fpath)
    resume.file_path = fpath
    resume.save()
    
    messages.success(request, "PDF-файл успішно збережено!")
    print(resume.file_path)
    return redirect("resume-details", pk=pk)
    # return FileResponse(open(resume.file_path, 'rb'), content_type='application/pdf')
    
def ResumeFileLoadView(request,pk):
    resume = Resume.objects.get(id=pk)
    return FileResponse(open(resume.file_path, 'rb'), as_attachment=True, content_type='application/pdf')
