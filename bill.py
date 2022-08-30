# bill.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm, inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime
########################
import win32print
import win32api
#########START##########

# set font size
pdfmetrics.registerFont(TTFont('F1','tahomabd.ttf'))
pdfmetrics.registerFont(TTFont('F2','tahoma.ttf'))
pdfmetrics.registerFont(TTFont('F3','impact.ttf'))

# paper size
c = canvas.Canvas('bill.pdf')
c.setPageSize((80 * mm, 150 * mm ))

# HEADER
c.setFont('F1',10)
c.drawCentredString(40 * mm, 140 * mm, 'ใบเสร็จรับเงิน/ใบกำกับภาษีอย่างย่อ')

c.setFont('F1',15)
c.drawCentredString(40 * mm, 130 * mm, 'ร้านลุงโภชนาการ')

company = ['ที่อยู่: 123 พหลโยธิน สามเสนใน พญาไท กทม.',
           'โทร. 02-123-4567, 081 238 5678',
           'สาขา: 199 TAX ID: 0107778888',
           'Line: @unclefood']

c.setFont('F2',8)
for i,cm in enumerate(company):
	c.drawCentredString(40 * mm, (120 - (i*3)) * mm ,cm)


products = [['ชาร้อน',1,50,50],['ชาเขียว',2,50,100],['ชามะลิ',3,30,90],['กาแฟโบราณ',1,40,40]]

for i,pd in enumerate(products):
	c.drawString(5 * mm, (100 - (i*4)) * mm, pd[0])
	c.drawRightString(35 * mm, (100 - (i*4)) * mm, str(pd[1]))
	c.drawRightString(40 * mm, (100 - (i*4)) * mm, str(pd[2]))
	c.drawRightString(65 * mm, (100 - (i*4)) * mm, str(pd[3]))

c.showPage()
c.save()

#########PRINT PDF##########
current_printer = win32print.GetDefaultPrinter()
win32api.ShellExecute(0, 'print', 'bill.pdf', None, '.', 0)
win32print.SetDefaultPrinter(current_printer)

'''
# EXAMPLE

# hello text

# c.setFont('F1',10)
# c.drawString(10 * mm, 140 * mm, 'Hello Text')

# c.setFont('F2',7)
# c.drawString(10 * mm, 30 * mm, 'ตัวอย่าง')
# c.drawCentredString(40 * mm, 50 * mm, 'อักษรตรงกลาง')

# c.setFont('F3',7)
# c.drawRightString(70 * mm, 80 * mm, '5')
# c.drawRightString(70 * mm, 85 * mm, '60')
# c.drawRightString(70 * mm, 90 * mm, '700')
# c.drawRightString(70 * mm, 95 * mm, '8000')

#x1,y1,x2,y2 = [10 * mm,100 * mm,70  * mm,100 * mm]
#ml = [[10 * mm,100 * mm,70  * mm,100 * mm],[10 * mm,120 * mm,70  * mm,120 * mm]]
# c.line(x1,y1,x2,y2)
#c.lines(ml)

'''