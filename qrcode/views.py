from django.shortcuts import render
from datetime import date
from qr_code.qrcode.utils import MeCard, VCard, QRCodeOptions

# Create your views here.

def qr_code(request):
    """
    qr_code
    """
    # qr_code_url = "https://www.google.com"
    # qr_code_url = "https://ecp.machinitechnologies.co.ke/"
    # qr_code_name = "ECP"
    # qr_code_email = "fredmanchini@gmail.com"
    # qr_code_phone = "0723456789"
    # qr_code_address = "Nairobi"
    # qr_code_image = MeCard(qr_code_name, qr_code_email, qr_code_phone, qr_code_address)
    # context = dict(
    #     qr_code_image=qr_code_image,
    # )

    mecard_contact = MeCard(
    name='Doe, John',
    phone='+41769998877',
    email='j.doe@company.com',
    url='http://www.company.com',
    birthday=date(year=1985, month=10, day=2),
    memo='Development Manager',
    org='Company Ltd'
)

    vcard_contact = VCard(
    name='Doe; John',
    phone='+41769998877',
    email='j.doe@company.com',
    url='http://www.company.com',
    birthday=date(year=1985, month=10, day=2),
    street='Cras des Fourches 987',
    city='Delémont',
    zipcode=2800,
    region='Jura',
    country='Switzerland',
    memo='Development Manager',
    org='Company Ltd'
)

    context = dict(
    mecard_contact=mecard_contact,
    vcard_contact=vcard_contact,
    options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
)

    return render(request, "index.html", context)
