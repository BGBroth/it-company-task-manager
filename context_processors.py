from django.conf import settings


def cfg_assets_root(request):

    return { 'ASSETS_ROOT' : "static" }
