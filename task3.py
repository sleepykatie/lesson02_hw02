import os
import yaml
import shutil


def dict_proc(current_dict, current_dict_path):

    for key in current_dict:
        os.makedirs(current_dict_path, exist_ok=True)
        element = current_dict[key]
        if type(element) == list:
            current_path = os.path.join(current_dict_path, key)
            os.makedirs(current_path, exist_ok=True)
            list_proc(element, current_path)
        elif type(element) == dict:
            current_path = os.path.join(current_dict_path, key)
            dict_proc(element, current_path)


def list_proc(current_list, current_list_path):
    for el in current_list:
        if type(el) == dict:
            dict_proc(el, current_list_path)
        elif type(el) == str:
            open(os.path.join(current_list_path, el), 'w').close()


if __name__ == '__main__':
    root_path = os.path.join(os.getcwd(), 'task3')
    os.makedirs(root_path, exist_ok=True)
    with open(os.path.join(root_path, 'config_temp.yaml'), 'r') as f:
        config = yaml.full_load(f)

    dict_proc(config, root_path)

    templates_path = os.path.join(os.getcwd(), 'task3', 'templates')
    os.makedirs(templates_path, exist_ok=True)
    for root, dirs_in_root, files_in_root in os.walk(os.path.join(root_path, 'my_project')):
        if root.__contains__('templates') and not root.__contains__('templates/'):
            # print(root)
            old_path = root
            shutil.copytree(old_path, templates_path, dirs_exist_ok=True)


'''
{'my_project': 
    {'settings': ['__init__.py', 'dev.py', 'prod.ru'], 
    'mainapp': ['__init__.py', 'models.py', 'views.py', 
        {'templates': [{'mainapp': ['base.html', 'index.html']}]}
        ], 
    'authapp': ['__init__.py', 'models.py', 'views.py', 
        {'templates': [{'authapp': ['base.html', 'index.html']}]}
        ]
        }
        }
'''