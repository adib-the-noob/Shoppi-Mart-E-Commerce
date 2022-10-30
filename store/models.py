from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ['-date_added',]

    def __str__(self):
        return self.title

    def get_absolute(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'https://ecommerc-web.herokuapp.com/' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'https://ecommerc-web.herokuapp.com' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_to = BytesIO()
        img.save(thumb_to, 'JPEG', quality=85)

        thumbnail = File(thumb_to, name=image.name)
        return thumbnail