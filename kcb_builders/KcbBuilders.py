from kcb_dto.Kcb import *
from kcb_settings.models import KcbCategory, KcbDepartments,KcbRegionalZonal


class KcbBuilders:
    def get_category_data(id):
        if id is not None:
            category = KcbCategory.objects.filter(uuid=id).first()
            if category:
                return KcbCategoryObject(
                    id = category.id,
                    uuid = category.uuid,
                    category_name = category.category_name,
                    is_active = category.is_active,
                )
            else:
                return KcbCategoryObject()
        else:
            KcbCategoryObject()

    def get_regional_zone_data(id):
        if id is not None:
            regional_zone = KcbRegionalZonal.objects.filter(uuid=id).first()
            if regional_zone:
                return KcbRegionalZonalObject(
                    id = regional_zone.id,
                    uuid = regional_zone.uuid,
                    zone_name = regional_zone.zone_name,
                    zone_code = regional_zone.zone_code,
                    zone_description = regional_zone.zone_description,
                    is_active = regional_zone.is_active,
                )
            else:
                return KcbRegionalZonalObject()
        else:
            KcbRegionalZonalObject()

    def get_departments_data(id):
        if id is not None:
            department = KcbDepartments.objects.filter(uuid=id).first()
            if department:
                return KcbDepartmentObject(
                    id = department.id,
                    uuid = department.uuid,
                    department_name = department.department_name,
                    department_code = department.department_code,
                    department_description = department.department_description,
                    is_active = department.is_active,

                )
            else:
                return KcbDepartmentObject()
        else:
            KcbDepartmentObject()        

   