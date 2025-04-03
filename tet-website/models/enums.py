from enum import Enum

class UserType(Enum):
    ADMIN = 'admin'
    SECO_MANAGER = 'seco_manager'
    USER = 'user'

class PerformedTaskStatus(Enum):
    SOLVED = 'solved'
    UNSOLVED = 'unsolved'

class NavigationType(Enum):
    PAGE_NAVIGATION = 'page_navigation'
    TAB_SWITCH = 'tab_switch'

class AcademicLevel(Enum):
    HIGH_SCHOOL = 'high_school'
    BACHELOR = 'bachelor'
    MASTER = 'master'
    DOCTORATE = 'doctorate'

class PreviousExperience(Enum):
    NEVER = 'never'
    RARELY = 'rarely'
    OFTEN = 'often'
    AWAYS = 'always'

class SegmentType(Enum):
    ACADEMIA = 'academia'
    INDUSTRY = 'industry'
    BOTH = 'both'

