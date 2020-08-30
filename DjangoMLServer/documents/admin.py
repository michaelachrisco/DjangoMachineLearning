from django.contrib import admin
from django.apps import apps
from DjangoMLServer.settings import MY_APPS

# https://hackernoon.com/automatically-register-all-models-in-django-admin-django-tips-481382cf75e5
class BaseAdmin(object):
    def __init__(self, model, admin_site):
        super(BaseAdmin, self).__init__(model, admin_site)

    class Meta:
        fields = '__all__'


for my_app in MY_APPS:
    app = apps.get_app_config(my_app.split('.')[0])

    for my_model in app.models.items():
        admin_class = type('AdminClass', (BaseAdmin, admin.ModelAdmin), {})
        admin_class.list_display = [f.name for f in my_model[1]._meta.fields]
        admin_class.search_fields = ('id',)
        try:
            if not my_model[1]._meta.abstract and not my_model[1]._meta.auto_created:
                admin.site.register(my_model[1], admin_class)
        except admin.sites.AlreadyRegistered:
            pass


# Decorator function to re-register a model with a new ModelAdmin
# Should always be used in place of @admin.register()
# Example:
# from core.admin import re_register_model
# @re_register_model(SystemSettings)
# class TestAdmin(admin.ModelAdmin):
#     pass
def re_register_model(*models, site=None):
    def _model_admin_wrapper(new_admin_class):
        admin_site = site or admin.site
        admin_site.unregister(*models)
        admin_site.register(*models, admin_class=new_admin_class)

    return _model_admin_wrapper
