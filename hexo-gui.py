import os
import tkinter as tk
import tkinter.messagebox as msgbox


def change_dir(path):
    """
    切换到指定目录
    :param path: 目标目录路径
    :return: None
    """
    os.chdir(path)


def upload_and_deploy():
    try:
        change_dir(myPath)
        os.system("hexo clean")
        os.system("hexo g")
        os.system("hexo d")
    except Exception as e:
        msgbox.showerror("错误", "上传并部署失败：\n" + str(e))
        return

    # 弹窗提示上传并部署成功
    msgbox.showinfo("提示", "上传并部署成功！")


myPath = "D:\\github\\Josephucas.github.io"


class HexoUploader:
    def __init__(self, master):
        # 创建主窗口
        self.master = master
        master.title("Hexo上传并部署")
        master.configure(bg="gray")

        # 创建模板类型选择部分
        template_frame = tk.Frame(master, bg="gray")
        template_frame.pack(pady=10)
        template_label = tk.Label(template_frame, text="模板类型:", bg="gray", font=("Arial", 12))
        template_label.pack(side=tk.LEFT, padx=10)
        self.template_var = tk.StringVar()
        self.template_var.set("默认")
        default_radio = tk.Radiobutton(template_frame, text="默认", variable=self.template_var, value="默认", bg="gray",
                                       font=("Arial", 12))
        default_radio.pack(side=tk.LEFT, padx=10)
        paper_radio = tk.Radiobutton(template_frame, text="paper", variable=self.template_var, value="paper", bg="gray",
                                     font=("Arial", 12))
        paper_radio.pack(side=tk.LEFT)

        # 创建文章标题输入部分和生成文章图标
        title_frame = tk.Frame(master, bg="gray")
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text="文章标题:", bg="gray", font=("Arial", 12))
        title_label.pack(side=tk.LEFT, padx=10)
        self.title_entry = tk.Entry(title_frame, width=30, font=("Arial", 12))
        self.title_entry.pack(side=tk.LEFT)
        gen_button = tk.Button(title_frame, text="生成文章", bg="gray", font=("Arial", 12), command=self.generate_article)
        gen_button.pack(side=tk.LEFT, padx=10)

        # 创建上传并部署按钮
        button_frame = tk.Frame(master, bg="gray")
        button_frame.pack(pady=10)
        upload_button = tk.Button(button_frame, text="上传并部署", bg="gray", font=("Arial", 12),
                                  command=upload_and_deploy)
        upload_button.pack()

    # 生成文章函数
    def generate_article(self):
        # 获取模板类型和文章标题
        template = self.template_var.get()
        title = self.title_entry.get()

        # 生成文章
        if template == "默认":
            change_dir(myPath)
            os.system("hexo new " + title)
        else:
            change_dir(myPath)
            os.system("hexo new paper " + title)

        # 弹窗提示生成文章成功
        msgbox.showinfo("提示", "文章生成成功！")


if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    app = HexoUploader(root)
    root.mainloop()
