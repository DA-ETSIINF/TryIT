import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from register.forms import RegisterCompanyForm
from register.models import RegisterCompany


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        data = request.POST
        form = RegisterCompanyForm(data)
        if form.is_valid():
            register = RegisterCompany()
            register.contact_name = data['contactName'].strip()
            register.company = data.get('company', '').strip()
            register.email = data['email'].strip()
            register.phone = data['phone'].strip()
            register.sponsor = data['sponsor']

            if register.sponsor:
                register.sponsor_type = data['sponsorType']
                register.sponsor_date = data.get('sponsorDate', '')

            register.type = data['type']
            register.topic = data['topic'].strip()
            register.description = data['description'].strip()

            # File upload
            if 'document' in request.FILES:
                register.document = request.FILES['document']

            register.save()

            return HttpResponse('ok')
        else:
            error = {'id': 2, 'message': 'Error en la validación'}
            return HttpResponseBadRequest(json.dumps(error))
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])
