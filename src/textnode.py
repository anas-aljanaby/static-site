from htmlnode import LeafNode

text_type_text = 'text'
text_type_bold = 'bold'
text_type_italic = 'italic'
text_type_code = 'code'
text_type_image = 'image'
text_type_link = 'link'

class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == 'text':
      return LeafNode(tag=None, value=text_node.text)

    if text_node.text_type == 'bold':
        return LeafNode(tag='b', value=text_node.text)

    if text_node.text_type == 'italic':
        return LeafNode(tag='i', value=text_node.text)

    if text_node.text_type == 'code':
        return LeafNode(tag='code', value=text_node.text)

    if text_node.text_type == 'link':
        return LeafNode(tag='a', props={'href': text_node.url},
        value=text_node.text)

    if text_node.text_type == 'image':
        return LeafNode(tag='img', props={
        'src': text_node.url, 'alt': text_node.text},
        value='')

    raise ValueError(f"Invalid text type: {text_node.text_type}")







