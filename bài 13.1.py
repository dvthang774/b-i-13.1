import os
import os
# tao thu muc moi
os.mkdir("thu_muc_moi")
# xoa thu muc hien tai
os.rmdir('ten_thu_muc')
# Lenh nay se cung cap vi tri thu muc hien tai
os.getcwd()
#############Đọc tất cả thư mục và tập tin rồi in ra màn hình
for root, dirs,files in os.walk("E:\\"):
    print(root)
    print(dirs)
    print(files)
###########################################Đọc tập tin và đưa vào danh sách
lst1, lst2 = [], []
for root, dirs, files in os.walk('e:\\'):
    for name in files:
        f = (os.path.join(name))
        lst1.append(f)

    for name in dirs:
        t = (os.path.join(name))
        lst2.append(t)
print("danh sánh file:\n ", lst1,              end='\n')
print("danh sánh thư mục:\n ", lst2)#####