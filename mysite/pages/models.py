from django.db import models

# Create your models here.

class TypeCategory(models.Model):

    name = models.CharField('Category Type name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TypeCategory'
        verbose_name_plural = 'TypeCategories'


class NoutCategory(models.Model):
    typecategory = models.ForeignKey(TypeCategory, on_delete=models.CASCADE, related_name='nout_type')
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NoutCategory'
        verbose_name_plural = 'NoutCategories'


class Notebook(models.Model):

    noutcategory = models.ForeignKey(NoutCategory, on_delete=models.CASCADE, related_name='nout_model')
    name = models.CharField('Nout name', max_length=50)
    price = models.FloatField('Nout price', blank=True)
    img = models.ImageField('Nout image', upload_to='media_images')
    video = models.FileField('Nout video', upload_to='media_videos')
    slug = models.SlugField('Nout slug', unique=True)
    email = models.EmailField('Nout email')
    link = models.URLField('Nout link')
    boolean = models.BooleanField('Nout bool')
    date = models.DateTimeField('Nout update date', auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'
        ordering = ['price']
