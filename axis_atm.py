from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import datetime

print("********************** AXIS BANK ATM CARD MACHINE **********************")

image = Image.new('RGB', (1000, 900), (165, 42, 42))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Bold.ttf', size=45)

(x, y) = (20, 20)
message = "SECURE +"
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number.
(x, y) = (200, 510)
idno1 = random.randint(1000, 9000)
message = str(idno1)
idno2 = random.randint(1000, 9000)
message += ' ' + str(idno2)
idno3 = random.randint(1000, 9000)
message += ' ' + str(idno3)
idno4 = random.randint(1000, 9000)
message += ' ' + str(idno4)
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (20, 600)
message = input('Enter Your Full Name: ')
name = message
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)


now = datetime.datetime.now()
from_year = now.year
from_month = now.month

start_validity = str(from_month) + "/" + str(from_year)

till_year = from_year + 5
till_month = from_month

end_validity = str(till_month) + "/" + str(till_year)

(x, y) = (20, 655)
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=30)
draw.text((x, y), "FROM  " + start_validity, fill=color, font=font)


(x, y) = (300, 655)
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=30)
draw.text((x, y), "THRU  " +end_validity, fill=color, font=font)

(x, y) = (20, 740)
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=30)
draw.text((x, y), "INSTA DEBIT CARD", fill=color, font=font)

image.save(str(name) + '.png')

qr_code = qrcode.make(str(idno1))
qr_code.save(str(idno1) + '.bmp')

final_image = Image.open(name + '.png')
qr_image = Image.open(str(idno1) + '.bmp')
axis_logo = Image.open("axis_logo"+'.png')
visa_logo = Image.open("visa"+'.gif')

final_image.paste(axis_logo, (750, 20))
final_image.paste(qr_image, (30, 200))

final_image.paste(visa_logo, (650, 680))

final_image.save(name + '.png')

print('\n\n\nYour ATM CARD Successfully created in a PNG file ' + name + '.png')

