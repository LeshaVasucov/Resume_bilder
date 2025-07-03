from django.shortcuts import render , redirect
from django.http import FileResponse , HttpResponse
from resume_creator.models import Resume
from resume_creator.forms import ResumeForm, EducationForm, IndividualInfoForm, WorkExperienceForm, CategoryFilterForm
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
            
        if form.is_valid():
            attachment = form.save()
            attachment.category = category
            resume = Resume.objects.get(id=pk)
            resume.attachments.add(attachment)
            attachment.save()
            resume.save()
            
    return redirect("resume-details", pk=pk)
def ResumeFileCreateView(request, pk):
    resume = Resume.objects.get(id=pk)
    resume_text = resume.description
    fpath = f"pdf_files/{request.user}.pdf"

    pdf = FPDF()
    pdf.add_font('DejaVu', '', 'media/fonts/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.add_page()
    pict_x, pict_y, pict_w = 10, 15, 50
    #аватарка 
    if resume.pict :
        pdf.image(resume.pict.path, x=pict_x, y=pict_y, w=pict_w)
    else:
        pdf.image("media/user.png", x=pict_x, y=pict_y, w=pict_w)

    #о себе
    pdf.set_xy(pict_x + pict_w, pict_y)
    pdf.multi_cell(w=100, h=50, text= f'{resume_text}')

    #вложения attachments всякие
    attachment_x, attachment_y, attachment_w, attachment_h = pict_x + pict_w, pict_y + 60, 100,10
    pdf.set_xy(attachment_x, attachment_y)
    for attachment in resume.attachments.all():
        pdf.set_x(10)
        pdf.multi_cell(w=attachment_w,h=attachment_h, text= f'{attachment.title}\n{attachment.description}',
                       border=1, align='L')
        attachment_y += attachment_h

    #создание
    pdf.output(fpath, 'F')
    return FileResponse(open(fpath, "rb"),as_attachment=True, filename=f"{request.user}.pdf")
    