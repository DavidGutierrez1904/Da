from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name = 'Nombre', max_length=100)
    description = models.TextField(verbose_name = 'Descripción', max_length=500)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Category'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(verbose_name = 'Producto', max_length=100)
    price = models.DecimalField(verbose_name = 'Precio', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name = 'Inventario')
    description = models.TextField(verbose_name = 'Descripción', max_length=500)
    state = models.BooleanField(verbose_name = 'Estado', max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #category = models.ManyToManyField(Category, verbose_name='Categoria')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Product'
        ordering = ['id']