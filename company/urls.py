import re

from django.urls import re_path, path

from . import views

urlpatterns = [
    re_path("^$", views.home, name="home"),
    re_path(r"^get_all_invoices/(?P<company_id>[\w-]+)/$",
        views.get_all_invoices,
        name="get_all_invoices"),
    re_path(r"^get_invoice/(?P<company_id>[\w-]+)/(?P<invoice_id>[\w-]+)$",
        views.get_invoice,
        name="get_invoice_by_number"),
]
