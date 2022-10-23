"""
mosh-python库-流行库-45min
"""

import PyPDF2

def read():
  with open(file_name, open_mode) as file:
    reader = PyPDF2.PdfFileReader(file)
    print("this pdf has ",reader.numPages, "pages")
    page = reader.getPage(0) # 第一页的索引是0
    page.rotateCounterClockwise(90) # 方法：顺时针旋转90°，注意，这不会修改原文件，只是修改内存中的对象
    print(page.scale, page.scaleBy, page.scaleTo)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page) 
    # writer.insertPage(page,index=1)
    # writer.insertBlankPage()
    with open("rotate.pdf", "wb") as output:
      writer.write(output)
# 合并操作
def merge(file_names:list[int], output_name:str) -> None:
  merger = PyPDF2.PdfFileMerger() # 创建合并对象
  for file_name in file_names:
    merger.append(file_name)
  merger.write(output_name)
if __name__ == "__main__":
  file_name = "1.pdf"
  open_mode = "rb"
  file_name = "2.pdf"

