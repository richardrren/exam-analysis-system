import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
from datetime import datetime

from config import load_config, save_config
from ai_client import generate_analysis
from excel_generator import generate_excel
from pdf_parser import extract_pdf_content


class ExamAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("初中科学试卷分析系统")
        self.root.geometry("800x600")

        self.config = load_config()
        self.current_pdf_path = None
        self.analysis_data = None
        self.processing = False

        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        main_frame = ttk.Frame(notebook)
        config_frame = ttk.Frame(notebook)

        notebook.add(main_frame, text="试卷分析")
        notebook.add(config_frame, text="接口配置")

        self.create_main_tab(main_frame)
        self.create_config_tab(config_frame)

    def create_main_tab(self, parent):
        upload_frame = ttk.LabelFrame(parent, text="PDF上传", padding=10)
        upload_frame.pack(fill=tk.X, padx=10, pady=10)

        self.pdf_label = ttk.Label(upload_frame, text="未选择文件", foreground="gray")
        self.pdf_label.pack(side=tk.LEFT, padx=5)

        ttk.Button(upload_frame, text="选择PDF文件", command=self.select_pdf).pack(side=tk.LEFT, padx=5)

        action_frame = ttk.Frame(parent, padding=10)
        action_frame.pack(fill=tk.X, padx=10, pady=5)

        self.analyze_btn = ttk.Button(action_frame, text="开始分析", command=self.start_analysis, state=tk.DISABLED)
        self.analyze_btn.pack(side=tk.LEFT, padx=5)

        self.download_btn = ttk.Button(action_frame, text="下载细目表", command=self.download_excel, state=tk.DISABLED)
        self.download_btn.pack(side=tk.LEFT, padx=5)

        log_frame = ttk.LabelFrame(parent, text="处理日志", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def create_config_tab(self, parent):
        frame = ttk.Frame(parent, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="API地址:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.api_url_entry = ttk.Entry(frame, width=50)
        self.api_url_entry.grid(row=0, column=1, sticky=tk.EW, pady=10)
        self.api_url_entry.insert(0, self.config.get("api_url", ""))

        ttk.Label(frame, text="API密钥:").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.api_key_entry = ttk.Entry(frame, width=50, show="*")
        self.api_key_entry.grid(row=1, column=1, sticky=tk.EW, pady=10)
        self.api_key_entry.insert(0, self.config.get("api_key", ""))

        ttk.Label(frame, text="模型名称:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.model_entry = ttk.Entry(frame, width=50)
        self.model_entry.grid(row=2, column=1, sticky=tk.EW, pady=10)
        self.model_entry.insert(0, self.config.get("model", "gpt-4"))

        frame.columnconfigure(1, weight=1)

        ttk.Button(frame, text="保存配置", command=self.save_config).grid(row=3, column=0, columnspan=2, pady=20)

    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def select_pdf(self):
        file_path = filedialog.askopenfilename(
            title="选择PDF文件",
            filetypes=[("PDF文件", "*.pdf"), ("所有文件", "*.*")]
        )
        if file_path:
            self.current_pdf_path = file_path
            self.pdf_label.config(text=os.path.basename(file_path), foreground="black")
            self.analyze_btn.config(state=tk.NORMAL)
            self.log(f"已选择文件: {os.path.basename(file_path)}")

    def start_analysis(self):
        if not self.current_pdf_path:
            messagebox.showwarning("警告", "请先选择PDF文件")
            return

        if self.processing:
            messagebox.showwarning("警告", "正在处理中，请稍候")
            return

        config = {
            "api_url": self.api_url_entry.get(),
            "api_key": self.api_key_entry.get(),
            "model": self.model_entry.get()
        }

        if not config["api_url"] or not config["api_key"]:
            messagebox.showwarning("警告", "请先配置API接口信息")
            return

        self.processing = True
        self.analyze_btn.config(state=tk.DISABLED)
        self.log("开始处理...")

        thread = threading.Thread(target=self.process_pdf, args=(config,))
        thread.daemon = True
        thread.start()

    def process_pdf(self, config):
        try:
            self.log("步骤1/4: 正在解析PDF文件...")
            pdf_content = extract_pdf_content(self.current_pdf_path)
            if not pdf_content:
                self.root.after(0, self.handle_error, "PDF解析失败")
                return

            self.log("步骤2/4: PDF解析成功")
            self.log("步骤3/4: 正在调用AI分析...")
            self.analysis_data = generate_analysis(
                pdf_content,
                config["api_url"],
                config["api_key"],
                config["model"]
            )

            if not self.analysis_data:
                self.root.after(0, self.handle_error, "AI分析失败")
                return

            self.log("步骤4/4: 分析完成！")
            self.log(f"共分析 {len(self.analysis_data)} 道题目")

            self.root.after(0, self.handle_success)

        except Exception as e:
            self.root.after(0, self.handle_error, f"发生错误: {str(e)}")

    def handle_error(self, error_msg):
        self.log(f"错误: {error_msg}")
        self.processing = False
        self.analyze_btn.config(state=tk.NORMAL)

    def handle_success(self):
        self.processing = False
        self.download_btn.config(state=tk.NORMAL)
        self.analyze_btn.config(state=tk.NORMAL)
        messagebox.showinfo("成功", "试卷分析完成！请下载细目表。")

    def download_excel(self):
        if not self.analysis_data:
            messagebox.showwarning("警告", "没有可下载的数据")
            return

        default_name = os.path.splitext(os.path.basename(self.current_pdf_path))[0] + "-细目表.xlsx"
        file_path = filedialog.asksaveasfilename(
            title="保存细目表",
            defaultextension=".xlsx",
            initialfile=default_name,
            filetypes=[("Excel文件", "*.xlsx"), ("所有文件", "*.*")]
        )

        if file_path:
            if generate_excel(self.analysis_data, file_path):
                self.log(f"细目表已保存: {os.path.basename(file_path)}")
                messagebox.showinfo("成功", "细目表已保存！")
            else:
                messagebox.showerror("错误", "保存失败")

    def save_config(self):
        config = {
            "api_url": self.api_url_entry.get(),
            "api_key": self.api_key_entry.get(),
            "model": self.model_entry.get()
        }
        save_config(config)
        self.config = config
        messagebox.showinfo("成功", "配置已保存！")


def main():
    root = tk.Tk()
    app = ExamAnalysisApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
