from django.contrib import admin
from .models import QHSE, CSR, CSRMedia, Index, Capabilities, Contact, MediaCategory, Media, Career, CareerDetail, Experience, Partner, PartnersText, ProductSupplied, QHSECategory, ServicesRendered, ServicesMedia, Services, WhoWeAreHome, WhoWeAreAbout, WEDS, WSPS


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    search_fields = ['summary', 'created']
    list_display = ['summary', 'created']

@admin.register(WhoWeAreHome)
class WhoWeAreHomeAdmin(admin.ModelAdmin):
    search_fields = ['summary', 'created']
    list_display = ['summary', 'created']

@admin.register(WhoWeAreAbout)
class WhoWeAreAboutAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'summary', 'created']
    list_display = ['title', 'image', 'featured', 'created']

@admin.register(ServicesMedia)
class ServicesMediaAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'created']
    list_display = ['title', 'content', 'logo','image', 'created']

@admin.register(Capabilities)
class CapabilitiesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created']
    list_display = ['title', 'created']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'website', 'created']
    list_display = ['name', 'logo', 'website', 'created']

@admin.register(QHSECategory)
class QHSECategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created']
    list_display = ['title', 'created']
    
@admin.register(QHSE)
class QHSEAdmin(admin.ModelAdmin):
    search_fields = ['category', 'content', 'created']
    list_display = ['category', 'content', 'created']

@admin.register(CSR)
class CSRAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']
    
@admin.register(CSRMedia)
class CSRAdmin(admin.ModelAdmin):
    # search_fields = [ 'created']
    list_display = ['image', 'created']

@admin.register(ServicesRendered)
class ServicesRenderedAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']

@admin.register(PartnersText)
class PartnerTextAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created']
    list_display = ['title', 'summary', 'created']

@admin.register(ProductSupplied)
class ProductSuppliedAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']

@admin.register(WEDS)
class WEDSAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']

@admin.register(WSPS)
class WSPSAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'created']
    list_display = ['title', 'description', 'created']

@admin.register(Career)
class CareersAdmin(admin.ModelAdmin):
    search_fields = ['job_title', 'job_type', 'job_location' 'experience_level', 'created']
    list_display = ['job_title', 'job_type', 'job_location', 'experience_level', 'job_summary', 'job_requirement', 'created']

@admin.register(CareerDetail)
class CareerDetailAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'file']
    list_display = ['first_name', 'last_name', 'email', 'phone', 'file', 'message', 'created']

@admin.register(MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'created']
    list_display = ['title', 'created']
    
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['category', 'image', 'created']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	search_fields = ('full_name', 'email', 'subject')
	list_display = ('full_name','email', 'subject', 'message')