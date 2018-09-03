from django.apps import AppConfig


class ClassroomConfig(AppConfig):
    name = 'randomizer'

    def ready(self):
        import randomizer.signals
