from osgeo import gdal,osr

# Read Raster with gdal
raster_1 = gdal.Open('EXAMPLE_RASTER_LOCATION.tif')

# Getting Raster Projection & Spatial Reference System
raster_prj = raster_1.GetProjection()
print(raster_prj)

srs = osr.SpatialReference(wkt=raster_prj)
if srs.IsProjected:
    print(srs.GetAttrValue('projcs'))
print(srs.GetAttrValue('geogcs'))


# Getting Raster Pixel Resolution

gt = raster_1.GetGeoTransform()
print(gt)

## GDAL documentation states GT(1) is pixel width, and GT(5) is pixel height
pixelSizeX = gt[1]
pixelSizeY =-gt[5]


print("pixelSizeX:",pixelSizeX,"m")
print("pixelSizeX:",pixelSizeY,"m")
