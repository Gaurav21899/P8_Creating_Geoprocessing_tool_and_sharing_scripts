import arcpy
import os

# Define our inputs

fc_input_path = arcpy.GetParameterAsText(0)
output_type = arcpy.GetParameterAsText(1)
output_folder = arcpy.GetParameterAsText(2)
file_name = arcpy.GetParameterAsText(3)

arcpy.MakeFeatureLayer_management(fc_input_path,"fc_layer")

if output_type == "KMZ":
out_kmz_file = "{}.KMZ".format(file_name)
full_output_kmz_path = os.path.join(output_folder, out_kmz_file)
arcpy.conversion.LayerToKML("fc_layer", full_output_kmz_path)
arcpy.AddMessage("Exported successfully to KMZ")


elif output_type == "EXCEL":
out_excel_file = "{}.xlsx".format(file_name)
full_output_excel_path = os.path.join(output_folder, out_excel_file)
arcpy. TableToExcel_conversion("fc_layer", full_output_excel_path)
arcpy.AddMessage("Exported successfully to EXCEL")


elif output_type == "SHP":
out_shp_file = "{}.shp".format(file_name)
full_output_shp_path = os.path.join(output_folder, out_shp_file)
arcpy.conversion. FeatureClassToShapefile(" fc_layer",full_output_shp_path)
arcpy.AddMessage("Exported successfully to SHAPEFILE")