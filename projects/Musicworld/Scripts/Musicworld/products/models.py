from django.db import models

class products(models.Model):
    name = models.CharField('producto', max_length=100)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Stock')
    description = models.TextField(verbose_name='Descripción')
    #image = models.ImageField(verbose_name='Imagen', upload_to='products/images')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    state = models.BooleanField(verbose_name='Disponible', default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'product'
        ordering = ['id']
    class violin(models.Model):
    name = models.CharField('violin', max_length=150)
    description = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.name,drescription

    class Meta:
        verbose_name = 'Violin'
	      verbose_name_plural = 'Violines'
	      db_table = 'violin'
	      ordering = ['id']
    class trumpet(models.Model): 
    name = models.CharField('trompeta', max_length=100)
    description = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.name,description

    class Meta:
        verbose_name = 'Trompeta'
	      verbose_name_plural = 'Trompeta'
	      db_table = 'trumpet'
	      ordering = ['id']
    class keyboard(models.Model):
    name = models.CharField('piano', max_length=100)
    description = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.name,description

    class Meta:
        verbose_name = 'Piano'
	      verbose_name_plural = 'Piano'
	      db_table = 'keyboard'
	      ordering = ['id']