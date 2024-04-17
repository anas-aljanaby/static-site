import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode(
         props={"href": "https://www.google.com", "target": "_blank"}
                )
        html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(htmlnode.props_to_html(), 
                         html)
        
    def test_to_html(self):
        test_cases = {
            LeafNode("p", "This is a paragraph of text.").to_html():
            '<p>This is a paragraph of text.</p>',
            LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html():
            '<a href="https://www.google.com">Click me!</a>'     
        }
        for test_case in test_cases.items():
            self.assertEqual(test_case[0], test_case[1])
            
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__=='__main__':
    unittest.main()
                         
