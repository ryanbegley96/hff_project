import pandas as pd
import subprocess

bands = ['f105w','f125w','f140w','f160w','f435w','f606w','f814w']
apertures = ['3.2','3.5','3.9','4.1','3.3','3.3','3.3']

for band, aper in zip(bands,apertures):
    subprocess.call('sex hff_abells1063-hffpar_f160w_microJy_backsub.fits,hff_abells1063-hffpar_'+band+'_microJy_backsub.fits -c default.sex -PARAMETERS_NAME default.param -CATALOG_NAME detect_f160w_'+band+'.cat -CHECKIMAGE_TYPE NONE -CHECKIMAGE_NAME detect_f160w_'+band+'_CHECK.fits -PHOT_APERTURES '+aper, shell='true')
    df = pd.read_table('detect_f160w_'+band+'.cat', sep='\s+', header= None, names=['ID','XCEN','YCEN','RA','DEC',band+'_FLUX',band+'_FLUX_ERR',band+'_FLUX_ISO',band+'_FLUX_ERR_ISO'])
    df.to_csv('detect_f160w_'+band+'.csv', index=False, sep = ',')
