import html2image
from jinja2 import Template

hti = html2image.Html2Image()

def get_html(message: str, time: str, avatar: str):
    with open("template/index.html") as file:
        t = Template(file.read())
        t2 = t.render(message = message, time = time, avatar = avatar)
        return t2

def get_screen(message: str, time: str, avatar: str = None):
    hti.load_file('template/style.css')
    path = hti.screenshot(html_str = get_html(message, time, avatar), size=(530, 500))
                                                    # screen non fixed      , 150
    return open(path[0], "rb")