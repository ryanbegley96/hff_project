import numpy as np
import astropy.io.fits as pyfits
from pyraf import iraf
from iraf import noao, digiphot, apphot, phot, txdump
import matplotlib
from matplotlib import pyplot as plt

iraf.noao.digiphot.apphot.phot.interac='no'
iraf.noao.digiphot.apphot.phot.centerp.calgori='none'
iraf.noao.digiphot.apphot.phot.photpar.apertur='3.9'
iraf.noao.digiphot.apphot.phot.fitskypars.salgori='constant'
iraf.noao.digiphot.apphot.phot.cache='yes'
iraf.noao.digiphot.apphot.phot.salgori='constant'

iraf.phot(image='hff_abells1063-hffpar_f140w_wht.fits', interactive='no',calgorithm='none', salgori='constant',coords='box_coords_f140w.coo', output='PHOT_WHT_hff_abells1063_par_f140w.txt',verify='no')

iraf.txdump(textfile='PHOT_WHT_hff_abells1063_par_f140w.txt', fields='XCEN, YCEN, SUM', expr='yes', Stdout='PHOT_WHT_hff_abells1063_par_f140w_OUTFILE.txt')
