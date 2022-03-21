from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def index(request):
    if request.method=="POST":

        print(request.POST['name'])
        print(request.POST)
        name=request.POST['name']
        email=request.POST['Email']
        phonenumber=request.POST['Phone number']
        annualincome=request.POST['Annual Income']
        loanpurpose=request.POST['loanpurpose']
        data={
            'name':name,
            'email':email,
            'phonenumber':phonenumber,
            'annualincome':annualincome,
            'loanpurpose':loanpurpose

        }
        print(data)
        template = get_template("pdf.html")
        html = template.render(data)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None
        pdf=pdf
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

        # return HttpResponse(pdf, content_type='application/pdf')

        # force download




        return HttpResponse("hello world ")
    else:
        return render(request,"index.html")


