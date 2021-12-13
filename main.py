import os
from tkinter import *
import tkinter.filedialog
from pdf2image import convert_from_path
from PIL import ImageDraw
from PIL import Image

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

h=669
w=72
name=['김주현','김채림','민은지','박고은','박선아','안수빈','이가옥','이은혜','이혜수','임예진',"11","12","13","14","15","16","17"]
# image = Image.open("image.jpg")
# draw = ImageDraw.Draw(image)
# draw.line((0, h, image.size[1], h), fill="black", width=w)
# draw.line((0, h+w*2, image.size[1], h+w*2), fill="black", width=w)
# draw.line((0, h+w*3, image.size[1], h+w*3), fill="black", width=w)
# image.save("test.jpg")

for i in range(0,17):
    image=Image.open("image.jpg")
    draw = ImageDraw.Draw(image)
    for j in range(0,17):
        if j!=i:
            draw.line((0, h + w * j, image.size[1], h + w * j), fill="black", width=w)
        filename="이체확인증_"+name[i]+".jpg"
        image.save(filename)