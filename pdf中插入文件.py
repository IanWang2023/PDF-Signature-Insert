import fitz

def insert_pdf(main_pdf_path, insert_pdf_path, position):
    main_doc = fitz.open(main_pdf_path)  # 打开主 PDF 文件
    insert_doc = fitz.open(insert_pdf_path)  # 打开要插入的 PDF 文件

    # 将插入的 PDF 插入到主 PDF 的指定位置
    main_doc.insert_pdf(insert_doc, from_page=0, to_page=len(insert_doc) - 1, start_at=position)

    # 保存修改后的主 PDF
    output_path = f"{main_pdf_path[:-4]}_with_inserted.pdf"
    main_doc.save(output_path)

    # 关闭文档
    main_doc.close()
    insert_doc.close()

    print(f"操作完成，文件已保存为: {output_path}")

# 如果需要运行该函数，请取消注释以下行
if __name__ == '__main__':
#    print(insert_pdf("main.pdf", "insert.pdf", 2))  # 示例用法，将 insert.pdf 插入到 main.pdf 的第 2 页
    insert_pdf('abc.pdf', 'abc_part1.pdf', 3)