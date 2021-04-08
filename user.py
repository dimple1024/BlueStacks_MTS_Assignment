from role import Role
from typing import List
from config import ROLE_TYPES,USERS

class User:
    def __init__(self,user_name,roles:List[Role]=[]):
        self.user_name=user_name
        self.roles=roles
        USERS.append(self)

    def get_roles_of_user(self):
        return self.roles

    def assign_role_to_user(self,role):
            self.roles+=role

    def delete_role_of_user(self,role):
        self.roles.remove(role)

    def is_valid_role_of_user(self,role_type):
        for role in self.roles:
            if role.role_type==role_type:
                return True
        return False

        
        