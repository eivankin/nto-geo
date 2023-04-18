from abc import ABCMeta

from pydantic import BaseModel, BaseConfig
from humps import camelize
from geojson_pydantic import FeatureCollection, Polygon, Point, LineString, MultiLineString


class CamelCaseConfig(BaseConfig):
    allow_population_by_field_name = True
    alias_generator = camelize


class AbstractCamelCaseModel(BaseModel, metaclass=ABCMeta):
    class Config(CamelCaseConfig):
        orm_mode = True


class ClassInfo(AbstractCamelCaseModel):
    alias: str
    attributes: list[int]
    class_code: str
    draw_order: int
    name: str
    parent: str


class DomainInfo(AbstractCamelCaseModel):
    type: int
    vals: dict[str, str]


class AttributeInfo(AbstractCamelCaseModel):
    alias: str
    default_value: str | None
    key: str
    max_length: int | None
    name: str
    precision: int
    type: int
    domain: DomainInfo | None


class CatalogResponse(AbstractCamelCaseModel):
    attributes: dict[str, AttributeInfo]
    classes: dict[str, ClassInfo]


class ObjectProperties(BaseModel):
    class_code: str
    feature_ID: int

    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = lambda name: "pidOOODBAttr_" + camelize(name)


ObjectResponse = FeatureCollection[Point | Polygon | LineString | MultiLineString, ObjectProperties]


class SaveObject(AbstractCamelCaseModel):
    # TODO
    pass
