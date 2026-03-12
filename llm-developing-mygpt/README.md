```
# 介绍
- 展示基本的openai的api调用方法
- 展示简单的gradio界面

# 运行
1、创建虚拟环境并安装依赖
   - conda create -n env_xiaoxiang python=3.10
   - conda activate env_xiaoxiang
   - pip install -r requirements.txt

2、配置环境变量
   - 打开`.env.example`文件
   - 填写完整该文件中的`OPENAI_API_KEY`环境变量
   - 把`.env.example`文件重命名为`.env`

3、运行`app.py`文件
```bash
python app.py

# 学习教程
## Gradio
与他人共享机器学习模型、API 或数据科学工作流的最佳方式之一是创建一个交互式应用，使用户或同事能够在其浏览器中试用演示。

Gradio 允许您在 Python 中构建演示并共享它们。而且通常只需几行代码！因此，让我们开始吧。

官网 Quickstart：https://www.gradio.app/guides/quickstart

官网 Docs：https://www.gradio.app/docs/interface



