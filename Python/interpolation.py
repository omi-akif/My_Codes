#!wget http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_55_08.zip #SE

#unzip srtm.zip

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from osgeo import gdal
from scipy.interpolate import griddata

filename = "srtm_55_08.tif"
gdal_data_ = gdal.Open(filename)

#gdal_band_ = gdal_data_.GetRasterBand(1)

#gdal_band_ = gdal_data_.GetRasterBand(1)

data_arr = gdal_data_.ReadAsArray().astype(np.float)

data_arr[data_arr<0] = 0

row_mean = np.nanmean(data_arr, axis=1)
indice = np.where(np.isnan(data_arr))
data_arr[indice] = np.take(row_mean, indice[1])
#elevation data

Xcolumn = gdal_data_.RasterXSize
Ycolumn = gdal_data_.RasterYSize

geotransform = gdal_data_.GetGeoTransform()
XOrigin = geotransform[0]
YOrigin = geotransform[3]

pixelWidth = geotransform[1]
pixelHeight = geotransform[5]

lons = XOrigin + np.arange(0, Xcolumn)*pixelWidth #longitude
lats = YOrigin + np.arange(0, Ycolumn)*pixelHeight #latitude

x_arr = np.linspace(np.min(lons), np.max(lons), 50)
y_arr = np.linspace(np.min(lats), np.max(lats), 50)
#z_arr = np.linspace(np.min(data_arr), np.max(data_arr), 100)

x_mesh, y_mesh = np.meshgrid(x_arr, y_arr)

z_mesh = griddata((lons, lats), data_arr, (x_mesh, y_mesh), method='linear')