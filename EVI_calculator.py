#Import system modules
import arcpy
from arcpy.sa import *

#Activate Spatial Analyst
arcpy.CheckOutExtension("Spatial")

#Set workspace
arcpy.env.workspace = "C:\Personal\ArcGIS\Projects"

#Set near-infrared, red , and blue band inputs
nirBand = Float(Raster("in_raster.tif\Band_4"))
redBand = Float(Raster("in_raster.tif\Band_1"))
bluBand = Float(Raster("in_raster.tif\Band_3"))

#Calculate Enhanced Vegetation Index
outraster = (nirBand - redBand) / (nirBand + redBand - bluBand)
outraster.save("EVI.tif")
