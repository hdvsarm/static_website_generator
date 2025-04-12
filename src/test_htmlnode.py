import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        props = {"href": "https://www.google.com"}
        node = HTMLNode("<p>", "this is test text", children=None, props=props)
        self.assertEqual(
            "HTMLNode(tag=<p>, value=this is test text, children=None, props={'href': 'https://www.google.com'})", repr(node))
    
    def test_prop(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode("<p>", "this is test text", children=None, props=props)
        self.assertEqual(
            " href='https://www.google.com' target='_blank'", node.props_to_html())
        
    def test_children(self):
        props = {"href": "https://www.google.com"}
        node = HTMLNode("<p>", "this is test text", children=HTMLNode("<b>","bold text", children=None, props=None), props=props)
        self.assertEqual(
            "HTMLNode(tag=<p>, value=this is test text, children=HTMLNode(tag=<b>, value=bold text, children=None, props=None), props={'href': 'https://www.google.com'})", repr(node))


if __name__ == "__main__":
    unittest.main()