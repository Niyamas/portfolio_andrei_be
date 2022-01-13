from django.db import models
from django.utils.text import slugify
from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import (
  MultiFieldPanel,
  InlinePanel,
  FieldPanel,
  PageChooserPanel
)
from wagtail.api import APIField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from .serializers import TypeChoiceSerializer

class Links(Orderable):
  """
  Children of the Navigation model.
  """

  class LinkTypes(models.IntegerChoices):
    DEFAULT = 1, 'Default'
    ANCHOR_TAG = 2, 'Anchor tag'
    OPEN_IN_NEW_TAB = 3, 'Open in new tab'

  title = models.CharField(max_length=50, blank=False, null=True)
  page = models.ForeignKey('wagtailcore.Page', blank=True, null=True, related_name='+', on_delete=models.CASCADE)
  url = models.CharField(max_length=500, blank=True)
  link_type = models.PositiveSmallIntegerField(choices=LinkTypes.choices, default=LinkTypes.DEFAULT, null=False, blank=False)
  child_of = ParentalKey('Navigation', related_name='links')

  panels = [
    FieldPanel('title'),
    PageChooserPanel('page'),
    FieldPanel('url'),
    FieldPanel('link_type'),
  ]

  api_fields = [
    APIField('title'),
    APIField('page'),
    APIField('url'),
    APIField('link_type', serializer=TypeChoiceSerializer(choices=LinkTypes)),
  ]

class Navigation(ClusterableModel):
  """
  Can create navigation names like header menu & footer menu,
  and their corresponding links.
  """

  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True, blank=False, null=True)

  panels = [
    MultiFieldPanel([
      FieldPanel('title'),
      FieldPanel('slug'),
    ], heading='Navigation'),
    InlinePanel('links', label='Links')                    # Referenced in Link's page ParentalKey
  ]

  api_fields = [
    APIField('title'),
    APIField('slug'),
    APIField('links'),
  ]

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    super(Navigation, self).save(*args, **kwargs)

    self.slug = slugify(self.title, allow_unicode=True)
      
    return super(Navigation, self).save(*args, **kwargs)