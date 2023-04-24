import openai
from xml.dom import minidom
import xml.dom.minidom

dom_tree = xml.dom.minidom.parse("..\default.xml")
root = dom_tree.documentElement

def API(text,induce):
    # 设置API密钥
    openai.api_key = root.getElementsByTagName("element")[4].firstChild.nodeValue.strip("'")
    # 设置模型和引擎ID
    model_engine = "text-davinci-003"  # 模型和引擎ID
    # 与GPT-3进行交互的函数
    def interact_with_gpt3(prompt):
        response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024)
        return response.choices[0].text.strip()
        # 命令行应用程序
        # 从用户那里获取输入
    user_input = text
    # 将输入与医疗领域的提示文本合并，并发送到GPT-3，获取响应
    prompt = induce + user_input+"\""
    gpt3_response = interact_with_gpt3(prompt)
    # 将GPT-3的响应打印到控制台
    print(user_input)
    print(gpt3_response)
    return gpt3_response

purifyInduce="请去除下面文章中的错别字和错误代码，然后输出:\""
def purify(text):
    return API(text, purifyInduce)

programInduce="请基于下面文章写出和补全代码，尽可能的利用文章中现有的代码和语言，代码如果有错误和缺少的话进行补全，然后输出:\""
def program(text):
    return API(text, programInduce)


def out(text,text2):
    outInduce = "实验要求\n"+text+"\n代码\n"+text2+"\n给出代码运行输出的结果，代码如果有错误和缺少的话请忽略，然后输出:\""
    return API(text, outInduce)

homeWorkInduce="请基于以下内容写一份500字左右的实验报告，内容涉及实验学到的知识，调用的数据结构，算法，设计方法:\""
def homeWorkD(text):
    return API(text, homeWorkInduce)

shorterInduce="请缩写以下内容\""
def short(text):
    return API(text, shorterInduce)

languangeInduce="这段代码的编程语言是?\""
def languange(text):
    return API(text, languangeInduce)