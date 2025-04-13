from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italics"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):

        # TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
        # TextType.BOLD: This should return a LeafNode with a "b" tag and the text
        # TextType.ITALIC: "i" tag, text
        # TextType.CODE: "code" tag, text
        # TextType.LINK: "a" tag, anchor text, and "href" prop
        # TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)

    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
        
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
        
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, prop={"href": text_node.url})
        
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props= {"src": text_node.url, "alt": text_node.text})

        
