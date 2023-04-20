from abc import ABCMeta

from pydantic import BaseModel, BaseConfig, Extra
from humps import camelize
from geojson_pydantic import FeatureCollection, Polygon, Point, LineString, MultiLineString, \
    MultiPolygon


class CamelCaseConfig(BaseConfig):
    allow_population_by_field_name = True
    alias_generator = camelize


class AbstractCamelCaseModel(BaseModel, metaclass=ABCMeta):
    class Config(CamelCaseConfig):
        orm_mode = True


class ClassInfo(AbstractCamelCaseModel):
    alias: str
    attributes: list[str]
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
    feature_ID: str
    resource: list[str] | None
    commit_ID_feat: str | None
    commit_ID_geom: str | None

    class Config(BaseConfig):
        extra = Extra.allow
        allow_population_by_field_name = True
        alias_generator = lambda name: "pidOOODBAttr_" + camelize(name)


class ObjectResponse(
    FeatureCollection[Point | Polygon | LineString | MultiLineString | MultiPolygon, ObjectProperties]):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = lambda name: "pidOOODBAttr_" + camelize(
            name) if name in ObjectProperties.__fields__ else name
