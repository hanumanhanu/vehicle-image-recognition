from PIL import Image

width = 224
height = 224
i = 1

#resize test images
# while i <= 50:
# 	img = Image.open("v_data/test/boats/%s.jpg" % (i))
# 	img2 = img.resize((width, height), Image.NEAREST).convert('RGB')
# 	img2.save("%s.jpg" % (i))
# 	print("resized %s.jpg" % (i))
# 	i+= 1

#resize train images
while i <= 200:
	img = Image.open("v_data/train/boats/%s.jpg" % (i))
	img2 = img.resize((width, height), Image.NEAREST).convert('RGB')
	img2.save("%s.jpg" % (i))
	print("resized %s.jpg" % (i))
	i+= 1