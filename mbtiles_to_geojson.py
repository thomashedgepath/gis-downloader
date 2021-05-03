from download import download_from_arcmap
from convert import mbtiles_to_geojsontiles

TIPPECANOE_DIR = '/usr/local/bin/'

#url = 'https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/TxDOT_City_Boundaries/FeatureServer/0'
geojson_directory = "/Users/thomashedgepath/Documents/GitHub/ArcGIS Rest API/geojson"
mbtiles_directory = "/Users/thomashedgepath/Documents/GitHub/ArcGIS Rest API/mbtiles"


#output_filename = download_from_arcmap(url, geojson_directory)
geojson_path = geojson_directory + "/" + output_filename + ".geojson"
mbtiles_path = mbtiles_directory + "/" + output_filename + ".mbtiles"

#This can take multiple geojson files as layers. 
mbtiles_to_geojsontiles(
    filepaths=[geojson_path],
    tippecanoe_dir=TIPPECANOE_DIR,
    mbtiles_file=mbtiles_path,
)

