# -*- coding=utf-8 -*-

from urllib import request

import cv2
import pytesseract
from PIL import Image
import flask_wtf.csrf
import pytesseract.pytesseract
import pyttsx3
import speech_recognition as sr
from flask import Flask, render_template, request
from controller import mysqlConnect
from controller.chatGPT import purify, program, homeWorkD, out
from entity.loginForm import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "vauikohkjqkv o29038rtq9rof&"
flask_wtf.csrf.CSRFProtect(app)

'''
    各网页的直接链接

    目前有的页面是 login google chatGPTorc sphinx chatGPTout
'''


@app.route('/')
def index():
    # 登录页
    return render_template('loginPage.html')


@app.route('/google')
def google():
    # google
    return render_template('mainPage.html')


@app.route('/chatGPT')
def chatGPT():
    # generic页面的逻辑
    return render_template('chatGPT.html')


@app.route('/sphinx')
def sphinx():
    # generic页面的逻辑
    return render_template('sphinx.html')

@app.route('/homeWork')
def homeWork():
    # generic页面的逻辑
    return render_template('homeWork.html')


'''
    网页的提交逻辑处理

    也就是表单提交后直接关联的第一个代码
'''


# 登录页
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        # and form.validate_on_submit() 未解决form方法
        name = form.name.data
        email = form.email.data
        if mysqlConnect.check_user(name, email):
            return render_template('mainPage.html')
    return render_template('loginPage.html')


# 谷歌页 同时也是登进首页
@app.route('/googleSpeech', methods=['GET', 'POST'])
def googleSpeech():
    if request.method == 'POST':
        file_path = request.form.get('file_path')
        output = google(file_path)
        engine = pyttsx3.init()
        engine.say(output)
        engine.runAndWait()
        return render_template('mainPage.html', output=output)
    else:
        return render_template('mainPage.html')


# chatGPT 辅助OCR 页
@app.route('/chatGPT_post', methods=['GET', 'POST'])
def chatGPT_post():
    # C:/Users/leilu/Desktop/image-20230415010946260.png
    if request.method == 'POST':
        file_path = request.form.get('file_path')
        output = esseract(file_path)
        output = purify(output)
        return render_template('chatGPT.html', output=output)
    else:
        return render_template('chatGPT.html')


# sphinx页
@app.route('/sphinxSpeech', methods=['GET', 'POST'])
def sphinxSpeech():
    if request.method == 'POST':
        file_path = request.form.get('file_path')
        output = sphinx(file_path)
        return render_template('sphinx.html', output=output)
    else:
        return render_template('sphinx.html')

# chatGPT 辅助OCR 页
@app.route('/homeWorkDown', methods=['GET', 'POST'])
def homeWorkDown():
    if request.method == 'POST':
        file_path = request.form.get('file_path')
        output = esseract(file_path)
        #output OCR结果
        output = purify(output)

        #outputP 代码段
        outputP=program(output)

        #outputO 代码伪运行
        outputO = out(outputP)

        # outputH 实验报告
        outputH = homeWorkD(output)

        return render_template('homeWork.html', output=output,outputP=outputP,outputO=outputO,outputH=outputH)
    else:
        return render_template('homeWork.html')


'''
    各页的处理逻辑

    主要内嵌在前面的提交逻辑处理内，负责具体的处理
'''


# google语音转文字的逻辑
def google(file_path):
    # 实现语音转文字的逻辑
    # C:/Users/leilu\Desktop/LibriSpeech/dev-clean/84/121123/84-121123-0000.flac
    filename = file_path
    # initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
    return text


# esseract实现OCR的逻辑
def esseract(file_path):
    image1 = Image.open(file_path)
    imgery = image1.convert('L')
    image2 = cv2.imread(file_path, 0)
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
    return str(text)


# sphinx实现语音转文字的逻辑
def sphinx(file_path):
    # 实现语音转文字的逻辑
    # C:/Users/leilu\Desktop/LibriSpeech/dev-clean/84/121123/84-121123-0000.flac
    filename = file_path
    # initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_sphinx(audio_data)
    return text


'''
    main函数 运行相关
'''

if __name__ == '__main__':
    app.run(debug=True)






