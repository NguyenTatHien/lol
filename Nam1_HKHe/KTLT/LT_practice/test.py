import os
def show_dir(path):
    direntry = os.scandir(path)
    for e in direntry:
        if e.is_file():
            print(f'File: {e.name}')
        elif e.is_dir():
            print(f'Directory: {e.name}')

    direntry.close()
    
show_dir(path = input("Nhập vào đường dẫn cần scan: "))