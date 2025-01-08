from django.core.mail import send_mail, EmailMessage
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_book.settings')
import django
django.setup()

# send_mail(
#     'Test Email',
#     'This is a test email from Django using an app password.',
#     'shrutishetty2003@gmail.com',
#     ['shrutispare2@gmail.com'],
#     fail_silently=False,
# )

email = EmailMessage(
    'MSG SENT USING DJANGO MODULE',
    'THIS IS A TEST MAIL SENT USING DJANGO i am sending my resume here',
    'shrutishetty2003@gmail.com',
    ['shrutispare2@gmail.com'],
)
email.attach_file("C:\\Users\\shrey\\Downloads\\Resume_Shruti_Karunakar_Shetty.pdf")
email.send()
