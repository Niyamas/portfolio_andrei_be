"""
Register Navigation Snippets Wagtail API Endpoint.

WIP @todo: Add a functional navigations API endpoint to display header and footer CMS items.

See:
https://www.google.com/search?q=wagtail+BaseAPIEndpoint&ei=C6nkYKKpMd2sqtsPjN65qAs&oq=wagtail+BaseAPIEndpoint&gs_lcp=Cgdnd3Mtd2l6EAMyBwghEAoQoAEyBQghEKsCOgcIABBHELADOgcIABCwAxBDOgoILhCwAxDIAxBDOgQIABBDOgQILhBDOgIIAEoFCDgSATFKBAhBGABQzQlYmgtgmw1oAnACeACAAWiIAbICkgEDMS4ymAEAoAEBoAECqgEHZ3dzLXdpesgBDcABAQ&sclient=gws-wiz&ved=0ahUKEwji2sGjkc_xAhVdlmoFHQxvDrUQ4dUDCA8&uact=5
https://stackoverflow.com/questions/51961999/wagtail-api-how-to-expose-snippets
https://github.com/wagtail/wagtail/tree/main/wagtail/api/v2
"""

from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.serializers import BaseSerializer

from .models import Navigation


class NavigationsAPIViewset (BaseAPIViewSet):
    model = Navigation

    #body_fields = ['id', 'title',]