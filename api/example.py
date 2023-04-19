from request_helper import APIRequestHelper
from util import filter_by_class, get_class_id_by_name
from geojson_pydantic import Polygon, Feature
from api_models import ObjectProperties, ObjectResponse

if __name__ == '__main__':
    helper = APIRequestHelper("http://192.168.1.62:8888/mapservices/oodb")
    catalog = helper.get_catalog()
    tree_class = get_class_id_by_name(".*Древесн.*", catalog)
    #print(tree_class)
    #filtered = filter_by_class(str(tree_class), helper.load_object(bbox="34.85542678861543,66.06507873609485,39.760146455994175,67.71469879171593"))
    #print(len(filtered))
    print(f'last_commit {helper.get_last_commit_id()}\n')

    print('save')
    geom = Polygon(coordinates=[[[30.87485, 59.830497], [30.87485, 59.838081], [30.896658, 59.838081], [30.896658, 59.830497], [30.87485, 59.830497]]])
    props = ObjectProperties(class_code=30200, feature_ID=0, **{'013': 'adkfbdhvb'})
    object_response = ObjectResponse(features=[Feature(geometry=geom, properties=props)])
    #save_res = helper.save_object(object_response); print(save_res)
    print(f'last_commit {helper.get_last_commit_id()}\n')

    print('update')
    update_id = 3166152
    object_response = helper.load_object(ids=update_id)
    object_response.features[0].geometry = Polygon(coordinates=[[[30.896658, 59.838081], [30.896658, 59.845633], [30.929458, 59.845633], [30.929458, 59.838081], [30.896658, 59.838081]]])
    #print(object_response.json(exclude_none=True, by_alias=True))
    #save_res = helper.save_object(object_response); print(save_res)
    #updated_object = helper.load_object(ids=update_id)
    #print(updated_object.json(exclude_none=True, by_alias=True))
    print(f'last_commit {helper.get_last_commit_id()}\n')

    print('remove')
    remove_id = 3166147
    #remove_res = helper.remove_objects([remove_id]); print(remove_res)
    print(f'last_commit {helper.get_last_commit_id()}\n')
