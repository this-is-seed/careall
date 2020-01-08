from django.apps import AppConfig


class PoolsConfig(AppConfig):
    name = 'pools'

    def apps(self):
    	import pools.signals
