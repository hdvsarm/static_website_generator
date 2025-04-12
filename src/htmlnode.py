class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        running_string=""
        if self.props==None:
            return ""
        for i in self.props:
            running_string=running_string+' '+f"{i}='{self.props[i]}'"
        return running_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value==None:
            raise ValueError
        if self.tag==None:
            return self.value
        

        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"