from wagtail.core import blocks

class RichTextBlock(blocks.RichTextBlock):
    """Richtext with Draftail features."""

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full Rich Text'

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold', 'italic',
            'h2', 'h3', 'h4',
            'superscript', 'subscript',
            'center',
            'ol', 'ul', 'hr',
            'link', 'document-link', 'image', 'embed',
            'code',
            'redo', 'undo',
        ]

class TextImageBlock(blocks.StructBlock):
    pass

class FloatingCardsBlock(blocks.StructBlock):
    pass

class ContactBlock(blocks.StructBlock):
    pass

class ServicesBlock(blocks.StructBlock):
    pass

class ImageTextBlock(blocks.StructBlock):
    pass

class ImageGalleryBlock(blocks.StructBlock):
    """Inspo:
        - https://www.lenasteinkuehler.com/

    Args:
        blocks ([type]): [description]
    """
    pass

class ImageSliderBlock(blocks.StructBlock):
    """Inspo:
        - https://www.tsakhi.com/sax

    Args:
        blocks ([type]): [description]
    """
    pass