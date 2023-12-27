import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P8_Creating_Geoprocessing_tool_and_sharing_scripts\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"

# Inputs

x_cord = arcpy.GetParameterAsText(0)
y_cord = arcpy.GetParameterAsText(1)
Output_fc_name = arcpy.GetParameterAsText(2)

fc_path = os.path.join(gdb_path, Output_fc_name)
# Point Object
pnt_obj = arcpy.Point(x_cord, y_cord)

# Spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Point Geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

arcpy.CopyFeatures_management(pnt_geom, fc_path)

print("Process Completed")