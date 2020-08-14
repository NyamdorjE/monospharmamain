from blog.forms import ContactForm

def contact_form(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        return {'contact_form': contact_form}
    return