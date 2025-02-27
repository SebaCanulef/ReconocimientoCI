from django.db import models

class Tipo(models.Model):
    tipo_ID = models.AutoField(primary_key=True)
    tipo_nombre = models.CharField(max_length=50, null=False)

class Empresa(models.Model):
    empresa_ID = models.AutoField(primary_key=True)
    empresa_nombre = models.CharField(max_length=50, null=False)

class Lugar(models.Model):
    lugar_ID = models.AutoField(primary_key=True)
    lugar_nombre = models.CharField(max_length=50, null=False)


class Trabajador(models.Model):
    trabajador_ID = models.CharField(primary_key=True, max_length=8)
    trabajador_nombre = models.CharField(max_length=50, null=False)
    trabajador_apellido = models.CharField(max_length=50, null=False)
    trabajador_apellido2 = models.CharField(max_length=50, null=True)
    trabajador_activo = models.BooleanField(null=False)



class Visita(models.Model):
    visita_ID = models.AutoField(primary_key=True)
    visita_rut = models.CharField(max_length=8, null=False)
    visita_nombre = models.CharField(max_length=50, null=False)
    visita_apellido_1 = models.CharField(max_length=50, null=False)
    visita_apellido_2 = models.CharField(max_length=50, null=True)
    visita_observacion = models.CharField(max_length=200, null=True)
    visita_fecha_llegada = models.DateTimeField(null=False)
    visita_fecha_salida = models.DateTimeField(null=True)
    visita_activo = models.BooleanField(null=True)
    tipo_ID = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=False)
    empresa_ID = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    trabajador_ID = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=True)
    lugar_ID = models.ForeignKey(Lugar, on_delete=models.CASCADE, null=False)
    


class Alumno(models.Model):
    Alumno_RUT = models.CharField(primary_key=True, max_length=8)
    Alumno_Nombre = models.CharField(max_length=50, null=False)
    Alumno_Apellido_Pat=models.CharField(max_length=50, null=False)
    Alumno_Apellido_Mat=models.CharField(max_length=50, null=False)
    Alumno_Curso=models.CharField(max_length=10, null=False)
    Alumno_TEA=models.BooleanField(null=False)


class Apoderado(models.Model):
    Apoderado_RUT = models.CharField(primary_key=True, max_length=8)
    Apoderado_Nombre = models.CharField(max_length=50, null=False)
    Apoderado_Apellido_Pat=models.CharField(max_length=50, null=False)
    Apoderado_Apellido_Mat=models.CharField(max_length=50, null=False)
    Apoderado_Mail=models.CharField(max_length=50, null=False)
    Apoderado_Observacion = models.CharField(max_length=200, null=True)
    Apoderado_Activo=models.BooleanField(null=False)
    Hijo_1 = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='hijo1_set', null=True)
    Hijo_2 = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='hijo2_set', null=True)
    Hijo_3 = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='hijo3_set', null=True)


class Familia(models.Model):
    Familia_ID= models.AutoField(primary_key=True)
    Apoderado_RUT= models.CharField(max_length=8)
    Alumno_RUT= models.CharField(max_length=8)