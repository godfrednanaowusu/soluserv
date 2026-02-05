from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import CSR, Index, WEDS, WSPS, Capabilities, Career, Experience, Media, MediaCategory, Partner, PartnersText, ProductSupplied, QHSECategory, ServicesRendered, Services, WhoWeAreAbout, WhoWeAreHome
from django.views import View
from django.contrib import messages
from .forms import ContactForm, CareerDetailForm, NewsLetterForm
from .utils import build_url, emailsender


class IndexView(View):
    template_index = 'index.html'

    def get(self, request):
        indexes = Index.objects.all()
        wwah = WhoWeAreHome.objects.all()
        services = Services.objects.filter(featured=True)
        capabilities = Capabilities.objects.all()
        partners = Partner.objects.all()
        return render(request, self.template_index, {
            'indexes': indexes,
            'wwahs': wwah,
            'services': services,
            'capabilities': capabilities,
            'partners': partners
        })

class WhoWeAreView(View):
    template_whoweare = 'whoweare.html'

    def get(self, request):
        wwaa = WhoWeAreAbout.objects.all()
        sevrend = ServicesRendered.objects.all()
        parttext = PartnersText.objects.all()
        products = ProductSupplied.objects.all()
        return render(request, self.template_whoweare, {
            'wwaas': wwaa,
            'sevrendz': sevrend,
            'parttexts': parttext,
            'productzs': products
        })

class CopStructureView(View):
    template_copstructure = 'cop-structure.html'

    def get(self, request):
        return render(request, self.template_copstructure, {})

class ExperienceView(View):
    template_experience = 'experience.html'

    def get(self, request):
        experiences = Experience.objects.all()
        return render(request, self.template_experience, {'experiences': experiences})

class QHSEView(View):
    template_qhse = 'qhse.html'

    def get(self, request):
        qhse_categories = QHSECategory.objects.all()
        policies = Media.objects.all()
        return render(request, self.template_qhse, {
            'categories': qhse_categories, 
            'policies': policies
        })

class CSRView(View):
    template_csr = 'csr.html'

    def get(self, request):
        csr_categories = CSR.objects.all()
        csr = CSR.objects.all()
        return render(request, self.template_csr, {
            'categories':csr_categories, 
            'csrs': csr
        })

class ServicesView(View):
    template_services = 'services.html'

    def get(self, request):
        # services = Services.objects.all().order_by('order_id')
        # for service in services:
        #     service.media_service = service.media_service.all().order_by('order_id')

        services = Services.objects.prefetch_related('media_service').all()  # Prefetch to optimize queries
    
        # Sort media_service for each service
        for service in services:
            service.sorted_media_service = service.media_service.all().order_by('order_id')  # Replace 'field_name' with the desired sort field
    

        weds = WEDS.objects.all()
        wsps = WSPS.objects.all()
        return render(request, self.template_services, {
            'services':services,
            'weds': weds,
            'wsps': wsps
        })

class CareersView(View):
    template_careers = 'careers.html'

    def get(self, request):
        careers = Career.objects.all()
        return render(request, self.template_careers, {'careers': careers})
    
class CareerDetailView(View):
    template_career_details = 'career-details.html'
    form_class = CareerDetailForm

    def get(self, request, identifier):
        try:
            career = Career.objects.get(identifier=identifier)
        except Career.DoesNotExist:
            career = None
        return render(request, self.template_career_details, {'career':career })
    
    def post(self, request, identifier):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            messages.success(request, 'Application Submitted Successfully')

            # Send Email
            try:
                email_subject = 'Contact Message Submitted'
                email_fromName = 'Soluserv Ghana Limited'
                email_fromAddr = 'info@soluservgh.com'
                email_toAddr = 'info@soluservgh.com'
                email_replyTo = instance.email
                email_message = f'<p><b>Fullname:</b> {instance.first_name} {instance.last_name}</p><p><b>Email Address:</b> {instance.email}</p><p><b>PhoneNumber:</b> {instance.phone}</p></p><p><b>Message:</b> {instance.message}</p>'

                resp = emailsender(subject=email_subject, fromName=email_fromName, fromAddr=email_fromAddr, toAddr=email_toAddr, replyTo=email_replyTo, message=email_message)
                print(resp)
            except Exception as e:
                print(f'Email Error due to: {e}')

            return HttpResponseRedirect(build_url('career_details', kwargs={'identifier':identifier}, params={'form': form}))
        else:
            messages.error(
                request, 'Application Submission Failed, ' + str(form.errors))
            return HttpResponseRedirect(build_url('career_details', kwargs={'identifier':identifier}, params={'form': form}))

class MediaView(View):
    template_media = 'media.html'

    def get(self, request):
        media_categories = MediaCategory.objects.all()
        medias = Media.objects.all()
        return render(request, self.template_media, {
            'categories':media_categories, 
            'medias': medias
        })

class ContactUsView(View):
    template_contactus = 'contact-us.html'
    form_class = ContactForm
    
    def get(self, request):
        return render(request, self.template_contactus, { })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            messages.success(request, 'Message Submitted Successfully')

            # Send Email
            try:
                email_subject = 'Contact Message Submitted'
                email_fromName = 'Soluserv Ghana Limited'
                email_fromAddr = 'info@soluservgh.com'
                email_toAddr = 'info@soluservgh.com'
                email_replyTo = instance.email
                email_message = f'<p><b>Fullname:</b> {instance.name}</p><p><b>Email Address:</b> {instance.email}</p><p><b>Subject:</b> {instance.subject}</p><p><b>Message:</b> {instance.message}</p>'

                emailsender(subject=email_subject, fromName=email_fromName, fromAddr=email_fromAddr, toAddr=email_toAddr, replyTo=email_replyTo, message=email_message)
            except Exception as e:
                print(f'Email Error due to: {e}')

            return HttpResponseRedirect(build_url('contactus', kwargs={}, params={}))
        else:
            messages.error(
                request, 'Message could not be submitted, ' + str(form.errors))
            return HttpResponseRedirect(build_url('contactus', kwargs={}, params={'form': form}))

class NewsLetterView(View):
    template_index = 'index.html'
    form_class = NewsLetterForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            messages.success(request, 'Newsletter Subscription Successful')

            try:
                email_subject = 'Newsletter Submitted'
                email_fromName = 'Soluserv Ghana Limited'
                email_formAddr = 'info@soluservgh.com'
                email_toAddr = 'info@soluservgh.com'
                email_replyTo = instance.email
                email_message = f'<p><b>Email Address:<b> {instance.email}'

                emailsender(subject=email_subject, fromName=email_fromName, fromAddr=email_formAddr, toAddr=email_toAddr, replyTo=email_replyTo, message=email_message)
            except Exception as e:
                print(f'Email Error due to: {e}')
            
            return HttpResponseRedirect(build_url('index', kwargs={}, params={}))
        else:
            messages.error(
                request, 'Newsletter Subscription Failed, ' + str(form.errors))
            return HttpResponseRedirect(build_url('index', kwargs={}, params={'form': form}))