from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from .organisms.or_column_container import OrColumnContainer,GridContainer
from .molecules.ml_card import MlCard


class HomePage(Page):
    """ 
    TODO: change this for get any organisms.
    The correct structure should be:
    Page <- Header
    Page <- Slider or Banner
    Page <- [ ColumnContainer <- [ Cards ] ]
    Page <- Footer
    """
    # header = OrHeader()
    # footer = OrFooter()

    body = StreamField([
        ('or_column_container', OrColumnContainer()),
        ('grid_container', GridContainer()),
        # ('or_banner', OrBanner())
        # ('or_slider', OrSlider())
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    api_fields = [
        APIField('body'),
   ]
