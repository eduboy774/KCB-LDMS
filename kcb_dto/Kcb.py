import graphene
from graphene_federation import key, external, extend
from kcb_dto.Enum import ZoneCodeEnum,DepartmentCodeEnum
from kcb_dto.Response import ResponseObject


# Category
class KcbCategoryInputObject(graphene.InputObjectType):
    uuid = graphene.String()
    category_name = graphene.String()

@key(fields='id')
class KcbCategoryObject(graphene.ObjectType):
    id = graphene.String()
    uuid = graphene.String()
    category_name = graphene.String()

class KcbCategoryResponseObject(graphene.ObjectType):
    data = graphene.List(KcbCategoryObject)
    response = graphene.Field(ResponseObject)

class KcbCategoryFilteringInputObject(graphene.InputObjectType):
    uuid = graphene.String()
    category_name = graphene.String()


# Regional Zone
class KcbRegionalZonalInputObject(graphene.InputObjectType):
    uuid = graphene.String()
    zone_name = graphene.String(required=True)
    zone_code = ZoneCodeEnum(required=True)
    zone_description = graphene.String()
    

@key(fields='id')
class KcbRegionalZonalObject(graphene.ObjectType):
    id = graphene.String()
    uuid = graphene.String()
    zone_name = graphene.String()
    zone_code = graphene.String()
    zone_description = graphene.String()

class KcbRegionalZonalResponseObject(graphene.ObjectType):
    data = graphene.List(KcbRegionalZonalObject)
    response = graphene.Field(ResponseObject)

class KcbRegionalZonalFilteringInputObject(graphene.InputObjectType):
    uuid = graphene.String()
    zone_name = graphene.String()
    zone_code = graphene.String()



# Department
class KcbDepartmentInputObject(graphene.InputObjectType):
    uuid = graphene.String()
    department_name = graphene.String(required=True)
    department_code = graphene.String(required=True)
    department_description = graphene.String()


@key(fields='id')
class KcbDepartmentObject(graphene.ObjectType):
    id = graphene.String()
    uuid = graphene.String()
    department_name = graphene.String()
    department_code = graphene.String()
    department_description = graphene.String()


class KcbDepartmentResponseObject(graphene.ObjectType):
    data = graphene.List(KcbDepartmentObject)
    response = graphene.Field(ResponseObject)

class KcbDepartmentFilteringInputObject(graphene.InputObjectType):
    uuid = graphene.String()
    department_name = graphene.String()
    department_code = graphene.String()







