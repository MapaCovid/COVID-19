
import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path, page=None):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)




    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    return text


directory = '../informes_minsal/PDF/Informes-Departamento-Epidimiologia/'
date = '2020-03-30'
path = directory + date + '-INFORME_EPI_COVID19.pdf'


rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
fp = open(path, 'rb')
interpreter = PDFPageInterpreter(rsrcmgr, device)
password = ""
maxpages = 0
caching = True
pagenos = set()

pages = [page for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                              password=password,
                              caching=caching,
                              check_extractable=True)]

i = 0
page4 = interpreter.process_page(pages[4])
    
fp.close()
device.close()
text = retstr.getvalue()
retstr.close()





