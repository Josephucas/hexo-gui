# hexo-gui

功能:
根据自己的模块(有默认和我自定义的"paper"),填写好新建的文章名称之后,hexo可以在新建该名称的文章
选择上传和部署后,hexo上传和部署更新的博客

## 注意事项
1. 需要在hexo-gui.py脚本中修改hexo的文件夹位置为自己的目录
2. 如果自己有设计好的文章模板,需要在脚本中自己修改名称,我的另外一个脚本的模板名称是"paper",
3. 如果自己没有叫paper的模板的话,就直接用默认的就行.


脚本测试成功后

可以使用pyinstaller将脚本转换为一个可执行的二进制文件,这样可以在桌面直接完成hexo的简单操作
具体方式为
在指定目录下

```python
pip install pyinstaller
pyinstaller -F script.py

```

 
