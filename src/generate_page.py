from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line.lstrip('# ')
    raise ValueError('Markdown file must have an h1 header')


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    html_file =  markdown_to_html_node(markdown_content).to_html()
    
    title = extract_title(markdown_content)
    html_file = template.replace('{{ Title }}', title).replace('{{ Content }}', html_file)
    
    with open(dest_path, 'w') as f:
        f.write(html_file)
    





