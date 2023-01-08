from wagtail.api import APIField
from wagtail.core import blocks
from wagtail.fields import StreamField
from ..molecules.ml_card import MlCard

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