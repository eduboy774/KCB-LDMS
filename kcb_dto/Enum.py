import enum
import graphene

class ZoneCode(enum.Enum):
    ZONE_01 = 'ZONE_01',
    ZONE_02 = 'ZONE_02',
    ZONE_03 = 'ZONE_03',
    ZONE_04 = 'ZONE_04'

ZoneCodeEnum = graphene.Enum.from_enum(ZoneCode)



class DepartmentCode(enum.Enum):
    RB ='RB',
    CB ='CB',
    IB ='IB',
    CAB ='CAB',
    PB ='PB',
    TC ='TC',
    RM ='RM',
    CL ='CL',
    HR ='HR',
    ICT ='ICT',
    CS ='CS',
    MS ='MS',
    FA ='FA',
    OP ='OP',
    AI ='AI',
    
DepartmentCodeEnum =graphene.Enum.from_enum(DepartmentCode)


  
