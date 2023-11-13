from django.shortcuts import render, redirect
from .forms import FormularioAudit, SearchForm
from .models import Audit 
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import openpyxl




@login_required
def form_template(request):
    form = FormularioAudit()
    return render(request, 'form_audit/form_audit.html', {'form': form})
@login_required
def form_audit(request):
    if request.method == 'POST':
        form = FormularioAudit(request.POST)
        if form.is_valid():
            audit_instance = form.save(commit=False)  # Obtener la instancia del modelo sin guardarla aún
            
            # Realizar cálculos para el campo 'total'
            cantidad = int(audit_instance.cantidad)
            denominacion = int(audit_instance.denominacion)
            excedente = int(audit_instance.excedente)
            faltante = int(audit_instance.faltante)

            total = cantidad * denominacion + excedente - faltante

            audit_instance.total = total  # Actualizar el campo 'total' en la instancia del modelo

            audit_instance.save()  # Guardar el objeto en la base de datos con el 'total' actualizado

            return render(request, 'form_audit/form_ok.html')
    else:
        form = FormularioAudit()
    return render(request, 'form_audit/form_audit.html', {'form': form})

@login_required
def search_template(request):
    form = FormularioAudit()
    return render(request, 'form_audit/search_audits.html',{'form': form})

@login_required
def search_audit(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            pais = form.cleaned_data['pais']
            delegacion = form.cleaned_data['delegacion']
            fecha = form.cleaned_data['fecha']

            try:
                # Convertir la fecha a cadena y luego a la representación deseada (año-mes-día)
                fecha = datetime.strptime(str(fecha), "%Y-%m-%d").strftime("%Y-%m-%d")

                audits = Audit.objects.filter(Q(pais=pais) & Q(delegacion=delegacion) & Q(fecha_creacion=fecha))
                if audits:
                    return render(request, 'form_audit/success_search.html', {'audits': audits})
            except ValueError:
                pass

    return render(request, 'form_audit/negative_search.html')


@login_required
def logout_view(request):
    logout(request)
    
    return redirect('login')  


@login_required
def download_excel(request):
    audits = Audit.objects.all()  # Obtén todos los datos de auditoría

    # Crear un libro de trabajo de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Pais', 'Delegacion', 'Cliente', 'Sector', 'Saldo', 'Divisa', 'Tipo', 'Cantidad de tipo', 'Denominacion', 'Excedente', 'Faltante', 'Total', 'Fecha de auditoria'])

    for audit in audits:
        ws.append([
            audit.pais, audit.delegacion, audit.cliente, audit.sector, audit.saldo, audit.divisa, audit.tipo, audit.cantidad, audit.denominacion, audit.excedente, audit.faltante, audit.total, audit.fecha_creacion
        ])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="audits.xlsx"'

    wb.save(response)
    return response