from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter
from random import randint

def make_bitpic(img,string_generator,scale=16,font_size=40,compression=2,spacing=0):
    width,height = img.size
    draw_img = Image.new("RGB",(width*scale,height*scale))
    canvas = ImageDraw.Draw(draw_img)
    
    pixels = img.load()
    f = ImageFont.truetype("Fonts/arial.ttf",font_size)
    canvas.fontmode = "1"
  
    for i in range(0,height,compression):
        for j in range(0,width,compression):
            canvas.text((j*scale+spacing,i*scale+spacing),next(string_generator),font=f,fill = pixels[j,i])
    return draw_img

def binary_generator():
    while True:
        yield str(randint(0,1))
        
if __name__ == '__main__':
    img = Image.open("input.jpg")
    make_bitpic(img,binary_generator(),spacing=2).save("a_output.jpg")
    
   

    
