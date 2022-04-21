from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *



class ProductIcon:

	def __init__(self):
		self.quantity = None
		self.table_product = None
		self.v_radio = None

	def popup(self):
		# PGUI = Product GUI
		PGUI = Toplevel()
		PGUI.geometry('500x500')
		PGUI.title('ตั้งค่า -> โชว์ไอคอนรายการสินค้า')

		# ตารางสินค้า
		header = ['ID', 'รหัสสินค้า', 'ชื่อสินค้า', 'แสดงไอคอน']
		hwidth = [50,50,200,70]

		self.table_product = ttk.Treeview(PGUI,columns=header, show='headings',height=15)
		self.table_product.pack()

		for hd,hw in zip(header,hwidth):
			self.table_product.column(hd,width=hw)
			self.table_product.heading(hd,text=hd)


		self.table_product.bind('<Double-1>', self.change_status)
		self.insert_table()
		PGUI.mainloop()

	def insert_table(self):
		data = View_product_table_icon()
		print(data)
		for d in data:
			row = list(d) #convert tuple to list
			row.append('✔')
			self.table_product.insert('','end',value=row)


	def change_status(self,event=None):

		select = self.table_product.selection()
		pid = self.table_product.item(select)['values'][0]
		print('PID:',pid)

		SGUI = Toplevel() # SGUI = Status GUI
		SGUI.geometry('400x400')

		self.v_radio = StringVar()

		# Radio
		RB1 = ttk.Radiobutton(SGUI,text='โชว์ไอคอน', variable=self.v_radio, value='show',command=lambda x=None:insert_product_status(int(pid),'show'))
		RB2 = ttk.Radiobutton(SGUI,text='ไม่โชว์ไอคอน', variable=self.v_radio, value='',command=lambda x=None:insert_product_status(int(pid),''))
		RB1.pack()
		RB2.pack()
		RB1.invoke() #ตั้งค่า default ของ radio

		# Dropdown

		dropdown = ttk.Combobox(SGUI, values=['โชว์ไอคอน','ไม่โชว์ไอคอน'])
		dropdown.pack()
		dropdown.set('โชว์ไอคอน')

		dropdown.bind('<<ComboboxSelected>>',lambda x=None: print(dropdown.get()))




		SGUI.mainloop()

	def command(self):
		self.popup()





class AddProduct:

	def __init__(self):
		self.v_productid = None
		self.v_title = None
		self.v_price = None
		self.v_imagepath = None

	def popup(self):
		MGUI = Toplevel()
		MGUI.geometry('500x600')
		MGUI.title('Add Product')

		self.v_productid = StringVar()
		self.v_title = StringVar()
		self.v_price = StringVar()
		self.v_imagepath = StringVar()

		L = Label(MGUI,text='เพิ่มรายการสินค้า',font=(None,30))
		L.pack(pady=20)

		# -----------------
		L = Label(MGUI,text='รหัสสินค้า',font=(None,20)).pack()
		E1 = ttk.Entry(MGUI,textvariable= self.v_productid,font=(None,20))
		E1.pack(pady=10)

		# -----------------
		L = Label(MGUI,text='ชื่อสินค้า',font=(None,20)).pack()
		E2 = ttk.Entry(MGUI,textvariable= self.v_title,font=(None,20))
		E2.pack(pady=10)

		L = Label(MGUI,text='ราคา',font=(None,20)).pack()
		E3 = ttk.Entry(MGUI,textvariable= self.v_price,font=(None,20))
		E3.pack(pady=10)

		L = Label(MGUI,textvariable=self.v_imagepath).pack()

		Bselect = ttk.Button(MGUI, text='เลือกรูปสินค้า ( 50 x 50 px )',command=self.selectfile)
		Bselect.pack(pady=10)

		Bsave = ttk.Button(MGUI, text='บันทึก',command=self.saveproduct)
		Bsave.pack(pady=10,ipadx=20,ipady=10)

		
		MGUI.mainloop()

	def selectfile(self):
		filetypes = (
				('PNG', '*.png'),
				('All files', '*.*')
			)
		select = filedialog.askopenfilename(title='เลือกไฟล์ภาพ',initialdir='/',filetypes=filetypes)
		self.v_imagepath.set(select)
		'''
		# focus on top level (next time)
		self.lift()
		self.focus_force()
		self.grab_set()
		self.grab_release()
		'''


	def saveproduct(self):
		v1 = self.v_productid.get()
		v2 = self.v_title.get()
		v3 = float(self.v_price.get())
		v4 = self.v_imagepath.get()
		Insert_product(v1,v2,v3,v4)
		self.v_productid.set('')
		self.v_title.set('')
		self.v_price.set('')
		self.v_imagepath.set('')
		View_product()


	def command(self):
		self.popup()


if __name__ == '__main__':
	test = AddProduct()