from abc import ABC, abstractmethod
from typing import Any
from pydantic import parse_obj_as, BaseModel
from requests import Response

from api_models import CatalogResponse, ObjectResponse
from requests import get, post


class RequestHelper(ABC):
    def get_catalog(self) -> CatalogResponse:
        return parse_obj_as(CatalogResponse, self.do_raw_request(apioodbtype="catalog").json())

    def load_object(self, **kwargs) -> ObjectResponse:
        response = self.do_raw_request(apioodbtype="loadobj", **kwargs)
        assert response.ok, response
        return parse_obj_as(ObjectResponse, response.json())

    def save_object(self, model: ObjectResponse, **kwargs) -> bool:
        return self.do_raw_request(model, apioodbtype="saveobj", **kwargs).ok

    def remove_objects(self, ids, **kwargs):
        ids_str = str(ids[0]) + ''.join(','+str(i) for i in ids[1:])
        return self.do_raw_request(apioodbtype="remobj", ids=ids_str, **kwargs).ok
    
    def get_last_commit_id(self):
        return self.do_raw_request(apioodbtype="lastcommit").json()['LastCommitID']

    @abstractmethod
    def do_raw_request(self, data: BaseModel | None = None, **kwargs: Any) -> Response:
        pass


class APIRequestHelper(RequestHelper):
    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url

    def do_raw_request(self, data: BaseModel | None = None, **kwargs: Any) -> Response:
        params = dict(**kwargs, request="apioodb", version="1.0.0")
        if data is None:
            return get(self.endpoint_url, params=params)
        return post(self.endpoint_url, data=data.json(exclude_unset=True, by_alias=True), params=params)
