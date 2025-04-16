from textnode import TextNode, TextType, extract_markdown_links, extract_markdown_images
import re

# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)


# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if delimiter == '`':
        new_text_type = TextType.CODE
    elif delimiter == '_':
        new_text_type = TextType.ITALIC
    elif delimiter == '**':
        new_text_type = TextType.BOLD
    else:
        return old_nodes  # unknown delimiter

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    if part:
                        new_nodes.append(TextNode(part, new_text_type))
    return new_nodes
    
    print(new_nodes)
    return new_nodes

node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

def split_nodes_image(old_nodes):
    new_nodes = []
    image_pattern = r'!\[([^\]]+)\]\s*\(([^)]+)\)'

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(image_pattern, text))

        if not matches:
            new_nodes.append(node)
            continue

        prev_index = 0
        for match in matches:
            start, end = match.span()
            alt_text, url = match.groups()

            # Add preceding text if any
            if start > prev_index:
                new_nodes.append(TextNode(text[prev_index:start], TextType.TEXT))
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
            prev_index = end

        # Add remaining text after last match
        if prev_index < len(text):
            new_nodes.append(TextNode(text[prev_index:], TextType.TEXT))

    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        text = node.text
        curr_index = 0
        for link_text, url in links:
            start_token = f"[{link_text}]({url})"
            start = text.find(start_token, curr_index)
            if start > curr_index:
                new_nodes.append(TextNode(text[curr_index:start], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
            curr_index = start + len(start_token)
        
        if curr_index < len(text):
            new_nodes.append(TextNode(text[curr_index:], TextType.TEXT))
    return new_nodes
        
# node= "This is **text** with an _italic_ word and a `code block` and an ![obi wan image] (https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


def text_to_textnodes(text):
    old_node = [TextNode(text, TextType.TEXT)]
    new_nodes1 = split_nodes_delimiter(old_node, "**", TextType.BOLD)
    new_nodes2 = split_nodes_delimiter(new_nodes1, "_", TextType.ITALIC)
    new_nodes3 = split_nodes_delimiter(new_nodes2, "`", TextType.CODE)
    new_nodes4 = split_nodes_image(new_nodes3)
    new_nodes5 = split_nodes_link(new_nodes4)

    return new_nodes5


markdown  = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """







# print(markdown_to_blocks(markdown))