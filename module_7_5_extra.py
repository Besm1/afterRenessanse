import os

print(os.getcwd())
print(os.listdir())

for i in os.walk('.'):
    print(i)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(files)
print(files[4].title())
os.startfile(files[4])
os.copy_file_range()