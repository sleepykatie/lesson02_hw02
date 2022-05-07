import os
import yaml


def dict_proc(current_dict, current_dict_path):

    for key in current_dict:
        # print('makedir', current_dict_path)
        os.makedirs(current_dict_path, exist_ok=True)
        element = current_dict[key]
        if type(element) == list:
            current_path = os.path.join(current_dict_path, key)
            os.makedirs(current_path, exist_ok=True)
            # print('makedir', current_path)
            list_proc(element, current_path)
        elif type(element) == dict:
            current_path = os.path.join(current_dict_path, key)
            dict_proc(element, current_path)


def list_proc(current_list, current_list_path):
    for el in current_list:
        if type(el) == dict:
            dict_proc(el, current_list_path)
        elif type(el) == str:
            # print('makefile', current_list_path)
            open(os.path.join(current_list_path, el), 'w').close()


if __name__ == '__main__':
    root_path = os.path.join(os.getcwd(), 'task2')
    os.makedirs(root_path, exist_ok=True)
    with open(os.path.join(root_path, 'config.yaml'), 'r') as f:
        # config = yaml.safe_load(f)
        # config = yaml.load(f, Loader=yaml.FullLoader)
        config = yaml.full_load(f)

    dict_proc(config, root_path)


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

