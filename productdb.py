import sqlite3

conn = sqlite3.connect('productdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				productid TEXT,
				title TEXT,
				price REAL,
				image TEXT ) """)

c.execute("""CREATE TABLE IF NOT EXISTS product_status (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				product_id INTEGER,
				status TEXT) """)


def insert_product_status(pid,status):
	#pid = product id
	check = view_product_status(pid)
	if check == None:
		with conn:
			command = 'INSERT INTO product_status VALUES (?,?,?)'
			c.execute(command,(None,pid,status))
		conn.commit()
		print('status saved')
	else:
		print('pid exist!')
		print(check)
		update_product_status(pid,status)

def view_product_status(pid):
	# READ
	with conn:
		command = 'SELECT * FROM product_status WHERE product_id=(?)'
		c.execute(command,([pid]))
		result = c.fetchone()
	return result

def update_product_status(pid,status):
	# UPDATE
	with conn:
		command = 'UPDATE product_status SET status = (?) WHERE ID=(?)'
		c.execute(command,([status,pid]))
	conn.commit()
	print('updated:',(pid,status))

#################################
def Insert_product(productid,title,price,image):
	# CREATE
	with conn:
		command = 'INSERT INTO product VALUES (?,?,?,?,?)' # SQL
		c.execute(command,(None,productid,title,price,image))
	conn.commit() # SAVE DATABASE
	print('saved')


def View_product():
	# READ
	with conn:
		command = 'SELECT * FROM product'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result

def View_product_table_icon():
	# READ
	with conn:
		command = 'SELECT ID, productid, title FROM product'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result

def View_product_single(productid):
	# READ
	with conn:
		command = 'SELECT * FROM product WHERE productid=(?)'
		c.execute(command,([productid]))
		result = c.fetchone()
	print(result)
	return result


if __name__ == '__main__':
	# ฟังชั่นนี้เอาไว้เช็คว่าตอนนี้ไฟล์ที่กำลังรันนี้อยู่ในไฟล์จริงหรือไม่?
	#Insert_product('CF-1002','เอสเปรสโซ่',45, r'C:\Image\latte.png')
	# r'/Users/uncleengineer/Desktop/GUI/Image/a.png'
	# View_product()
	# View_product_table_icon()
	insert_product_status(1,'show')
	# print(view_product_status(1))
	