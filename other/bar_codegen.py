# sudo pip3 install python-barcode

# import EAN13 from barcode module 
from barcode import EAN13

# Make sure to pass the number as string 
number = '5901234123457'

# Now, let's create an object of EAN13 
# class and pass the number
my_code = EAN13(number)
  
# Our barcode is ready. Let's save it. 
my_code.save("new_code")

# let’s generate the same barcode in PNG format

# import ImageWriter to generate an image file 
from barcode.writer import ImageWriter 

my_code = EAN13(number, writer=ImageWriter()) 
  
# Our barcode is ready. Let's save it. 
my_code.save("new_code1")