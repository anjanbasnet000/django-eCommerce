from django.db import models

class Category(models.Model):
    STATUS=(
        ('true', 'True'),
        ('false', 'False'),
    )
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS=(
        ('published', 'Published'),
        ('draft', 'Draft'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  #many to one relation with Category
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    min_amount = models.IntegerField()
    detail = models.TextField()
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
