import os

directory = '.'
abs_path = os.path.abspath(directory)
print(os.path.join(abs_path, 'dirrrr'))
for dir_content in os.walk(directory):
    dir_name = dir_content[0]
    print(f'Папка {os.path.join(abs_path, dir_name[2:])}')
    for f in [f_ for f_ in os.listdir() if os.path.isfile(f_)]:
        print('   ', f.title(), f.path.getmtime())



