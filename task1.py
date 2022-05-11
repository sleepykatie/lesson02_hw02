import os

# print(os.getcwd())
root_path = os.path.join(os.getcwd(), 'task1')
os.makedirs(root_path, exist_ok=True)
# print(root_path)


def start_project(*project_dirs):

    os.makedirs(os.path.join(root_path, 'my_project'), exist_ok=True)
    dir_list = [*project_dirs]
    for project_dir in dir_list:
        os.makedirs(os.path.join(root_path, 'my_project', project_dir), exist_ok=True)


if __name__ == '__main__':

    start_project('settings', 'mainapp', 'adminapp', 'authapp')
