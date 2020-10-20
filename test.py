import os


i = 100
def read_path(path_name):
    global i
    for dir_item in os.listdir(path_name):
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):
            print(full_path)
            read_path(full_path)
        else:
            if dir_item.endswith('.jpg'):
                new_name = 'F:\\face&emotion_recognition\\others\\'+str(i)+'.jpg'
                os.rename(full_path, new_name)
        i = i+1

if __name__ == '__main__':
    read_path('./data')



