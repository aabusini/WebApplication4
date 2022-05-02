import xlwt
import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Data


# Create your views here.


def index(request):
    #template = loader.get_template('delete.html')
    # return HttpResponse(template.render())

    # data = Data.objects.all()[:5]
    # output = '<br>'.join([c.first_name for c in data])
    # return HttpResponse(output)

    # allData = Data.objects.all()
    # context = {'allData': allData}
    # objs=Data.objects.all()
    # return HttpResponse(template.render({}, request))
    # return render(request,'delete.html',{'objs':objs})

    allData = Data.objects.all()
    template = loader.get_template('delete.html')
    context = {
        'showData': allData,
    }
    return HttpResponse(template.render(context, request))

    def showData(request):
        allData = Data.objects.all()
        template = loader.get_template('delete.html')
        context = {
            'showData': allData,
        }
    return HttpResponse(template.render(context, request))

def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    with(open('data.csv', 'w', encoding='utf-8-sig')) as fh:
        writer = csv.writer(response)
        writer.writerow(['objectid', 'first_name', 'nationality', 'unilevel', 'ben_id', 'fisrt_phone', 'second_phone', 'gov', 'org_name', 'interested_in_working', 'benefited_from_makani', 'vaccinated', 'courses', 'created_date', 'lastdegree', 'readw', 'other_ben', 'other_ben_id'])

    users = Data.objects.all().values_list('objectid', 'first_name', 'nationality', 'unilevel', 'ben_id', 'fisrt_phone', 'second_phone', 'gov', 'org_name', 'interested_in_working', 'benefited_from_makani', 'vaccinated', 'courses', 'created_date', 'lastdegree', 'readw', 'other_ben', 'other_ben_id')
    for user in users:
        writer.writerow(user)

    return response


def export_data_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Data')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['objectid', 'first_name', 'nationality', 'unilevel', 'ben_id', 'fisrt_phone', 'second_phone', 'gov', 'org_name', 'interested_in_working', 'benefited_from_makani', 'vaccinated', 'courses', 'lastdegree', 'readw', 'other_ben', 'other_ben_id']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Data.objects.all().values_list('objectid', 'first_name', 'nationality', 'unilevel', 'ben_id', 'fisrt_phone', 'second_phone', 'gov', 'org_name', 'interested_in_working', 'benefited_from_makani', 'vaccinated', 'courses', 'lastdegree', 'readw', 'other_ben', 'other_ben_id')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response