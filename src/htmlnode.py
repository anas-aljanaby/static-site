class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ''
        pairs = [f' {k}="{v}"' for k, v in self.props.items()]

        return  ''.join(pairs)

    def __repr__(self):
        return f'''HTMLNode({self.tag},\n{self.value},\n{self.children},\n{self.props},'''

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have value.")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag was not provided")
        if not self.children:
            raise ValueError("children argument was not provided")

        html = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html += child.to_html()
        html += f'</{self.tag}>'
        return html

#node = ParentNode(
#    "p",
#    [
#        LeafNode("b", "Bold text"),
#        LeafNode(None, "Normal text"),
#        LeafNode("i", "italic text"),
#        LeafNode(None, "Normal text"),
#    ],
#)
#
#print(node.to_html())

# o = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})

#print(o.props_to_html())
#print(o.__repr__())



