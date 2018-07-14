#code to write coordinates of grid of apertures in 100x100 box to file - eg for apertures of size 0.5 : 0.5 0.5 \n 1.5 0.5 etc

outFile = open('box_coords_ACS.coo', 'w')
for i in range(1, 1637, 2):
	for j in range(1, 1637, 2):
		outFile.write(str(i*3.3)+' '+str(j*3.3)+'\n')
outFile.close()
