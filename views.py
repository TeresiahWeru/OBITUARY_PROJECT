from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from .models import Obituary
from django.db import DatabaseError

def submit_obituary(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            date_of_birth = request.POST['date_of_birth']
            date_of_death = request.POST['date_of_death']
            content = request.POST['content']
            author = request.POST['author']
            slug = slugify(name)

            # Create and save the obituary instance
            obituary = Obituary(
                name=name,
                date_of_birth=date_of_birth,
                date_of_death=date_of_death,
                content=content,
                author=author,
                slug=slug
            )
            obituary.save()
            return HttpResponse('Obituary submitted successfully!')

        except DatabaseError as e:
            return HttpResponse(f'An error occurred: {e}')
    return render(request, 'obituary_form.html')
from django.shortcuts import render
from .models import Obituary
from django.core.paginator import Paginator

def view_obituaries(request):
    obituaries_list = Obituary.objects.all()
    paginator = Paginator(obituaries_list, 10)  # Show 10 obituaries per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'view_obituaries.html', {'page_obj': page_obj})
from django.shortcuts import render, get_object_or_404
from .models import Obituary

def view_obituary(request, slug):
    obituary = get_object_or_404(Obituary, slug=slug)
    return render(request, 'view_obituary.html', {'obituary': obituary})
