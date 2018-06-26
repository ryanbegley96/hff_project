import numpy as np
import math
import matplotlib.pyplot as plt
import hff_functions as hf

hf.aper_diameter("Abell370/hff_abell370_f105w_aperture_data_star2.csv",7,70,3.,"f105w")
hf.aper_diameter("Abell370/hff_abell370_f125w_aperture_data_star2.csv",7,70,5.,"f125w")
hf.aper_diameter("Abell370/hff_abell370_f140w_aperture_data_star2.csv",7,70,5.,"f140w")
hf.aper_diameter("Abell370/hff_abell370_f160w_aperture_data_star2.csv",7,70,5.,"f160w")
hf.aper_diameter("Abell370/hff_abell370_f435w_aperture_data_star2.csv",8,80,0.03,"f435w")
hf.aper_diameter("Abell370/hff_abell370_f606w_aperture_data_star2.csv",7,80,0.25,"f606w")
hf.aper_diameter("Abell370/hff_abell370_f814w_aperture_data_star2.csv",7,80,0.8,"f814w")









"""
#abell370_f105w_aper_data w/ x&y being aperture radius & aper sum
abell370_f105w_aper_data_x, abell370_f105w_aper_data_y = np.loadtxt("Abell370/hff_abell370_f105w_aperture_data.csv", delimiter=",", unpack=True)

#fitting a polynomial for psf - should be power law but fits ok at appropiate section
aper_fig_fit = np.polyfit(abell370_f105w_aper_data_x, abell370_f105w_aper_data_y, 7)
aper_fig_fit_line = np.poly1d(aper_fig_fit)
abell370_f105w_aper_data_x_fit = np.linspace(abell370_f105w_aper_data_x[0], abell370_f105w_aper_data_x[-1], 1000)
abell370_f105w_aper_data_y_fit = aper_fig_fit_line(abell370_f105w_aper_data_x_fit)

plateau_flux = np.max(abell370_f105w_aper_data_y) #look at more carefully
percent_plateau_flux = 0.7*plateau_flux #chose percentage
tolerance = 50
aper_pix = np.extract(abs(abell370_f105w_aper_data_y_fit - percent_plateau_flux) < tolerance, [abell370_f105w_aper_data_x_fit,abell370_f105w_aper_data_y_fit])
print np.min(aper_pix)


plt.figure(1)
plt.plot(abell370_f105w_aper_data_x, abell370_f105w_aper_data_y, linewidth=1, marker='o', mfc='r')
plt.plot(abell370_f105w_aper_data_x_fit, abell370_f105w_aper_data_y_fit, linewidth=1)
plt.title("Aperture radius against aperture Flux")
plt.show()
"""
