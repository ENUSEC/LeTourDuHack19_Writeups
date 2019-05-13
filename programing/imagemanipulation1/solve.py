from PIL import Image

def open(x,y, pix):
	tup = pix[x,y]  # Get the RGBA Value of the a pixel of an image
	if(tup[0] == 255):
		return "0"
	else:
		return "1"

im = Image.open('matrix.png') # Can be many different formats.
pix = im.load()
bin=""
for y in range(1,232):
        for i in range(1,234):
                bin += open(i,y, pix)
fin = ""
im.close()

bin += "0" # This is the stream of pixel, using this we can work out the offset is 1 pixel, and therefore in order to fix the stream we just append a 0 onto the end 

# Now we have a stream we know it is 53824 bytes in length
# The square root of 53824 is 232 -> Therefore the QR code is 232 by 232

#print(bin)
#print(len(bin))


# Now we write the stream to another image removing the offset of 1 pixel
black = (0,0,0)
white = (255,255,255)
img = Image.new('RGB', (250, 250), color = white)
img.save("new.png")
img = Image.open("new.png")
pix = img.load()
count = 0
print(len(bin))
for y in range(1,233): # 232 -> I add a 1 pixel offset so it looks nice
        print("New line")
        for x in range(1,233): # 232 -> I add a 1 pixel offset so it looks nice
                print("Co ordinates: " + str(x) + "," + str(y))
		if(bin[count] == "1"):
			print("Color = Black")
         		pix[x,y] = black
		elif(bin[count] == "0"):
			print("Color = White")
			pix[x,y] = white

		count += 1

img.save("new.png")
img.close()
