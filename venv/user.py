from role import Role
from typing import List
from config import ROLE_TYPES,USERS

class User:
    def __init__(self,user_name,roles:List[Role]=[]):
        self.user_name=user_name
        self.roles=roles
        USERS.append(self)
    def assign_role_to_user(self,role):
            self.roles+=role
    def delete_role_of_user(self,role):
        self.roles.remove(role)
        
        