# EVIcalc

Script for ArcGIS that performs a raster calculation of Enhanced Vegetation Index (EVI) from a multispectral image.

Enhanced Vegetation Index is a calculation using data from multiple spectral bands- In this case: Red, blue, and near infrared light (NIR).  It represents comparative levels of vegetative health and photosynthetic activity, and can be useful in agricultural and environmental fields of study.

The formula used to calculate EVI by the program is as follows:

EVI = (NIR - RED) / (NIR + RED - BLUE)

The two images located in this repository provide an example of an EVI calculation performed by the program.
