from django.db import models

class Audit(models.Model):
    pais_choices = [
        ('Argentina', 'Argentina'), ('Chile', 'Chile'), ('España', 'España'), ('México', 'México'), ('Perú', 'Perú')
    ]

    delegacion_choices = [
        ('sur', 'Delegación Sur'), ('norte', 'Delegación Norte'), ('este', 'Delegación Este'), ('oeste', 'Delegación Oeste')
    ]
    
    sector_choices = [
        ('boveda', 'Boveda'), ('caja', 'Caja'), ('atm', 'ATM'), ('otr', 'Otro')
    ]
    
    divisa_choices = [
        ('pesos argentinos', 'Pesos argentinos'), ('dolares', 'Dolares'), ('guaranies', 'Guaranies'), ('euros', 'Euros'), ('reales', 'Reales'), ('chq_pesos', 'Chq Pesos'), ('chq_dolares', 'Chq Dolares')
    ]
    
    tipo_choices = [
        ('bala', 'Bala'), ('pico', 'Pico'), ('bulto_monedas', 'Bulto Monedas')
    ]
    
    saldo_choices = [
        ('saldo', 'Saldo'), ('moneda', 'Moneda'), ('atm', 'ATM')
    ]
    
    denominacion_choices = [
        ('1', '$1'), ('2', '$2'), ('5', '$5'), ('10', '$10'), ('20', '$20'), ('50', '$50'), ('100', '$100'), ('200', '$200'), ('500', '$500'), ('1000', '$1.000'), ('2000', '$2.000'), ('5000', '$5.000'), ('10000', '$10.000'), ('20000', '$20.000'), ('50000', '$50.000'), ('100000', '$100.000')
    ]
    
    pais = models.CharField(max_length=50, choices=pais_choices)
    delegacion = models.CharField(max_length=50, choices=delegacion_choices)
    cliente = models.CharField()
    sector = models.CharField(max_length=50, choices=sector_choices)
    saldo = models.CharField(max_length=50, choices=saldo_choices)
    divisa = models.CharField(max_length=50, choices=divisa_choices)
    tipo = models.CharField(max_length=50, choices=tipo_choices)
    cantidad = models.IntegerField()
    denominacion = models.CharField(max_length=50, choices=denominacion_choices)
    excedente = models.DecimalField(max_digits=15, decimal_places=2)
    faltante = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)
