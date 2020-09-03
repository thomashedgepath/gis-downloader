import json
import time
from esridump.dumper import EsriDumper
from tqdm import tqdm
from urllib.parse import urlsplit, urlunsplit
import datetime

today = datetime.datetime.now()


url = 'https://maps.mckinneytexas.org/mckinney/rest/services/OpenData/Planning_Zoning/MapServer/4'

split = urlsplit(url)

filename_str = today.strftime("%Y-%m-%d_%H:%M:%S") + split.path.replace("/",".") + ".geojson"
#print(filename_str)

d = EsriDumper(url, timeout=300)

start_string = """{"type": "FeatureCollection","features":"""
end_string = "]}"

start_time = time.time()


# Iterate over each feature

index = 0
feature_count = d.get_feature_count()
print(str(feature_count) + " total Features")
#print(d.get_metadata())

all_features = []
with tqdm(total=feature_count) as pbar:
   #all_features = list(d)
   #file_txt = json.dumps(all_features)

   for feature in d:
      #print(type(all_features[index]))
      #index += 1
      all_features.append(feature)
      # if index == feature_count:
      #    # if above is true that should mean were on the last feture in the set, so dont add ",\n" to the end - add closing brackets
      #    #file_txt = file_txt + json.dumps(feature) + "]}"
      #    pass
      # else:
      #    pass
         #file_txt = file_txt + json.dumps(feature) + ",\n"
      pbar.update(1)
      #print(time.time() - start_time, end="\r", flush=True)

file_txt = json.dumps(all_features)
file_txt = start_string + file_txt + end_string
#print(type(file_txt))

with open(filename_str, 'w') as outfile:
    outfile.write(file_txt)
    json.dumps(d.get_metadata())