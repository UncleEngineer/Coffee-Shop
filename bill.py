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
import subprocess
#########START##########


def PrintBill(products=[['A',50,1,50],['B',50,1,50]],printer=False,openfile=False,**kwargs):

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

	c.setFont('F2',7)
	c.drawString(5 * mm, 105 * mm, 'TAX INVOICE: {}'.format(kwargs['transaction']))
	c.drawRightString(70 * mm, 105 * mm, '{}'.format(kwargs['timestamp']))
	#products = [['ชาร้อน',50,1,50],['ชาเขียว',50,2,100],['ชามะลิ',30,3,90],['กาแฟโบราณ',40,1,40]]


	c.setFont('F2',8)

	next_ref = 0

	for i,pd in enumerate(products):
		c.drawString(5 * mm, (100 - (i*4)) * mm, pd[0])
		c.drawRightString(50 * mm, (100 - (i*4)) * mm, str(pd[1]))
		c.drawRightString(60 * mm, (100 - (i*4)) * mm, str(pd[2]))
		c.drawRightString(70 * mm, (100 - (i*4)) * mm, str(pd[3]))
		next_ref = 100 - (i*4) # next line y location

	quan = sum([ p[2] for p in products])
	total  = sum([ p[3] for p in products])
	vat = total * (7/107)
	nettotal = total * (100/107)

	c.setFont('F2',7)
	c.drawString(5 * mm, (next_ref - 5) * mm, '-' * 75)
	c.setFont('F2',9)
	c.drawString(5 * mm, (next_ref - 10) * mm, 'Total')
	c.drawRightString(70 * mm, (next_ref - 10) * mm, '{:,.2f}'.format(total))
	c.drawRightString(40 * mm, (next_ref - 10) * mm, '({})'.format(quan))
	c.setFont('F2',7)
	c.drawString(5 * mm, (next_ref - 15) * mm, '-' * 75)
	# VAT
	c.setFont('F2',7)
	c.drawString(5 * mm, (next_ref - 20) * mm, 'VAT 7%')
	c.drawRightString(70 * mm, (next_ref - 20) * mm, '{:,.2f}'.format(vat))

	# NET TOTAL
	c.setFont('F2',7)
	c.drawString(5 * mm, (next_ref - 25) * mm, 'NET TOTAL')
	c.drawRightString(70 * mm, (next_ref - 25) * mm, '{:,.2f}'.format(nettotal))
	# OTHER
	c.drawString(5 * mm, (next_ref - 30) * mm, '-' * 75 )
	c.drawCentredString(40 * mm, (next_ref - 35) * mm, 'Join Uncle Member')
	c.drawCentredString(40 * mm, (next_ref - 40) * mm, 'www.uncle-engineer.com')
	c.drawString(5 * mm, (next_ref - 45) * mm, '-' * 75 )
	c.drawCentredString(40 * mm, (next_ref - 50) * mm, 'Thank You')

	c.showPage()
	c.save()

	#########PRINT PDF##########
	if printer:
		current_printer = win32print.GetDefaultPrinter()
		win32api.ShellExecute(0, 'print', 'bill.pdf', None, '.', 0)
		win32print.SetDefaultPrinter(current_printer)
	
	# open pdf
	if openfile:
		subprocess.Popen('bill.pdf',shell=True)


if __name__ == '__main__':

	printout =[['ลาเต้',50,1,50],['เอสเปรสโซ',40,2,80],
			   ['ลาเต้',50,1,50],['เอสเปรสโซ',40,2,80],
			   ['ลาเต้',50,1,50],['เอสเปรสโซ',40,2,80],
			   ['ลาเต้',50,1,50],['เอสเปรสโซ',40,2,80],
			   ['ลาเต้',50,1,50],['เอสเปรสโซ',40,2,80],
			   ['ลาเต้',50,1,50],['เอสเปรสโซ',40,2,80],
			   ]
	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
	transaction = '23452345234'

	PrintBill(printout,transaction=transaction,timestamp=timestamp,printer=True)


















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