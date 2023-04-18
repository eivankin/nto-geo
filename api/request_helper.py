from abc import ABC, abstractmethod
from typing import Any
from pydantic import parse_obj_as, BaseModel
from requests import Response

from api.data import CatalogResponse, ObjectResponse, SaveObject
from requests import get, post


class RequestHelper(ABC):
    def get_catalog(self) -> CatalogResponse:
        return parse_obj_as(CatalogResponse, self.do_raw_request(apioodbtype="catalog").json())

    def load_object(self, **kwargs) -> ObjectResponse:
        return parse_obj_as(ObjectResponse,
                            self.do_raw_request(apioodbtype="loadobj", **kwargs).json())

    def save_object(self, model: SaveObject, **kwargs) -> bool:
        return self.do_raw_request(model, apioodbtype="saveobj", **kwargs).ok

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
        return post(self.endpoint_url, json=data.json(), params=params)
