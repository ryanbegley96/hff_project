import numpy as np
import astropy.io.fits as pyfits
from pyraf import iraf
from iraf import noao,artdata,starlist,mkobjects,digiphot,apphot,phot,artdata,starlist,mkobjects,txdump,stsdas,images,immatch,psfmatch, imutil, imarith
import subprocess
#Setting up microJy


#for band in ['f435w','f606w','f814w']:

#    head = pyfits.open('hlsp_frontier_hst_acs-60mas-selfcal_abells1063-hffpar_' + band + '_v1.0-epoch2_drz.fits')[0].header
#    flam = float(head['PHOTFLAM'])
#    plam = float(head['PHOTPLAM'])
#    ZP = -2.5*(np.log10(flam)) - 5 * (np.log10(plam))-2.408
#    print band + '     ' + str(ZP)
    
#    iraf.imutil.imarith(operand1='hlsp_frontier_hst_acs-60mas-selfcal_abells1063-hffpar_' + band + '_v1.0-epoch2_drz.fits',op='*',operand2=str(10**((23.9-ZP)/2.5)),result='hff_abells1063-hffpar_' + band + '_microJy.fits')   
#    iraf.imutil.imarith(operand1='hlsp_frontier_hst_acs-60mas-selfcal_abells1063-hffpar_' + band + '_v1.0-epoch2_rms.fits', op = '*', operand2=str(10**((23.9-ZP)/2.5)), result='hff_abells1063-hffpar_' + band + '_rms_microJy.fits')

#for band in ['f105w','f125w','f140w','f160w']:

#    head = pyfits.open('hlsp_frontier_hst_wfc3-60mas-bkgdcor_abells1063-hffpar_' + band + '_v1.0-epoch1_drz.fits')[0].header
#    flam = float(head['PHOTFLAM'])
#    plam = float(head['PHOTPLAM'])
#    ZP = -2.5*(np.log10(flam)) - 5 * (np.log10(plam))-2.408
#    print band + '     ' + str(ZP)
    
#    iraf.imutil.imarith(operand1='hlsp_frontier_hst_wfc3-60mas-bkgdcor_abells1063-hffpar_' + band + '_v1.0-epoch1_drz.fits',op='*',operand2=str(10**((23.9-ZP)/2.5)),result='hff_abells1063-hffpar_' + band + '_microJy.fits')   
#    iraf.imutil.imarith(operand1='hlsp_frontier_hst_wfc3-60mas-bkgdcor_abells1063-hffpar_' + band + '_v1.0-epoch1_rms.fits', op = '*', operand2=str(10**((23.9-ZP)/2.5)), result='hff_abells1063-hffpar_' + band + '_rms_microJy.fits')

for band in ['f435w','f606w','f814w','f105w','f125w','f140w','f160w']:
	subprocess.call('sextractor hff_abells1063-hffpar_' + band + '_microJy.fits -c ../hff.sex -PARAMETERS_NAME ../sky.param -CATALOG_NAME test.cat -CHECKIMAGE_TYPE -BACKGROUND -CHECKIMAGE_NAME hff_abells1063-hffpar_' + band + '_microJy_backsub.fits -FILTER_NAME ../gauss_2.5_5x5.conv',shell='true')
