from PIL import Image

pic = Image.open("pic_with_message1.png")
pic2 = Image.open("pic_with_message2.png")
pixels = pic.load()
color = []
width = pic.size[0]
height = pic.size[1]

def decode(pic, pic2):
    message = ""
    end1= []
    end2= ""
    end3 = ""
    lenght = 0
    for i in range(0, width):
        lenght += 1
        x = i % width
        y = i // width
        color = pixels[x, y]
        if "00100011" in message:
            break
        else:
            if color[2]%2 !=0:
                message += "1"
            elif color[2]%2 == 0:
                message += "0"


    end3 = str(message.zfill(lenght - 1))
    n = 8
    end1 = [end3[i:i + 8] for i in range(0, len(end3), 8)]
    print(*end1)

decode("pic_with_message1.png", "pic_with_message2.png")