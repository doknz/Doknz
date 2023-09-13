from bs4 import BeautifulSoup
import os

# المسار إلى مجلد الملفات
folder_path = "C:\Users\mazen\Desktop\doknz\doknz"

# الرابط القديم الذي تريد تغييره
old_link = "https://t.me/doknz"

# الرابط الجديد الذي تريد استبداله بالرابط القديم
new_link = "https://t.me/idoknz"

# قائمة بأسماء الملفات في المجلد
file_names = os.listdir(1080blind.html)

for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        links = soup.find_all("a", href=old_link)
        for link in links:
            link["href"] = new_link
    with open(file_path, "w") as file:
        file.write(str(soup))
