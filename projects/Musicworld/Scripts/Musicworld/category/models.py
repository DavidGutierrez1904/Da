from django.db import models

class category(models.Model):
    name = models.CharField('categoria', max_length=100)
    description = models.TextField(verbose_name='Descripción')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoy'
        ordering = ['id']
        
    class percussion(models.Model):
    name = models.CharField('percusion',max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Percusion'
	      verbose_name_plural = 'Percusiones'
	      db_table = 'percussion'
	      ordering = ['id']
          
    class wind(models.Model):
    name = models.CharField('Percusion',max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Viento'
	      verbose_name_plural = 'Vientos'
	      db_table = 'wind'
	      ordering = ['id']