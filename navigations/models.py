from django.db import models
from django.utils.text import slugify
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
  MultiFieldPanel,
  InlinePanel,
  FieldPanel,
  PageChooserPanel
)


class Links(Orderable):

  class LinkTypes(models.TextChoices):
    DEFAULT = 1, 'Default'
    OPEN_IN_NEW_TAB = 2, 'Open in new tab'
    ANCHOR_TAG = 3, 'Anchor tag'

  title = models.CharField(max_length=50, blank=False, null=True)
  page = models.ForeignKey('wagtailcore.Page', blank=True, null=True, related_name='+', on_delete=models.CASCADE)
  url = models.CharField(max_length=500, blank=True)
  type = models.PositiveSmallIntegerField(choices=LinkTypes.choices, default=LinkTypes.DEFAULT, null=False, blank=False)
  child_of = ParentalKey('Navigation', related_name='links')

  panels = [
    FieldPanel('title'),
    PageChooserPanel('page'),
    FieldPanel('url'),
    FieldPanel('type'),
  ]


class Navigation(ClusterableModel):
  """The main menu clusterable model."""

  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True, blank=False, null=True)

  panels = [
    MultiFieldPanel([
      FieldPanel('title'),
      FieldPanel('slug'),
    ], heading='Navigation'),
    InlinePanel('links', label='Links')                    # Referenced in Link's page ParentalKey
  ]

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    super(Navigation, self).save(*args, **kwargs)

    self.slug = slugify(self.title, allow_unicode=True)
      
    return super(Navigation, self).save(*args, **kwargs)