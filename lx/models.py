from django.db import models

class Contract(models.Model):
    contract_name = models.CharField(max_length=100)

    def __str__(self):
        return self.contract_name
