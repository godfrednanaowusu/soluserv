from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from .views import IndexView, NewsLetterView, WhoWeAreView, CopStructureView, ExperienceView, QHSEView, ServicesView, CareersView, CareerDetailView, MediaView, ContactUsView, CSRView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('who-we-are/', WhoWeAreView.as_view(), name='who_we_are'),
    path('cop-structure/', CopStructureView.as_view(), name='cop_structure'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('cop-structure/', CopStructureView.as_view(), name='copstructure'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('qhse/', QHSEView.as_view(), name='qhse'),
    path('csr/', CSRView.as_view(), name='csr'),
    path('services', ServicesView.as_view(), name='services'),
    path('careers/', CareersView.as_view(), name='careers'),
    path('careers/<uuid:identifier>', CareerDetailView.as_view(), name='career_details'),
    path('our-media/', MediaView.as_view(), name='media'),
    path('contact-us/', ContactUsView.as_view(), name='contactus'),
    path('newsletter/', NewsLetterView.as_view(), name='newsletter'),
]
