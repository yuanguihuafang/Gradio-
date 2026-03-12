# Gradio 入门示例代码
# #案例1 一个接收文本输入并返回该文本倒序输出的应用。 
# import gradio as gr
# def reverse_text(text):
#     # 将输入文本倒序返回，例如 "你好" → "好你"
#     return text[::-1]

# # 创建最简单的 Gradio 界面：输入文本，输出文本
# demo = gr.Interface(fn=reverse_text, inputs="text", outputs="text")
# demo.launch()

# # 更新界面布局  倒序+统计字数
# import gradio as gr

# # 这是修改后的函数
# def reverse_and_count(text):
#     reversed_text = text[::-1]   # 倒序
#     length = len(text)           # 统计字符数
#     return reversed_text, length

# demo = gr.Interface(
#     fn=reverse_and_count,
#     inputs="text",
#     # flagging_mode="never",
#     outputs=["text", "number"],  # 第一个输出是文本，第二个输出是一个数字
#     title="文本处理工具",  # 设置页面标题
#     description="输入一段文字，查看其倒序形式及字符数。",  # 添加简短说明
#     examples=[["你好，世界"], ["Hello World"]]          # 提供示例输入
# )

# demo.launch()


# #案例2 使用 Image 组件输入图像，并将其转换为铅笔素描。

# import gradio as gr
# import numpy as np
# import cv2

# def image_to_sketch(image):
#     gray_image = image.convert('L')              # 转为灰度图
#     inverted_image = 255 - np.array(gray_image)  # 颜色反转
#     blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)  # 高斯模糊
#     inverted_blurred = 255 - blurred             # 再次反转
#     # 原图除以模糊图，生成素描效果
#     pencil_sketch = cv2.divide(np.array(gray_image), inverted_blurred, scale=256.0)
#     return pencil_sketch
# demo = gr.Interface(
#     fn=image_to_sketch,
#     inputs=[gr.Image(label="输入图片", type="pil")],
#     outputs=[gr.Image(label="铅笔素描")],
#     title="图片转铅笔素描",
#     description="上传一张图片，自动转换为铅笔素描风格。"
# )

# demo.launch()