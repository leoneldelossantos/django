from django.shortcuts import render
from django.views.generic import DeleteView

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
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                phone_number = form.cleaned_data['phone_number'],
                email = form.cleaned_data['email'],

            )
            context = {
                'message': 'Contacto creado exitosamente'
            }
            return render(request, 'contacts/contacts-create.html', context=context)

        else:
            context = {
                'form_errors': form.errors,
                'form': ContactForm()
            }
            return render(request, 'contacts/contacts-create.html', context=context)

def update_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': ContactForm(
                initial={
                    'name' : contact.name ,
                    'address': contact.address,
                    'phone_number': contact.phone_number,
                    'email': contact.email,
                }
            )
        }

        return render(request, 'contacts/update-contact.html', context=context)

    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                contact.name = form.cleaned_data['name']
                contact.address = form.cleaned_data['address']
                contact.phone_number = form.cleaned_data['phone_number']
                contact.email = form.cleaned_data['email']
                contact.save()

            
                context = {
                    'message': 'Contacto modificado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': ContactForm()
            }
        return render(request, 'contacts/update-contact.html', context=context)

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contacts/delete-contact.html'
    success_url = '/contacts/contacts-list/'