from django.db import models

# Create your models here.
class mantencion(models.Model):
    idmantencion = models.AutoField(primary_key=True)
    idticket = models.ForeignKey('tickets.ticket', on_delete=models.RESTRICT, null=True, blank=True, db_column='idticket')
    descripcion = models.TextField(max_length=1000)
    estado = models.CharField(max_length=20, default='Pendiente')
    observaciones = models.TextField(max_length=1000, null=True, blank=True)
    fechainicio = models.DateTimeField(auto_now_add=True)
    fechatermino = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'mantencion'
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.descripcion