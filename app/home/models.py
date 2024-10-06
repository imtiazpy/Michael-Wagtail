from django.db import models
from wagtail_tag_manager.mixins import TagMixin

from wagtail.models import Page


class HomePage(TagMixin, Page):
    pass
