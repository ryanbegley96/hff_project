import numpy as np
import astropy.io.fits as pyfits
from pyraf import iraf
from iraf import noao, digiphot, apphot, phot, txdump
import matplotlib
from matplotlib import pyplot as plt

iraf.noao.digiphot.apphot.phot.interac='no'
iraf.noao.digiphot.apphot.phot.centerp.calgori='none'
iraf.noao.digiphot.apphot.phot.fitskypars.salgori='constant'
iraf.noao.digiphot.apphot.phot.cache='yes'
iraf.noao.digiphot.apphot.phot.salgori='constant'

for band, aperture in zip(['f105w','f125w','f140w','f160w','f435w','f606w','f814w'], ['3.2','3.5','3.9','4.1','3.3','3.3','3.3']):
    iraf.noao.digiphot.apphot.phot.photpar.apertur=aperture
    iraf.phot(image='SEG_' + band + '_sex_hff_abells1063_par_CHECK.fits', interactive='no',calgorithm='none', salgori='constant',coords='box_coords_' + band + '.coo', output='PHOT_SEG_hff_abells1063_par_' + band + '.txt',verify='no')
    iraf.txdump(textfile='PHOT_SEG_hff_abells1063_par_' + band + '.txt', fields='XCEN, YCEN, SUM', expr='yes', Stdout='PHOT_SEG_hff_abells1063_par_' + band + '_OUTFILE.txt')
