import fitz

def merge_two_pdfs(pdf1_path, pdf2_path, output_path):
    merged_doc = fitz.open()  # 创建一个新的 PDF 文档

    # 打开第一个 PDF 文件并插入到合并文档中
    doc1 = fitz.open(pdf1_path)
    merged_doc.insert_pdf(doc1)
    doc1.close()  # 关闭第一个 PDF 文件

    # 打开第二个 PDF 文件并插入到合并文档中
    doc2 = fitz.open(pdf2_path)
    merged_doc.insert_pdf(doc2)
    doc2.close()  # 关闭第二个 PDF 文件

    # 保存合并后的 PDF
    merged_doc.save(output_path)
    merged_doc.close()

    print(f"合并完成，文件已保存为: {output_path}")

# 如果需要运行该函数，请取消注释以下行
if __name__ == '__main__':

    merge_two_pdfs('abc_part1.pdf','abc_part2.pdf','output.pdf')