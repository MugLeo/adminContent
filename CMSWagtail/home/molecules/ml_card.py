from wagtail.api import APIField
from wagtail.core import blocks

def get_styles():
  return [('test-style','test'),('default-style','default'),]

class MlCard(blocks.StructBlock):
    # Requires
    title_text = blocks.TextBlock(required=True, help_text='Title text')
    body_text = blocks.TextBlock(required=True, help_text='Main text')
    # Optionals
    style = blocks.ChoiceBlock(choices=get_styles, required=False)

    image = blocks.URLBlock(required=False, help_text='Image')
    footer_text = blocks.TextBlock(required=False, help_text='Footer text')

    class Meta:
        icon = "snippet"
        label = "Ml Card"

    api_fields = [
        APIField('title'),
        APIField('image'),
        APIField('body'),
        APIField('footer'),
        APIField('style'),
    ]
