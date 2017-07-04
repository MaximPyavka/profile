from django.conf import settings


def some_context_processor(request):
    return {
        'SETTINGS': settings,
    }
