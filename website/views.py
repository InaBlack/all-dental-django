from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactInfo, Service, TeamMember, BlogPost
from .forms import AppointmentForm, ContactForm
from django.urls import reverse
from django.contrib import messages


def home(request):
    ctx = {
        'contact': ContactInfo.objects.first(),
        'services': Service.objects.all()[:4],
        'team': TeamMember.objects.all()[:3],
    }
    return render(request, 'website/home.html', ctx)


def services(request):
    return render(request, 'website/services.html', {'services': Service.objects.all()})


def about(request):
    return render(request, 'website/about.html', {
        'team': TeamMember.objects.all(),
        'contact': ContactInfo.objects.first(),
    })


def booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu hora ha sido agendada!')
            return redirect(reverse('website:booking'))
    else:
        form = AppointmentForm()
    return render(request, 'website/booking.html', {'form': form})


def contact(request):
    contact_info = ContactInfo.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Mensaje enviado, ¡gracias!')
            return redirect('.')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'contact': contact_info, 'form': form})

def blog(request):
    posts = BlogPost.objects.order_by('-published_at')
    return render(request, 'website/blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'website/blog_detail.html', {'post': post})