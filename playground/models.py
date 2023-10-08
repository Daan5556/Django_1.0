from django.db import models

class FormSubmission1(models.Model):
    form_data = models.TextField()
    device_identifier = models.CharField(max_length=255)

class FormSubmission2(models.Model):
    form_data = models.TextField()
    device_identifier = models.CharField(max_length=255)