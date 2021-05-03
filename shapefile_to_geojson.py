import shapefile
from tqdm import tqdm
# read the shapefile
reader = shapefile.Reader("/Users/thomashedgepath/PythonScripts/Mapbox/parcels_with_appraisal_data_R5-8/parcels.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in tqdm(reader.shapeRecords()):
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
    geometry=geom, properties=str(atr))) 

# write the GeoJSON file
from json import dumps
geojson = open("thebigone.json", "w")
geojson.write(dumps({"type": "FeatureCollection","features": buffer}, indent=2) + "\n")
geojson.close()

