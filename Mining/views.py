from django.http import HttpResponse
from django.template import loader
from Mining.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template


def index(request):
    template = loader.get_template('mining/index.html')
    context = {
        'title': "PSMHome Mining",
    }
    return HttpResponse(template.render(context, request))

def product(request, product):
    return render(request, 'mining/product.html', {'product': product})

def services(request):
    template = loader.get_template('mining/services.html')
    context = {
        'title': "PSMHome Mining",
    }
    return HttpResponse(template.render(context, request))


def gallery(request):
    template = loader.get_template('mining/gallery.html')
    context = {
        'title': "PSMHome Mining",
    }
    return HttpResponse(template.render(context, request))


def products(request):
    template = loader.get_template('mining/products.html')
    context = {
        'title': "PSMHome Mining",
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('mining/about.html')
    context = {
        'title': "PSMHome Mining",
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            contact_phone = request.POST.get('contact_phone', '')

            # Email the profile with the
            # contact information
            template = get_template('mining/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage("New contact form submission", content, "Your website" + '',
                                 ['amirbedair83@gmail.com'], headers={'Reply-To': contact_email}
                                 )
            email.send()
            return redirect('contact')
    return render(request, 'mining/contact.html', {
        'form': form_class,
    })
