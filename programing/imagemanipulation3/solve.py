from PIL import Image
# Flip the bits from black to white and visa versa
# Leave the L shaped border black

def open(x,y, pix):
	tup = pix[x,y]  # Get the RGBA Value of the a pixel of an image
	if(tup[0] == 255):
		return "1"
	else:
		return "0"

# Get the first row
im = Image.open('chall.png') # Can be many different formats.
pix = im.load()
# 274 x 72
fin = ""
bin = ""
for y in range(84):
	# 34, 236
	bin += "1111"
        for x in range(4,88):
                bin += open(x,y, pix)

#print(bin)
bin += "1" * (88*4)
im.close()
print(bin)

# Now we write the stream to another image but add an offset
black = (0,0,0)
white = (255,255,255)
img = Image.new('RGB', (88, 88), color = white)
img.save("solve.png")
img = Image.open("chall.png")
pix = img.load()
count = 0
print(len(bin))
for y in range(88):
        print("New line")
        for x in range(88):
               # print("Co ordinates: " + str(x) + "," + str(y))
                print("Count" +str(count))
                #for t in range(16):
		if(bin[count] == "1"):
               		pix[x,y] = black
		elif(bin[count] == "0"):
			pix[x,y] = white

		count += 1

img.save("solve.png")
img.close()
