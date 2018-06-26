import numpy as np
import math
import matplotlib.pyplot as plt

def aper_diameter(csv_filename, polynomial_order, percentage_flux, tolerance, filter):
    data_x, data_y = np.loadtxt(csv_filename, delimiter=",", unpack=True)

    aper_fig_fit = np.polyfit(data_x, data_y, polynomial_order)
    aper_fig_fit_line = np.poly1d(aper_fig_fit)
    data_x_fit = np.linspace(data_x[0], data_x[-1],100)
    data_y_fit = aper_fig_fit_line(data_x_fit)

    plateau_flux = np.max(data_y)
    percent_plateau_flux = percentage_flux*plateau_flux/100.0
    #print percent_plateau_flux
    aper_pix = np.extract(abs(data_y_fit - percent_plateau_flux) < tolerance, [data_x_fit, data_y_fit])
    print("The aperture diameter for the "+str(filter)+" is "+str(aper_pix*2.0*0.06)+" arcsec")
    plt.figure(filter)
    plt.plot(data_x,data_y,marker='o',mfc='r', linewidth=1)
    plt.plot(data_x_fit,data_y_fit,linewidth=1)
    plt.show()
    return
