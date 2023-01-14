from wagtail.api import APIField
from wagtail.core import blocks
from wagtail.fields import StreamField
from ..molecules.ml_card import MlCard
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
class OrColumnContainer(blocks.StructBlock):
    title = blocks.TextBlock(required=False, max_length=30)
    elements = blocks.StreamBlock([
        ('ml_card', MlCard()),
    ], blank=True, use_json_field=True)

    class Meta:
        icon = "snippet"
        label = "Column Container"

    api_fields = [
        APIField('elements'),
        APIField('title'),
    ]

def get_size():
  return [('px','px'),('fr','fr'),]

class Column(blocks.StructBlock):
    size = blocks.IntegerBlock(required=False, min_value=1)
    unit_type = blocks.ChoiceBlock(choices=get_size, required=False)

    class Meta:
        icon = "snippet"
        label = "Column"

    api_fields = [
        APIField('size'),
        APIField('unit_type'),
    ]

class Row(blocks.StructBlock):
    size = blocks.IntegerBlock(required=False, min_value=1)
    unit_type = blocks.ChoiceBlock(choices=get_size, required=False)

    class Meta:
        icon = "snippet"
        label = "Row"

    api_fields = [
        APIField('size'),
        APIField('unit_type'),
    ]

class GridContainer(blocks.StructBlock):
    items = blocks.IntegerBlock(required=False, min_value=1)

    column = blocks.StreamBlock([
        ('column', Column()),
    ], blank=True, use_json_field=True)

    row = blocks.StreamBlock([
        ('row', Row()),
    ], blank=True, use_json_field=True)


    content_panels = Page.content_panels + [
        FieldPanel('items'),
        FieldPanel('column'),
        FieldPanel('row')
    ]

    api_fields = [
        APIField('items'),
        APIField('column'),
        APIField('row'),
   ]
