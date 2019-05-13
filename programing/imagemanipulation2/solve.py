from PIL import Image

def open(x,y, pix):
	tup = pix[x,y]  # Get the RGBA Value of the a pixel of an image
	if(tup[0] == 255):
		return "0"
	else:
		return "1"
# Get the first row
im = Image.open('chall.png') # Can be many different formats.
pix = im.load()
# 274 x 72
fin = ""
bin = ""
for y in range(72):
	# 34, 236
	bin = ""
        for x in range(34,236):
                bin += open(x,y, pix)
	#print(bin)
	fin += "1111111111111111001100110011000000" + bin[::-1] + "00111111111111110011000000110011000011" # Add the header and footer to the line which is reversed
im.close()
bin = fin
print(bin)

# Now we write the stream to another image
black = (0,0,0)
white = (255,255,255)
img = Image.new('RGB', (274, 72), color = white)
img.save("fin.png")
img = Image.open("fin.png")
pix = img.load()
count = 0
print(len(bin))
for y in range(72):
        for x in range(274):
		if(bin[count] == "1"):
               		pix[x,y] = black
		elif(bin[count] == "0"):
			pix[x,y] = white
		count += 1

img.save("fin.png")
img.close()
