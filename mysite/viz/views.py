import random, datetime, time
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import IncomeTract, SiteLocation

def index(request):
    data = SiteLocation.objects.all()
    context = {'site_list': data}
    return render(request, 'viz/index.html', context)
   
def tracts(request):
    data = IncomeTract.objects.all()
    context = {'tract_list': data}
    return render(request, 'viz/tracts.html', context) 

def tracts_site(request, tract_id):
    sites = SiteLocation.objects.filter(tract=tract_id).values()
    # data = get_object_or_404(sites, tract=tract_id)
    context = {'tracts_site_list': sites}
    return render(request, 'viz/tracts_site.html', context)

def sites(request):
    data = SiteLocation.objects.all()
    context = {'site_list': data}
    return render(request, 'viz/sites.html', context) 

def pie(request):
    """
    pieChart page
    """
    xdata = ["$1-10,000", "$10,000-25,000", "$25,000-30,000", "$30,000-40,000", "$40,000-55,000", "$55,000-70,000", "$70,000-85,000", "$85,000-100,000", "$100,000-150,000", "$150,000-190,000"]
    ydata = [   SiteLocation.objects.filter(income__gt=0).filter(income__lte=10000).count(), 
                SiteLocation.objects.filter(income__gt=10000).filter(income__lte=25000).count(), 
                SiteLocation.objects.filter(income__gt=25000).filter(income__lte=30000).count(),
                SiteLocation.objects.filter(income__gt=30000).filter(income__lte=40000).count(),
                SiteLocation.objects.filter(income__gt=40000).filter(income__lte=55000).count(),
                SiteLocation.objects.filter(income__gt=55000).filter(income__lte=70000).count(),
                SiteLocation.objects.filter(income__gt=70000).filter(income__lte=85000).count(),
                SiteLocation.objects.filter(income__gt=85000).filter(income__lte=100000).count(),
                SiteLocation.objects.filter(income__gt=100000).filter(income__lte=150000).count(),
                SiteLocation.objects.filter(income__gt=150000).filter(income__lte=190000).count()
            ]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " sites"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('viz/pie.html', data)

def bar(request):
    """
    multibarchart page
    """
    total_site_count = SiteLocation.objects.all().count()
    total_income_count = IncomeTract.objects.all().count()


    xdata = ["$1-10,000", "$10,000-25,000", "$25,000-30,000",
            "$30,000-40,000", "$40,000-55,000", "$55,000-70,000", 
           "$70,000-85,000", "$85,000-100,000", "$100,000-150,000", "$150,000-190,000"]

    #xdata = [0]
    nb_element = 10
    #xdata = range(nb_element)

    ydata = [   round(SiteLocation.objects.filter(income__gt=0).filter(income__lte=10000).count()/total_site_count,4)*100, 
                round((SiteLocation.objects.filter(income__gt=10000).filter(income__lte=25000).count()/total_site_count),4)*100, 
                round(SiteLocation.objects.filter(income__gt=25000).filter(income__lte=30000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=30000).filter(income__lte=40000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=40000).filter(income__lte=55000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=55000).filter(income__lte=70000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=70000).filter(income__lte=85000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=85000).filter(income__lte=100000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=100000).filter(income__lte=150000).count()/total_site_count,4)*100, 
                round(SiteLocation.objects.filter(income__gt=150000).filter(income__lte=190000).count()/total_site_count,4)*100 
            ]

    ydata2 = [  round(IncomeTract.objects.filter(income__gt=0).filter(income__lte=10000).count()/total_income_count,4)*100, 
                round(IncomeTract.objects.filter(income__gt=10000).filter(income__lte=25000).count()/total_income_count,4)*100, 
                round(IncomeTract.objects.filter(income__gt=25000).filter(income__lte=30000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=30000).filter(income__lte=40000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=40000).filter(income__lte=55000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=55000).filter(income__lte=70000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=70000).filter(income__lte=85000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=85000).filter(income__lte=100000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=100000).filter(income__lte=150000).count()/total_income_count,4)*100,
                round(IncomeTract.objects.filter(income__gt=150000).filter(income__lte=190000).count()/total_income_count,4)*100
            ]

    extra_serie_1 = {"tooltip": {"y_start": "", "y_end": "% of superfund sites in income bracket"}}
    extra_serie_2 = {"tooltip": {"y_start": "", "y_end": "% of census tracts in income bracket"}}

    chartdata = {
        'x': xdata,
        'name1': 'Sites in proportion to Income', 'y1': ydata, 'extra1': extra_serie_1, #number of sites with blank income
        'name2': 'Tracts in proportion to Income', 'y2': ydata2, 'extra2': extra_serie_2,
    }

    charttype = "multiBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('viz/bar.html', data)
