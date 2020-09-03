import json
import time
from esridump.dumper import EsriDumper

d = EsriDumper('https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/Texas_County_Boundaries_Detailed/FeatureServer/0', timeout=300)

file_txt = """{"type": "FeatureCollection","features":["""
start_time = time.time()


# Iterate over each feature
index = 0
feature_count = d.get_feature_count()
print(feature_count)
# print(d.get_metadata())

all_features = list(d)

for feature in all_features:
   index += 1
   
   if index == 1:
   #    # if above is true that should mean were on the last feture in the set, so dont add ",\n" to the end - add closing brackets
   #    file_txt = file_txt + json.dumps(feature) + "]}"
      property_dict = feature['properties']
      for key, value in property_dict:
         print(key,value)
   # else:
   #    file_txt = file_txt + json.dumps(feature) + ",\n"
   #print(feature)

   print(time.time() - start_time, end="\r", flush=True)




# Or get all features in one list

#print(file_txt)

# with open('counties.json', 'w') as outfile:
#     outfile.write(file_txt)
#     # json.dumps(d.get_metadata())