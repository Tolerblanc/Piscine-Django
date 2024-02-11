import sys
import os
import re


def load_settings():
    '''Load settings from settings.py'''
    import settings
    return {k: getattr(settings, k) for k in dir(settings) if not k.startswith("__")}


def render_template(template_path, context):
    with open(template_path, 'r') as file:
        content = file.read()

    for key, value in context.items():
        content = re.sub(f"{{ {key} }}", str(value), content)

    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <template_file>")
        sys.exit(1)

    template_path = sys.argv[1]
    if not template_path.endswith('.template'):
        print("Error: File must have a '.template' extension.")
        sys.exit(1)

    if not os.path.exists(template_path):
        print(f"Error: The file {template_path} does not exist.")
        sys.exit(1)

    settings = load_settings()

    content = render_template(template_path, settings)
    content = f'''<html>
<head><title>My CV</title></head>
<body>
{content}
</body>
</html>'''

    result_path = template_path.replace('.template', '.html')
    with open(result_path, 'w') as file:
        file.write(content)
    print(f"The {result_path} has been created.")


if __name__ == "__main__":
    main()
    # TODO : fix template file
