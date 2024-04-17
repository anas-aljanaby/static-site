import unittest

from textnode import  *
from inline_markdown import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", "bol")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", 'text')
        new_nodes = split_nodes_delimiter([node], "`", 'code')
        
        ans = [
         TextNode("This is text with a ", 'text'),
         TextNode("code block", 'code'),
         TextNode(" word", 'text'),
            ]
        self.assertEqual(new_nodes, ans)
    
    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", 'text')
        new_nodes = split_nodes_delimiter([node], "*", 'italic')
        self.assertListEqual(
            [
                TextNode("This is text with an ", 'text'),
                TextNode("italic", 'italic'),
                TextNode(" word", 'text'),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main() 

