from request_helper import APIRequestHelper
from util import filter_by_class, get_class_id_by_name

if __name__ == '__main__':
    helper = APIRequestHelper("http://192.168.1.62:8888/mapservices/oodb")
    catalog = helper.get_catalog()
    tree_class = get_class_id_by_name(".*Древесн.*", catalog)
    print(tree_class)
    filtered = filter_by_class(str(tree_class), helper.load_object(
        bbox="34.85542678861543,66.06507873609485,39.760146455994175,67.71469879171593"))
    print(len(filtered))
