# Django imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# User-defined modules
from .utils import _get_all_invoices, _get_invoice

def home(request):
    '''
    Args:
        request:object = Request object.
    Returns:
        Renders home page using home.html template.
    '''

    return render(request, "home.html")

def get_all_invoices(request, company_id):
    '''
    Args:
        request:object = Request object.
        company_id = Company id for which invoices are needed. 
    Returns:
        Renders invoice.html template by sending invoice imformation.
    '''

    if not company_id:
        result = {"success": False, "response": "Company ID cannot be empty"}
        return render(request, "invoice.html", dict(result=result))

    result = _get_all_invoices(company_id)
    return render(request, "invoice.html", dict(result=result, company_id=company_id))

def get_invoice(request, company_id, invoice_id):
    '''
    Args:
        request:object = Request object.
        company_id:str = Company id for which invoices are needed.
        invoice_id:str = ID of the invoice
    Returns:
        Json format of Invoice information
    '''

    if not company_id:
       return JsonResponse({"success": False, "response": "Company ID cannot be empty"})

    if not invoice_id:
       return JsonResponse({"success": False, "response": "Company ID cannot be empty"})

    result = _get_invoice(company_id, invoice_id)
    return JsonResponse(result)
