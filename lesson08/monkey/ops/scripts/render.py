import os
import jinja2

def get_data_from_db():
    #((), ())
    data = {'content' : [
                {'name': 'm1', 'age' : 20},
                {'name': 'm2', 'age' : 21},
                {'name': 'm3', 'age' : 22},
                {'name': 'm4', 'age' : 23},
            ]
    }
    return data

def renderHtml(data):
    TemplateLoader = jinja2.FileSystemLoader(os.path.abspath('.'))
    TemplateEnv = jinja2.Environment(loader=TemplateLoader)
    template = TemplateEnv.get_template('reboot-users.html')
    htmlString = template.render(data)  # must -> dict
    print(htmlString)
    return htmlString

def main():
    data = get_data_from_db()
    renderHtml(data)


main()