from PIL import Image

def output_handler(file_path : str, ascii_value : str, image : Image):
    r = 50
    g = 255
    b = 100
    file_clear(file_path)
    with open(file_path, "a", encoding="utf-8") as file:
            html_body_start = '<html><body style="margin: 0; padding: 0; font-family: monospace; font-size: 10px; line-height: 0.6;">'
            html_body_end =(f'</body></html>')
            
            file.write(html_body_start)


            x,y = image.size
            print(x,y)
            for i in range(0,y):
                for j in range(0,x):
                    r,g,b = image.getpixel((j,i))
                    colored_character = (f'<span style="color: rgb({r}, {g}, {b});">'f'{ascii_value}</span>')
                    file.write(colored_character)
                file.write("<br>")
            file.write(html_body_end)




def file_clear(file_path:str):
    file_Clear = ""
    with open(file_path, "w", encoding="utf-8") as file:
         file.write(file_Clear)