#9-11
from user import Privileges
from user import Admin

god = Admin('Jesus', 'Christ', Privileges(['read', 'write', 'ove']))
god.privileges.show_privileges()
god.desc()
god.greetings()
god.inc_cnt()
god.inc_cnt()
god.inc_cnt()
god.desc()
