from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    max_count = 1
    parent_page_types = ['wagtailcore.page']
    subpage_types = []

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank=False,
        on_delete = models.SET_NULL,
        related_name = '+',
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image')
    ]