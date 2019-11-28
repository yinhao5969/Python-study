#9_12
from admin import Admin
from privileges import Privileges
president = Admin('sha', 'bi', Privileges(['kill', 'cheat', 'steal', 'rob']))
president.privileges.show_privileges()
president.desc()
president.reset_cnt()
president.inc_cnt()
president.desc()
