import csv

from django.shortcuts import render
from pprint import pprint


def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', encoding='cp1251') as f:
        inflation_data = csv.DictReader(f, delimiter = ';')
        inflation_data = list(inflation_data)

        pprint(inflation_data)


    context = {
        'inflation_data': inflation_data
    }

    return render(request, template_name,
                  context)