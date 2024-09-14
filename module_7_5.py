from os import chdir, getcwd, walk, path
from time import strftime, localtime

directory = '.'
chdir(directory)
dir_spec = getcwd()
print(dir_spec)
for root, dirs, files in walk(directory):
    print (root)
    for f in files:
        f_path = path.join(root, f)
        print(f'   Файл {f_path}, время '
                  f'{strftime("%d.%m.%Y %H:%M", localtime(path.getmtime(f_path)))}'
                  f', размер  {path.getsize(f_path)}, родительская директория {path.dirname(f_path)}')


