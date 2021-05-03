from download import download_from_arcmap
from convert import geojson_to_mbtiles

TIPPECANOE_DIR = '/usr/local/bin/'

url = input("MapServer URL:")
geojson_directory = "/Users/thomashedgepath/Documents/GitHub/ArcGIS Rest API/geojson"
mbtiles_directory = "/Users/thomashedgepath/Documents/GitHub/ArcGIS Rest API/mbtiles"


output_filename = download_from_arcmap(url, geojson_directory)
#output_filename = "2020-09-15_15:37:39.arcgis.rest.services.Parcels.MapServer.0"
geojson_path = geojson_directory + "/" + output_filename + ".geojson"
mbtiles_path = mbtiles_directory + "/" + output_filename + ".mbtiles"

#This can take multiple geojson files as layers. 
geojson_to_mbtiles(
    filepaths=[geojson_path],
    tippecanoe_dir=TIPPECANOE_DIR,
    mbtiles_file=mbtiles_path,
)

