from openpyxl import Workbook
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def search_audits(request):
    return render(request, 'search_audits/search_audits.html')


@login_required
def descargar_excel(request):
    # Supongamos que tienes datos de ejemplo desde un formulario
    datos_formulario = {
        'Columna1': 'Dato1',
        'Columna2': 'Dato2',
        # Ajusta esto según los datos que tienes
    }

    libro_excel = Workbook()
    hoja_excel = libro_excel.active

    hoja_excel.append(list(datos_formulario.keys()))
    hoja_excel.append(list(datos_formulario.values()))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="formulario.xlsx"'

    libro_excel.save(response)

    return response