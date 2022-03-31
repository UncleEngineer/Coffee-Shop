import sqlite3

conn = sqlite3.connect('productdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				productid TEXT,
				title TEXT,
				price REAL,
				image TEXT ) """)


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
	View_product()

	