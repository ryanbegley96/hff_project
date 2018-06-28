import numpy as np
import astropy.io.fits as pyfits
from pyraf import iraf
from iraf import noao, digiphot, apphot, phot, txdump
import matplotlib
from matplotlib import pyplot as plt

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

radii_pts = file_len("radii.txt")
print radii_pts

iraf.noao.digiphot.apphot.phot.interac='no'
iraf.noao.digiphot.apphot.phot.centerp.calgori='none'
iraf.noao.digiphot.apphot.phot.photpar.apertur='radii.txt'
iraf.noao.digiphot.apphot.phot.fitskypars.salgori='constant'
iraf.noao.digiphot.apphot.phot.cache='yes'
iraf.noao.digiphot.apphot.phot.salgori='constant'
iraf.phot(image='hff_abells1063-hffpar_f814w_microJy_backsub.fits', interactive='no',calgorithm='none', salgori='constant',coords='coords.coo', apertures='radii.txt', output='test.txt',verify='no')


iraf.txdump.textfile='test.txt'
iraf.txdump.expr='yes'

iraf.txdump(textfile='test.txt', fields='SUM',expr='yes',Stdout='stuff.txt')

def tidy_txdump(filename,band):
    radii = np.loadtxt("radii.txt")
    data = np.loadtxt(filename)
    a = np.array([data])
    b = a.T
    b = b.reshape(radii_pts,1)
    radii = np.array([radii])
    radii = radii.reshape(radii_pts,1)
    c = np.hstack((radii,b/np.max(b)))
    np.savetxt("out_" + band + ".txt",c)

    d = b/np.max(b)

    plt.plot(radii,d)

    plt.title('Flux versus Radius')
    plt.xlabel('Aperture radius')

    plt.xticks(np.arange(0,32,2.0))
    plt.yticks(np.arange(0,1.5,0.05))
    plt.ylabel('Enclosed flux (counts)')
    plt.grid(b=True, which='both')
    plt.savefig('fluxradiusplot_' + band + '_huh.png')
    print "Flux vs Radius plot has been saved in the folder"

tidy_txdump('stuff.txt','f814w')
