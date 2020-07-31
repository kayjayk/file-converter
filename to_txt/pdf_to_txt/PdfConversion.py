#!/usr/bin/env python
# coding: utf-8

# In[5]:


import PyPDF4
import os


# In[3]:


class PdfConversion:
    def __init__(self, file_path):
        self.file_dir, self.file_name = os.path.split(file_path)
        self.file_path = file_path

    def pdf_to_txt(self):
        file = open(self.file_path, 'rb')
        fileReader = PyPDF4.PdfFileReader(file)
# #         fileReader.pageMode()
#     #     # 문서의 정보
#         print(fileReader.documentInfo)

#     #     # 전체 페이지수를 출력한다
#         print(fileReader.numPages)

        txt_list = []
        for i in range(fileReader.getNumPages()):
            pageObj = fileReader.getPage(i)
            txt = pageObj.extractText()
            print(txt)
            txt_list.append(txt)
        print('asdf')
        full_txt = ' '.join(txt_list)

        return full_txt

    def save_txt(self, save_dir, txt):
        file_name_wo_ext = self.file_name.split('.')[0]
        with open(os.path.join(self.root_dir, file_name_wo_ext + '.txt', "w")) as f:
            f.write(txt)

