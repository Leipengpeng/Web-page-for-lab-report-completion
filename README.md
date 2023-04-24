#### read me first

# Web-page-for-lab-report-completion
Based on chatGPT to realize the automatic completion of the webpage of the experiment report, input the PDF file to complete the OCR recognition, the writing of the experiment code, the generation of the experiment result, and the experiment report.基于chatGPT实现实验报告自动完成的网页，输入PDF文件即可完成OCR识别，实验代码书写，实验结果生成，实验报告。


#### 1.项目简介

本项目基于python flask技术编写，主要实现了以下特色功能

1.cv2计算二值化最佳阈值，然后通过tesseract本地进PDF OCR识别，最后通过chatGPT api工具进行文本修改

该方法对于代码类文本的纠错能力极强，可以非常高效率的实现代码类实验参考文档的PDF转化

2.sphinx本地进行语言转文本，然后通过chatGPT api工具进行修正

3.连接Mysql数据库的登录功能

4.借助chatGPT api接口和prism css js组件实现完成实验代码的生成，模拟截图和实验总结。

#### 2.如何使用

打开default.xml，填入自己的Mysql数据库名称，用户，密码。在数据库中新建一个包含users和password的表单。

填入自己的chatGPT api key

安装全部的项目依赖包

运行main.py即可运行。

#### 3.项目结构介绍

1.controller储存部分后台处理和逻辑判断，包括Mysql，chatGPT api调用，PDF OCR封装

2.entity储存表单类

3.history历史可执行代码储存

4.static flask规定的css js images icon 储存目录

5.template flask规定的html代码储存目录

6.main.py项目主程序，运行可见网页

7.testWebStyle.py用于测试网页的样式效果

#### 4.项目待改进内容

1.在flask框架下，html文件的csrf安全验证还没较好的完成，在表单输入验证方面存在部分bug

2.没有写用户注册相关，用户登录也欠考虑

3.没有写错误跳转页面，没有任何的error处理

4.由于chatGPT特性，实验报告生成部分可能会生成不全

5.由于没有使用Ajax等方法，代码表单的class不能动态的根据选择的内容变化

6.chatGPT本身的不稳定性，可能导致输出结果随open ai模型的变化而有所不同

7.部分css js image类型文件的引用失效（不过不影响功能）
