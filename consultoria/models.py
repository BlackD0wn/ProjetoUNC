from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    priceType = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O número deve estar no seguinte formato: '+999999999'. São permitidos até 15 digitos.")

    name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()
    text = models.TextField()
    # shit implementation, but works
    service = models.ForeignKey(Service, on_delete="CASCADE",null=True, blank=True)

    STATUS_CHOICES = (
        ("NOVO", "Novo"),
        ("CONTATO FEITO", "Realizado contato"),
        ("ACEITO", "Aceito"),
        ("RECUSADO", "Recusado"),
    )

    status = models.CharField(max_length=30,
                      choices=STATUS_CHOICES,
                      default="NOVO")


    def __str__(self):
        return self.name + ' | ' + self.status
