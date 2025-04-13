from textnode import TextNode, TextType

# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)


# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    match delimiter:
        case '`':
            new_text_type=TextType.CODE
        case '_':
            new_text_type=TextType.ITALIC
        case '**':
            new_text_type=TextType.BOLD
        
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            base_text = old_nodes[0].text
            delimited = base_text.split(delimiter)
            if delimited == base_text:
                raise Exception("no delimiter found")
            
            text_node_list = []
            for i in range(0,len(delimited)):
                if i%2==0:
                    new_nodes.append(TextNode(delimited[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(delimited[i],new_text_type))
    
    print(new_nodes)
    return new_nodes

