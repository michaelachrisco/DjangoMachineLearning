from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        # using .format for backward compatibility
        verbose_name = f'VERBOSE NOT SET {__name__}'
        verbose_name_plural = f'VERBOSE PLURAL NOT SET {__name__}'
        abstract = True

class Document(BaseModel):
    text_contents = models.TextField()

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'