
# from Input_handler import read_input

import Input_handler as input 
import Output_handler as output
output_file = "C:\\Users\\anuja\Desktop\\project\\image-to-ASCII-converter\\output_data\\output.html"
input_file = "C:\\Users\\anuja\\Desktop\\project\\image-to-ASCII-converter\\input_data\\batman.jpg"



image = input.read_input(input_file,"rgb")


#pixel = image.getpixel((200, 220))
#print(pixel)

output.output_handler(output_file,"@", image)