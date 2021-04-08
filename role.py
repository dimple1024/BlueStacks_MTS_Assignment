from typing import List, Dict
from typing_extensions import TypedDict
from config import ROLE_TYPES,ACTION_TYPES,ROLES

#TODO:Move this to interface, and add similar for role type , and resource
def is_valid_action_types(action_types):
    for action_type in action_types:
        if (action_type not in ACTION_TYPES):
            return False
    return True

class AccessToResource(TypedDict):
    resource:str
    access_types:List[str]


class Role:
    def __init__(self,role_type:str,access_to_resources:AccessToResource={}):
        self.role_type=role_type
        self.access_to_resources=access_to_resources
        ROLES.append(self)

    def add_resource(self,resource:str,access_types:List[str]=[]):
        self.access_to_resources[resource]=access_types
        
    def remove_resource(self,resource:str):
        self.access_to_resources.pop(resource)
        
    def assign_access_to_resource(self,resource:str,access_types:List[str]=[]):
        if is_valid_action_types(access_types):
            try:
                self.access_to_resources[resource]+=access_types
            except :
                self.access_to_resources[resource]=access_types
        else:
            print("Invalid access type specified!")
            
    def delete_access_from_resource(self,resource,access_types:List[str]):
        for access_type in access_types:
            if access_type in self.access_to_resources[resource]:
                self.access_to_resources[resource].remove(access_type)
        print("Access deleted for resource: "+resource)
    
        
        
        

