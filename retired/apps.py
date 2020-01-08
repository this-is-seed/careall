from django.apps import AppConfig


class RetiredConfig(AppConfig):
    name = 'retired'

    def apps(self):
    	import retired.signals