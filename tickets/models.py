from django.db import models

# Create your models here.
class ticket(models.Model):
    idticket = models.AutoField(primary_key=True)
    idasignacion = models.IntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    prioridad = models.CharField(max_length=20, default='Media')
    estado = models.CharField(max_length=20, default='Pendiente')
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechacierre = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ticket'
        managed = True

    def __str__(self):
        return self.titulo