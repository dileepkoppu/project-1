from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.core.mail import send_mail
from django.db.models.signals import post_save



class Kid(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    parent_phone_number = models.CharField(max_length=10)
    parent_email_address = models.EmailField()

    def __str__(self) -> str:
        return self.name



class Image(models.Model):

    food_groups=[
        ('Veg','Veg'),
        ('Fruit','Fruit'),
        ('Grain','Grain'),
        ('Protein','Protein'),
        ('Dairy','Dairy'),
        ('Confectionery','Confectionery'),
        ('Unknown','Unknown')
    ]

    kid_name= models.ForeignKey(Kid,on_delete=models.CASCADE)
    image = models.URLField()
    @property
    def image_preview(self):
        return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image))

    food_group = models.CharField(choices=food_groups,max_length=20)
    is_Approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=40)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now_add=True)


def post_user_created_signal(sender, instance, created, **kwargs):
    if instance.food_group=='Unknown':
        sender_mail='anjanidileepkoppu@gmail.com'
        if not settings.DEBUG:
            sender_mail=settings.EMAIL_HOST_USER

        send_mail(
            'Welcome',
            'Good Morning have a nice day',
            sender_mail,
            [instance.kid_name.parent_email_address,]
        )

post_save.connect(post_user_created_signal, sender=Image)