import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Hello, world!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href='https://www.google.com'>Hello, world!</a>")




if __name__ == "__main__":
    unittest.main()