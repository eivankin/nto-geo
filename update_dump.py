import geopandas as gpd
from request_helper import APIRequestHelper
from geojson_pydantic import FeatureCollection

batch_size = 20

trees = gpd.read_file('data/dump_filtered_30200.geojson')
ids = trees['id'].values

batch_count = int(len(ids) / batch_size) + int(len(ids) % batch_size != 0)

helper = APIRequestHelper("http://192.168.1.62:8888/mapservices/oodb")

objects = []
for i_batch in range(batch_count):
    i_begin = i_batch * batch_size
    i_end = (i_batch * batch_size) + batch_size if i_batch != batch_count - 1 else len(ids)

    ids_batch = ids[i_begin:i_end]
    ids_batch_str = str(ids_batch[0]) + ''.join(','+str(i) for i in ids_batch[1:])

    objects.extend(helper.load_object(ids=ids_batch_str))

fc = FeatureCollection(features=objects)
fc_json = fc.json(exclude_none=True, by_alias=True)

with open('data/dump_update.geojson', 'w') as f:
    f.write(fc_json)
