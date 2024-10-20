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


  
class UserProfile(enum.Enum):
    ADMIN_PROFILE = 'ADMIN_PROFILE',
    NORMAL_PROFILE = 'NORMAL_PROFILE'

UserProfileEnum = graphene.Enum.from_enum(UserProfile)



class GenderTypeInum(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NONE = "NONE"

GenderEnum = graphene.Enum.from_enum(GenderTypeInum)

class ProfileLevelInum(enum.Enum):
    REGION = "REGION"
    DISTRICT = "DISTRICT"


ProfileLevelEnum = graphene.Enum.from_enum(ProfileLevelInum)

class UserTypeInum(enum.Enum):
    ADMIN_PROFILE = 'ADMIN_PROFILE'
    NORMAL_PROFILE = 'NORMAL_PROFILE'
    


UserEnum = graphene.Enum.from_enum(UserTypeInum)