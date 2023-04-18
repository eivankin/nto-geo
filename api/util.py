import re

from data import ObjectResponse, CatalogResponse
from geojson_pydantic import Feature
from tqdm import tqdm


def filter_by_class(class_regex: str, all_objects: ObjectResponse) -> list[Feature]:
    return [
        feature
        for feature in tqdm(all_objects.features, desc='feats')
        if re.fullmatch(class_regex, feature.properties.class_code)
    ]


def get_class_id_by_name(class_name_regex: str, catalog: CatalogResponse) -> str:
    for class_id, class_info in catalog.classes.items():
        if re.fullmatch(class_name_regex, class_info.alias):
            return class_id
    raise KeyError('class not found')
