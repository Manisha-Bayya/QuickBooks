# Django imports
from django.conf import settings

# 3rd party imports
import requests

def _get_headers():
    '''
    Args:
        None.
    Returns:
        Headers dictionary.

    Gets access token from settings and creates headers dict.
    '''
    
    headers = {}
    headers["Authorization"] = "Bearer %s" %(settings.ACCESS_TOKEN)
    headers["Accept"] = 'application/json'
    return headers
    
def _request_intuit(method, url, headers={}, body=""):
    '''
    Args:
        method:str = Request type. Ex: get, post
        url:str = URL to be requested.
        headers:dict = Headers to be while requesting.
        body:str/dict/list = body to be sent while requesting.
    Returns:
        Response given by URL.

    Using python's request module, requests given url and gets response
    '''
    
    try:
        req_obj = getattr(requests, method)
    except Exception:
        return {"success": False, "response": "Wrong request type"}

    headers = _get_headers()
    resp = req_obj(url=url, headers=headers, data=body)
    try:
        result = resp.json()
    except Exception:
        result = resp.content
    return {"success": True, "response": result}

def _get_all_invoices(company_id):
    '''
    Args:
        company_id:str = Company id for which invoices are needed.
    Returns:
        list of invoices
    '''
    
    url = "https://sandbox-quickbooks.api.intuit.com"\
        "/v3/company/%s/query?query=select * "\
        "from Invoice" %(company_id)
    response = _request_intuit("get", url)
    return response

def _get_invoice(company_id, invoice_id):
    '''
    Args:
        company_id:str = Company id for which invoices are needed.
        invoice_id:str = ID of the invoice
    Returns:
        Invoice information
    '''

    url = "https://sandbox-quickbooks.api.intuit.com"\
        "/v3/company/%s/query?query="\
        "select * from Invoice where id = '%s'" %(company_id, invoice_id)
    response = _request_intuit("get", url)
    return response
