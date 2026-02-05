from django.db import models
from tinymce.models import HTMLField
from .validators import *
from django.utils import timezone
import uuid

class Index(models.Model):
    summary = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.summary

class WhoWeAreHome(models.Model):
    summary = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.summary

class Partner(models.Model):
    name = models.CharField(max_length=100, default='')
    logo = models.ImageField(upload_to='partners_images')
    website = models.URLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class WhoWeAreAbout(models.Model):
    title = models.CharField(max_length=50, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description

class QHSECategory(models.Model):
    title = models.CharField(max_length=50, default='')
    unique_name = models.CharField(max_length=200, default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

class QHSE(models.Model):
    category = models.ForeignKey(QHSECategory, related_name="category_policy", null=True, blank=True, on_delete=models.SET_NULL)
    content = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.category} - {self.created}'

class CSR(models.Model):
    title = models.CharField(max_length=50, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'
    
class CSRMedia(models.Model):
    category = models.ForeignKey(CSR, related_name="category_csr", null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='csr_images')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.category} - {self.created}'

# class CSR(models.Model):
#     title = models.CharField(max_length=100, default='')
#     description = HTMLField(default='')
#     image = models.ImageField(upload_to='csr_images')
#     created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=100, default='')
    home_text = models.CharField(max_length=200, null=True, blank=True, default='')
    summary = HTMLField(default='', null=True, blank=True)
    image = models.ImageField(upload_to='gallery_images', null=True, blank=True)
    unique_name = models.CharField(max_length=200, default='')
    background_color = models.CharField(max_length=10, default='',null=True, blank=True)
    text_color = models.CharField(max_length=10, default='',null=True, blank=True) 
    order_id = models.IntegerField(default=0,null=True, blank=True)    
    featured = models.BooleanField(blank=True,  default=True)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
class ServicesMedia(models.Model):
    service = models.ForeignKey(Services, related_name="media_service", null=True, blank=True, on_delete=models.SET_NULL)
    logo = models.ImageField(upload_to='services_media', null=True, blank=True)
    title = models.CharField(max_length=50, default='')
    content = HTMLField(default='')
    image = models.ImageField(upload_to='services_media', null=True, blank=True)
    order_id = models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

class Capabilities(models.Model):
    title = models.CharField(max_length=100, default='')
    # image = models.ImageField(upload_to='capabilities_images')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ServicesRendered(models.Model):
    title = models.CharField(max_length=50, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class PartnersText(models.Model):
    title = models.CharField(max_length=100, default='')
    summary = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ProductSupplied(models.Model):
    title = models.CharField(max_length=50, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=50, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class WEDS(models.Model):
    title = models.CharField(max_length=100, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class WSPS(models.Model):
    title = models.CharField(max_length=100, default='')
    description = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Career(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4)
    job_title = models.CharField(max_length=50, default='')
    job_type = models.CharField(max_length=50, default='')
    job_location = models.CharField(max_length=50, default='')
    experience_level = models.CharField(max_length=50, default='')
    job_summary = models.CharField(max_length=100, default='')
    job_requirement = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title

class CareerDetail(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=255, blank=True, null=True, default='',)
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Phone Number' )
    file = models.FileField(upload_to='job_applications', default='', validators=[validate_file_size])
    message = HTMLField(default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name
    
class MediaCategory(models.Model):
    title = models.CharField(max_length=50, default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'
    
class Media(models.Model):
    category = models.ForeignKey(MediaCategory, related_name="category_media", null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='media_images')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.category} - {self.created}'
    
class Contact(models.Model):
    full_name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=254, default='')
    subject = models.CharField(max_length=200, default='')
    message = models.TextField(default='')
    
    def __str__(self):
        return self.full_name
    
class NewsLetter(models.Model):
    class Meta:
        verbose_name_plural = "NewsLetters"
        
    email = models.EmailField(max_length=254, default='')
    active = models.BooleanField(blank=True,  default=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email