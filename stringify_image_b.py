from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter
from random import randint
from time import time

def make_blank_bitpic(img,string_generator,scale,font_size,spacing):
    
    draw_img = Image.new("RGB",(img.size[0]*scale,img.size[1]*scale))
    width,height = draw_img.size
    d = ImageDraw.Draw(draw_img)
    pixels = img.load()
    f = ImageFont.truetype("courbd.ttf",font_size)
    d.fontmode = "1"
  
    for i in range(0,height):
       
        d.text((0,i*spacing),''.join(next(string_generator) for i in range(width//scale)),font=f,fill =(255,255,255))
    return draw_img

def hd_bitpic(img,string_generator,scale=1,font_size=12,spacing=11):
    start = time()
    ret_img = make_blank_bitpic(img,string_generator,scale,font_size,spacing)
  
    print("Blank Done",time() - start)
    width,height = img.size
    new_width,new_height = ret_img.size
    px_old = img.load()
    px_new = ret_img.load()
    
    for y in range(height):
        for x in range(width):
            tmp = px_old[x,y]
            if scale == 1:
                if px_new[x,y] == (255,255,255):
                    px_new[x,y] = tmp
            else:
                for i in range(y*scale,y*scale+scale):
                    for j in range(x*scale,x*scale+scale):
                        if px_new[j,i] == (255,255,255):
                            px_new[j,i] = tmp     
    return ret_img

def binary_generator():
    while True:
        yield str(randint(0,1))
        
if __name__ == '__main__':  
    ht = time()
    hd_bitpic(Image.open("input.jpg"),binary_generator(),scale=4,font_size=14,spacing=14).save("b_output.jpg")
    print(time()-ht)    


    
