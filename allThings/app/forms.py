from django import forms
from django.db.models import fields
from django.db.models.expressions import CombinedExpression, F
from django.forms.fields import CharField
from .models import *
from django.forms import ValidationError
import datetime

class RegProductoForm(forms.ModelForm):
    def clean_codigo_de_Barras(self):
        codBarras = self.cleaned_data["codigo_de_Barras"]
        existe = Producto.objects.filter(codigo_de_Barras = codBarras).exists()
        
        if existe:
            raise ValidationError("Este codigo de barras ya esta siendo utilizado!")
        
        return codBarras
    def clean_fecha_de_Ingreso(self):
        
        fecha = self.cleaned_data["fecha_de_Ingreso"]
        if fecha > datetime.date.today():
            raise forms.ValidationError("Debes ingresar la fecha de hoy o fechas pasadas")
        return fecha   
    
    nombre = forms.CharField(min_length=3, max_length=50)
    stock = forms.IntegerField(min_value=1, max_value=999999)
    precio_Venta = forms.IntegerField(min_value=20, max_value=9999999)
    precio_Costo = forms.IntegerField(min_value=10, max_value=9999999)
    imagen = forms.ImageField(required=False)

    
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_de_Ingreso' : forms.SelectDateWidget(years=range(1945, 2022))
        }
    
class ModProductoForm(forms.ModelForm):
    def clean_fecha_de_Ingreso(self):
        
        fecha = self.cleaned_data["fecha_de_Ingreso"]
        if fecha > datetime.date.today():
            raise forms.ValidationError("Debes ingresar la fecha de hoy o fechas pasadas")
        return fecha   
    
    nombre = forms.CharField(min_length=3, max_length=50)
    stock = forms.IntegerField(min_value=1, max_value=999999)
    precio_Venta = forms.IntegerField(min_value=20, max_value=9999999)
    precio_Costo = forms.IntegerField(min_value=10, max_value=9999999)
    imagen = forms.ImageField(required=False)

    
    class Meta:
        model = Producto
        fields = '__all__'
        
        widgets = {
            'fecha_de_Ingreso' : forms.SelectDateWidget(years=range(1945, 2022))
        }
    
class RegMarcaForm(forms.ModelForm):
    
    def clean_id(self):
        identificador = self.cleaned_data["id"]
        existe = Marca.objects.filter(id = identificador).exists()
        
        if existe:
            raise ValidationError("Este id ya esta siendo utilizado!")
        
        return identificador
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Marca.objects.filter(nombre = nombre).exists()
        
        if existe:
            raise ValidationError("Este Nombre ya esta siendo registrado!")
        
        return nombre
    nombre = forms.CharField(min_length=1, max_length=50)
    class Meta:
        model = Marca
        fields = '__all__'
        

class ModMarcaForm(forms.ModelForm):

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Marca.objects.filter(nombre = nombre).exists()
        
        if existe:
            raise ValidationError("Este Nombre ya esta siendo registrado!")
        
        return nombre
    nombre = forms.CharField(min_length=1, max_length=50)
    class Meta:
        model = Marca
        fields = '__all__'

class RegUsuarioForm(forms.ModelForm):

    rut = forms.IntegerField(min_value=1000000, max_value=99999999)
    nombre = forms.CharField(min_length=3, max_length=50)
    apellido_Materno = forms.CharField(min_length=3, max_length=50)
    apellido_Paterno = forms.CharField(min_length=3, max_length=50)

    class Meta:
        model = Usuario
        fields = '__all__'
    
        widgets = {
            'fecha_de_Nacimiento' : forms.SelectDateWidget(years=range(1945, 2022))
        }
    def clean_rut(self):
        rut = self.cleaned_data["rut"]
        existe = Usuario.objects.filter(rut = rut).exists()

        if existe:
            raise ValidationError("Este rut ya está registrado!")    
        return rut   

    def clean_fecha_de_Nacimiento(self):
        
        fecha = self.cleaned_data["fecha_de_Nacimiento"]
        if fecha > datetime.date.today():
            raise forms.ValidationError("Debes ingresar una fecha valida")
        return fecha 
    


class ModUsuarioForm(forms.ModelForm):

    def clean_fecha_de_Nacimiento(self):
        
        fecha = self.cleaned_data["fecha_de_Nacimiento"]
        if fecha > datetime.date.today():
            raise forms.ValidationError("Debes ingresar una fecha valida")
        return fecha 

    rut = forms.IntegerField(min_value=1000000, max_value=99999999)
    nombre = forms.CharField(min_length=3, max_length=50)
    apellido_Materno = forms.CharField(min_length=3, max_length=50)
    apellido_Paterno = forms.CharField(min_length=3, max_length=50)


    class Meta:
        model = Usuario
        fields = '__all__'

        widgets = {
            'fecha_de_Nacimiento' : forms.SelectDateWidget(years=range(1945, 2022))
        }
        

