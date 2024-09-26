import fitz
import tkinter as tk
from tkinter import filedialog, messagebox
#from tkinterdnd2 import DND_FILES, TkinterDnD

def insert_pdf(main_pdf_path, insert_pdf_path, position):
    main_doc = fitz.open(main_pdf_path)
    insert_doc = fitz.open(insert_pdf_path)

    main_doc.insert_pdf(insert_doc, from_page=0, to_page=len(insert_doc) - 1, start_at=position)
    output_path = f"{main_pdf_path[:-4]}_with_inserted.pdf"
    main_doc.save(output_path)

    main_doc.close()
    insert_doc.close()

    return output_path


def on_insert():
    main_pdf_path = main_pdf_entry.get()
    insert_pdf_path = insert_pdf_entry.get()
    position = int(position_entry.get())

    try:
        output_path = insert_pdf(main_pdf_path, insert_pdf_path, position)
        messagebox.showinfo("成功", f"操作完成，文件已保存为: {output_path}")
    except Exception as e:
        messagebox.showerror("错误", str(e))

def browse_main_pdf():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        main_pdf_entry.delete(0, tk.END)
        main_pdf_entry.insert(0, filename)

def browse_insert_pdf():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        insert_pdf_entry.delete(0, tk.END)
        insert_pdf_entry.insert(0, filename)

# 创建主窗口
app = tk.Tk()
app.title("PDF 插入工具（华门社科专用）")

# 主 PDF 路径输入
tk.Label(app, text="主 PDF 文件路径:").pack()
main_pdf_entry = tk.Entry(app, width=50)
main_pdf_entry.pack()
tk.Button(app, text="浏览", command=browse_main_pdf).pack()

# 要插入的 PDF 路径输入
tk.Label(app, text="要插入的 PDF 文件路径:").pack()
insert_pdf_entry = tk.Entry(app, width=50)
insert_pdf_entry.pack()
tk.Button(app, text="浏览", command=browse_insert_pdf).pack()

# 插入位置输入
tk.Label(app, text="插入位置（第几页之后）:").pack()
position_entry = tk.Entry(app)
position_entry.pack()

# 执行按钮
tk.Button(app, text="执行插入", command=on_insert).pack()

# 添加水印
watermark = tk.Label(app, text="Copyright:wsc2024", font=("Arial", 12), fg="gray", bg="white")
watermark.pack(side=tk.BOTTOM, fill=tk.X)

'''
# 允许拖放
def drop(event):
    file_path = event.data
    if file_path.endswith('.pdf'):
        if main_pdf_entry.focus_get() == main_pdf_entry:
            main_pdf_entry.delete(0, tk.END)
            main_pdf_entry.insert(0, file_path)
        elif insert_pdf_entry.focus_get() == insert_pdf_entry:
            insert_pdf_entry.delete(0, tk.END)
            insert_pdf_entry.insert(0, file_path)

main_pdf_entry.drop_target_register(DND_FILES)
main_pdf_entry.dnd_bind('<<Drop>>', drop)
insert_pdf_entry.drop_target_register(DND_FILES)
insert_pdf_entry.dnd_bind('<<Drop>>', drop)
'''
app.mainloop()


