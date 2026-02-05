from urllib.parse import urlencode
from django.template.defaultfilters import slugify
from django.core.mail import EmailMessage
from django.urls import reverse


def build_url(*args, **kwargs):
    params = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)
    if params:
        url += '?' + urlencode(params)
    return url

def emailsender(*args, **kwargs):
    try:
        # print(f'kwargs: {kwargs}')
        subject = kwargs['subject']
        message = kwargs['message']
        fromAddr = kwargs['fromAddr']
        fromName = kwargs['fromName']
        toAddr = [kwargs['toAddr']]
        replyTo = kwargs['replyTo']

        html_message = f'<div style="">{message}</div>'

        email = EmailMessage(subject=subject, body=html_message,
                             from_email=f'{fromName} <{fromAddr}>', to=toAddr, headers={'Reply-To': replyTo})
        email.content_subtype = "html"  # Main content is now text/html
        data = email.send()

        return True

    except Exception as e:
        print(f'Email Error: {e}')
        return False
        return 'Error is ' + str(e)