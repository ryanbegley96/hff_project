import pandas as pd

for type in ['IMAGE','WHT','SEG']:
    for band in ['f105w','f125w','f140w','f160w','f435w','f606w','f814w']:
        df = pd.read_csv('PHOT_' + type + '_hff_abells1063_par_' + band + '_OUTFILE.txt', delim_whitespace=True, header=None, names=['#XCEN','YCEN',type+'FLUX'])
        df.to_csv('/Disk/ds-sopa-ifa/s1508137/HFF_2018/AbellS1063_parallel/hff_abells1063_hffpar_global_depth_catalogs/PHOT_' + type + '_hff_abells1063_par_' + band + '_OUTFILE.csv', index=False, sep = ',')
