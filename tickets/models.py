from django.db import models
from django.utils import timezone
from django.conf import settings


class ticket(models.Model):
    idticket = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    prioridad = models.CharField(max_length=20, default='Media')
    estado = models.CharField(max_length=20, default='Abierto')
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechacierre = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='tickets', null=True, blank=True)
    
    class Meta:
        db_table = 'ticket'
        managed = True
        default_permissions = ('add', 'change', 'delete', 'view')

    def eliminar_logico(self):
        if self.estado != 'Cerrado':
            self.estado = 'Cerrado'
            self.fechacierre = timezone.now()
            self.save(update_fields=['estado', 'fechacierre'])
        return self

    def __str__(self):
        return self.titulo