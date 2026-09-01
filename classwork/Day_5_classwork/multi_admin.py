"""my_multi_module_admin.py - demonstrates User and Admin split across two modules (9-12)"""
from privileges_admin_module import Admin

new_admin = Admin("David", "Onunkakwu")
new_admin.show_privileges()
