from django.db import models
from django.db.models.fields import IntegerField


# Create your models here.

class Marca(models.Model):
    id = IntegerField(primary_key=True)
    nombre  = models.CharField(max_length=50)
        
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo_de_Barras    = models.IntegerField(primary_key=True)
    nombre              = models.CharField(max_length=50)    
    marca               = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock               = models.IntegerField()
    precio_Costo        = models.IntegerField()
    precio_Venta        = models.IntegerField()
    fecha_de_Ingreso    = models.DateField()
    descripcion         = models.TextField()
    imagen              = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id = IntegerField(primary_key=True)
    nombre  = models.CharField(max_length=50)
        
    def __str__(self):
        return self.nombre

niveles = [0,"Educación Básica"],[1,"Educación Media"],[2,"Educación Superior"],[3,"Bachiller"],[4,"Licenciado"],[5,"Magister"],[6,"Doctorado"],[7,"Otro"]
dv = [0,"0"],[1,"1"],[2,"2"],[3,"3"],[4,"4"],[5,"5"],[6,"6"],[7,"7"],[8,"8"],[9,"9"],[10,"K"]
class Usuario(models.Model):
    rut                 = models.IntegerField(primary_key=True)
    digito_verificador  = models.IntegerField(choices=dv)
    nombre              = models.TextField(max_length=50)
    apellido_Paterno    = models.TextField(max_length=50)
    apellido_Materno    = models.TextField(max_length=50)
    email               = models.EmailField()
    fecha_de_Nacimiento = models.DateField()
    nivel_Educacional   = models.IntegerField(choices=niveles)
    pais                = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre 
