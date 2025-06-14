from django.shortcuts import render , HttpResponse
from django.http import FileResponse
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
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.text = form.cleaned_data.get("text")
            resume.creator = request.user
            resume.save()
            return HttpResponse("succeed", status=200)
    else:
        form = ResumeForm()
        return render(request, "resume_creator/resume_form.html", context={ "form" : form })
    
def ResumeFileCreateView(request, pk):
    resume = Resume.objects.get(id=pk)
    resume_text = resume.description
    fpath = f"pdf_files/{request.user}.pdf"

    pdf = FPDF()
    pdf.add_font('DejaVu', '', 'media/fonts/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.add_page()
    pict_x, pict_y, pict_w = 10, 15, 50

    if resume.pict :
        pdf.image(resume.pict.path, x=pict_x, y=pict_y, w=pict_w)
    else:
        pdf.image("media/user.png", x=pict_x, y=pict_y, w=pict_w)

    pdf.set_xy(pict_x + pict_w, pict_y)
    pdf.multi_cell(w=100, text= f'{resume_text}')
    pdf.output(fpath, 'F')

    return FileResponse(open(fpath, "rb"),as_attachment=True, filename=f"{request.user}.pdf")
    