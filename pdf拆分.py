import fitz

def split_pdf(doc_path, split_page):
    doc = fitz.open(doc_path)

    # 创建两个新的 PDF 文档
    first_part = fitz.open()
    second_part = fitz.open()

    # 拷贝页面到各自的文档
    for page_num in range(len(doc)):
        if page_num < split_page:
            first_part.insert_page(-1)
            first_part[-1].show_pdf_page(first_part[-1].rect, doc, page_num)
        else:
            second_part.insert_page(-1)
            second_part[-1].show_pdf_page(second_part[-1].rect, doc, page_num)

    # 保存两个拆分后的 PDF
    first_part.save(f"{doc_path[:-4]}_part1.pdf")
    second_part.save(f"{doc_path[:-4]}_part2.pdf")

    # 关闭文档
    first_part.close()
    second_part.close()
    doc.close()
    print(f"操作完成，文件已保存为:\n{doc_path[:-4]}_part1.pdf\n{doc_path[:-4]}_part2.pdf")
    #return f"操作完成，文件已保存为:\n{doc_path[:-4]}_part1.pdf\n{doc_path[:-4]}_part2.pdf"

if __name__=='__main__':
    split_pdf('test.pdf',3)