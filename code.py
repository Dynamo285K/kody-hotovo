from PIL import Image
message = "Ahoj svet"
obr = Image.open("nature.png")
pixels = obr.load()

lenght = 8

def make_zeroes (message:str)->list:
    res = [11]
    for letter in message:
        number = bin(ord(letter))[2::]
        pn = lenght - len(number)
        number = pn *"0" + number
        print(number)
        for j in number:
            res.append(int(j))
    return res

def drticka(message):
    mes_in_bin = make_zeroes (message)
    for i in range (len (mes_in_bin)):
        #toto tam ideme pchat[i]
        width = obr.size[0]
        height = obr.size [1]
        x = i % width
        y = i // width
        pixelblue = pixels[x,y][2]
        newblue = int(bin(pixelblue)[2:-1:] + str(mes_in_bin[i]), 2)
        newcolor = (pixels[x, y][0], pixels[x, y][1], newblue)
        print(pixels[x,y], newcolor)
        pixels[x,y] = newcolor
    obr.save("pic_with_message1.png")

drticka(message)