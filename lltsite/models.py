from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel

from .formdata import countries, states, languages, occupations

class StoryPage(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    thumbnail_desc = models.CharField(
        max_length=160, default='more...', null=True, blank=True, )
    image = models.CharField(max_length=100, blank=True, default='icon.png',
                             verbose_name='Icon image file name')
    listing_rank = models.IntegerField(blank=True, default=0, help_text='default rank. higher the number, lower the rank')
    featured = models.BooleanField(blank=True, default=False)
    featured_rank = models.IntegerField(blank=True, default=0, help_text='higher the number, lower the rank')
    headline = models.BooleanField(default=False)
    headline_tag = models.CharField(
        max_length=512, blank=True, null=True, default='')
    # tags = generic.GenericRelation(TaggedItem)
    private = models.BooleanField(default=False, blank=True, help_text='checking this ON will require a user to login to view this story')
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('page_view', args=[str(self.id)])

    def __str__(self):
        return self.title


class Subscriber(TimeStampedModel):
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(max_length=254, blank=False)
    last_name = models.CharField(max_length=254, blank=False)
    country = models.CharField(max_length=254, blank=False, choices=countries)
    state = models.CharField(max_length=254, blank=True, choices=states)
    occupation = models.CharField(max_length=254, blank=True, choices=occupations)
    language_speak  = models.CharField(max_length=512, blank=True, choices=languages)
    language_teach  = models.CharField(max_length=512, blank=True,choices=languages)
    notifications_on = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class ImpactFactor(models.Model):
    current_factor = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return str(self.current_factor)
