from django.shortcuts import render

# Create your views here.
from contacts.models import Contact
from contacts.forms import ContactForm

def contacts_list(request):
    contacts = Contact.objects.filter(is_active = True)
    context = {
        'contacts':contacts
    }
    return render(request, 'contacts/contacts-list.html', context=context)

def create_contact(request):
    if request.method == 'GET':
        context = {
            'form': ContactForm()
        }

        return render(request, 'contacts/contacts-create.html', context=context)

    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],

            )
            context = {
                'message': 'Contacto creado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ContactForm()
            }
            return render(request, 'contacts/contacts-create.html', context=context)
