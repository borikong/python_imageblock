import os
from tkinter import *
import tkinter.filedialog
from pdf2image import convert_from_path
from PIL import ImageDraw
from PIL import Image

h=669 #블록 처리를 시작할 세로 위치
w=72 #펜의 두께

def get_pdf_root():
    root = Tk().withdraw()
    pdf_root = tkinter.filedialog.askopenfilename(initialdir="/", title="PDF 파일 업로드", filetypes={("all files", "*.pdf")})
    print(pdf_root)
    return pdf_root

def get_save_root():
    root = Tk().withdraw()
    save_folder = tkinter.filedialog.askdirectory(title="저장 폴더 선택");
    print(save_folder)
    return save_folder

def pdf_to_img(pdf_root,save_root):
    try:
        directory = save_root + "/pdf2image"
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

    pages = convert_from_path(pdf_root,fmt="jpeg")

    for i, page in enumerate(pages):
        pagenum = None
        if i < 9:
            pagenum = "00" + str(i + 1)
        elif i >= 9 and i < 99:
            pagenum = "0" + str(i + 1)
        elif i >= 99:
            pagenum = str(i + 1)
        page.save(
            directory+"/image" + pagenum + ".jpg",
            "JPEG")

    return directory

# pdf_to_img(get_pdf_root(),get_save_root())

name=["name1","name2","name3","name4","name5","name6"]
# image = Image.open("image.jpg")
# draw = ImageDraw.Draw(image)
# draw.line((0, h, image.size[1], h), fill="black", width=w)
# image.save("test.jpg")

for i in range(0,17):
    image=Image.open("image.jpg")
    draw = ImageDraw.Draw(image)
    for j in range(0,17):
        if j!=i:
            draw.line((0, h + w * j, image.size[1], h + w * j), fill="black", width=w)
        filename="filename_"+name[i]+".jpg"
        image.save(filename)