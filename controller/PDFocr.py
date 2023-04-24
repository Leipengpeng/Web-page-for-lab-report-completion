from tkinter import Image
import fitz as PyMuPDF
import cv2
from pytesseract import pytesseract
from controller.chatGPT import API

#以下代码用来实现PDF的OCR功能(包含了chatGPT的修正)

def PDFocr(file_path):
    return PDF(file_path)

def OCR(file_path):
    image1 = Image.open(file_path)
    imgery = image1.convert('L')
    image2 = cv2.imread(file_path)
    # 使用OTSU算法自动计算最佳阈值
    ret, thresh = cv2.threshold(image2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    threshold = ret
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    temp = imgery.point(table, '1')
    text = pytesseract.image_to_string(temp, lang="chi_sim+eng", config='--psm 6')
    text=purify(text)
    return str(text)

purifyInduce="请去除下面文章中的错别字和错误代码，然后输出:\""
def purify(text):
    return API(text, purifyInduce)

# Opening the PDF file
#C:/Users/leilu/Desktop词法分析问题描述.pdf
def PDF(file_path):
    with PyMuPDF.open(file_path) as doc:
        out=""
        # Initializing lists to store text and image data
        text_list = []
        image_list = []
        index = 0  # 当前的图片数量
        # Iterating through each page of the PDF
        for page in doc:
            text = page.get_text("text")
            text_list.append(text)
            for image in page.get_images():
                pix = PyMuPDF.Pixmap(doc, image[0])
                pix.writePNG("../temp/" + index + "image.png")
                text = OCR("../temp/" + index + "image.png")
                image_list.append(text)
                index += 1
        # Printing the text and image data in the desired order
        for i in range(len(text_list)):
            out+=text_list[i]
            if i < len(image_list):
                out+=image_list[i]
        return out
