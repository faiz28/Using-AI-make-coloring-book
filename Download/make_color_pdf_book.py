from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfFileMerger
from reportlab.pdfbase import pdfmetrics
import os,random

pdf = canvas.Canvas("color_pdf.pdf")
pdf.setPageSize((8.5 * inch, 11 * inch)) 

# take one frame image

# take one frame image
frame_path = ".\\border\\"
frame_list = []
for file in os.listdir(frame_path):
    frame_list.append(frame_path+file)
random.shuffle(frame_list)
take_one_frame = frame_list[0]



# take limited amount of images
image_path = ".\\ninja\\"
image_list = []
for file in os.listdir(image_path):
    image_list.append(image_path+file)
random.shuffle(image_list)

x=0
odd_even =0
for i in range(0, len(image_list)):
    if len(image_list) ==0 or len(frame_list) == 0:
        break
    if odd_even%2==0:
        x=-0.4
    else:
        x=0
    odd_even+=1
    pdf.drawImage(take_one_frame, (1+x)*inch, 1*inch, width=7 * inch, height=9 * inch,mask='auto')
    pdf.drawImage(image_list[i], (2+x)*inch, 2*inch, width=5 * inch, height=7 * inch,mask='auto')
    pdf.showPage()
    print(i)
pdf.save()
        # print(file)
# pdf.drawImage(logo,  x*inch, (y+0.2)*inch, 0.6*inch,0.6*inch ,mask='auto')