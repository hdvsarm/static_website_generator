import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


class TestInline(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a `text` node", TextType.TEXT)
        node_split = split_nodes_delimiter([node], "`", text_type=TextType.CODE)
        self.assertEqual(node_split, [TextNode("This is a ", TextType.TEXT), TextNode("text", TextType.CODE), TextNode(" node", TextType.TEXT)])

    def test_text_fail(self):
        node = TextNode("This is a `text` node", TextType.CODE) ##requires old node to be text type of text
        node_split = split_nodes_delimiter([node], "`", text_type=TextType.CODE)
        self.assertEqual(node_split, [TextNode("This is a `text` node", TextType.CODE)])

    def test_bold(self):
        node = TextNode("This is a **text** node", TextType.TEXT)
        node_split = split_nodes_delimiter([node], "**", text_type=TextType.BOLD)
        self.assertEqual(node_split, [TextNode("This is a ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" node", TextType.TEXT)])

    def test_delimit_fail(self):
        node = TextNode("This is a _text_ node", TextType.TEXT)
        node_split = split_nodes_delimiter([node], "z", text_type=TextType.BOLD)
        self.assertRaises(Exception, node_split)

if __name__ == "__main__":
    unittest.main()