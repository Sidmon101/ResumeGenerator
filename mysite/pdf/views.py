from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from .models import Profile

def home(request):
    return render(request, 'pdf/home.html')

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        experience = request.POST.get("experience", "")
        skills = request.POST.get("skills", "")
        template_choice = request.POST.get("template_choice", "template1")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, experience=experience, skills=skills, template_choice=template_choice)
        profile.save()
        return redirect('user_list')
    return render(request, 'pdf/accept.html')


def resume(request, id):
    user_profile = get_object_or_404(Profile, pk=id)
    template_name = f'pdf/resume_{user_profile.template_choice}.html'
    return render(request, template_name, {'user_profile': user_profile})

def download_resume_pdf(request, id):
    user_profile = get_object_or_404(Profile, pk=id)
    template_name = f'pdf/resume_{user_profile.template_choice}.html'
    html_string = render_to_string(template_name, {'user_profile': user_profile})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf_file = html.write_pdf()

    # Get custom filename from query parameter
    custom_filename = request.GET.get('filename', 'resume')
    safe_filename = slugify(custom_filename) + '.pdf'

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{safe_filename}"'
    return response

def user_list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/user_list.html', {'profiles': profiles})
