from typing import List, Dict
from typing_extensions import TypedDict
from config import ROLE_TYPES,ACTION_TYPES,ROLES



class AccessToResource(TypedDict):
    resource:str
    access_types:List[str]


class Role:
    def __init__(self,role_type:str,access_to_resources:AccessToResource={}):
        self.role_type=role_type
        self.access_to_resources=access_to_resources
        ROLES.append(self)

    def get_access_to_resources(self):
        return self.access_to_resources

    def get_resources(self):
        return self.access_to_resources.keys()

    def add_resource(self,resource:str,access_types:List[str]=[]):
        self.access_to_resources[resource]=access_types
        
    def remove_resource(self,resource:str):
        self.access_to_resources.pop(resource)
        
    def modify_access_to_resource(self,resource:str,access_types:List[str]=[]):
        if len(access_types)>0:
            self.access_to_resources[resource]=access_types
        else:
            self.remove_resource(resource)

    def is_valid_resource_of_role(self,resource):
        try:
            self.access_to_resources[resource]
            return True
        except:
            return False
    
        
        
        

