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

class Size(blocks.StructBlock):
    value = blocks.IntegerBlock(required=False, min_value=1)
    unit_type = blocks.ChoiceBlock(choices=get_size, required=False)

    class Meta:
        icon = "snippet"
        label = "Size"

    api_fields = [
        APIField('unit_type'),
        APIField('value'),
    ]

class GridContainer(blocks.StructBlock):
    items = blocks.IntegerBlock(required=False, min_value=1)

    column = blocks.StreamBlock([
        ('column', Size()),
    ], blank=True, use_json_field=True)

    column_gap = blocks.StreamBlock([
        ('column_gap', Size()),
    ], blank=True, use_json_field=True, max_num=1)

    row = blocks.StreamBlock([
        ('row', Size()),
    ], blank=True, use_json_field=True)

    row_gap = blocks.StreamBlock([
        ('row_gap', Size()),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('items'),
        FieldPanel('column'),
        FieldPanel('column_gap'),
        FieldPanel('row'),
        FieldPanel('row_gap'),
    ]

    api_fields = [
        APIField('items'),
        APIField('column'),
        APIField('column_gap'),
        APIField('row'),
        APIField('row_gap'),
   ]
