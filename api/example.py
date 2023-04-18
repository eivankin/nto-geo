from request_helper import APIRequestHelper
from util import filter_by_class, get_class_id_by_name
from geojson_pydantic import Polygon, Feature
from api_models import ObjectProperties, ObjectResponse

if __name__ == '__main__':
    helper = APIRequestHelper("http://192.168.1.62:8888/mapservices/oodb")
    catalog = helper.get_catalog()
    tree_class = get_class_id_by_name(".*Древесн.*", catalog)
    print(tree_class)
    filtered = filter_by_class(str(tree_class), helper.load_object(
        bbox="34.85542678861543,66.06507873609485,39.760146455994175,67.71469879171593"))
    print(len(filtered))

    print(helper.get_last_commit_id())

    geom = Polygon(coordinates=[[[30.551342, 60.013808], [30.551342, 60.017778], [30.560372, 60.017778], [30.560372, 60.013808], [30.551342, 60.013808]]])
    props = ObjectProperties(class_code=30200, feature_ID=0)
    object_response = ObjectResponse(features=[Feature(geometry=geom, properties=props)])
    #save_res = helper.save_object(object_response); print(save_res)

    update_id = 3166142
    geom = Polygon(coordinates=[[[30.5, 60.0], [30.5, 60.1], [30.6, 60.1], [30.6, 60.0], [30.5, 60.0]]])
    props = ObjectProperties(class_code=30200, feature_ID=update_id)
    object_response = ObjectResponse(features=[Feature(geometry=geom, properties=props)])
    #save_res = helper.save_object(object_response); print(save_res)
    #updated_object = helper.load_object(ids=update_id)
    #print(updated_object)

    remove_id = 3166144
    #remove_res = helper.remove_objects([remove_id]); print(remove_res)

    
