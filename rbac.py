from role import Role
from user import User
from config import ROLE_TYPES,ACTION_TYPES,ROLES,USERS

#Validation functions
def is_valid_action_types(action_types):
    print(action_types)
    for action_type in action_types:
        if (action_type not in ACTION_TYPES):
            return False
    return True

def is_valid_role_type(role_type):
    for role in ROLE_TYPES:
        if role_type==role:
            return True
    return False

#Initialisation with some users and resources
def app_init():
    admin_role=Role("ADMIN")
    user_role=Role("USER")

    admin_role.add_resource("BACKEND_SERVER_CONFIG",["READ","WRITE","DELETE"])
    admin_user=User("admin",[admin_role])
    user=User("User1",[user_role])

def user_login():
    users_count=1
    print("Users with respective roles in the system:")
    print("S.NO  User  Role")
    for user in USERS:
        for role in user.roles:
            print(str(users_count)+"  "+user.user_name+" "+role.role_type)
            users_count+=1

    user_found=False
    user_name,role_type=input("Enter the user name and role type to login(space separated):").split(" ")
    for user in USERS:
        if user.user_name==user_name:
            for role in user.roles:
                if role_type==role.role_type:
                    current_user=user
                    user_found=True
                    break
            if user_found==True:
                break
    if user_found==False :
        print("Invalid user name or role type provided! Try again!")
        user_login()
    else:
        if role_type == "ADMIN":
            while 1:
                admin_options(current_user,role_type)
        else:
            while 1:
                user_options(current_user,role_type)

def admin_options(current_user,role_type):
    print("Hi! You are logged in as "+current_user.user_name +" with role as "+role_type)
    print("Press 1 to login as another user")
    print("Press 2 to create user")
    print("Press 3 to edit role")
    print("Press 4 to exit")
    option=int(input())
    if option==1:
        user_login()
    elif option==2:
        create_user()
    elif option==3:
        edit_role()
    elif option==4:
        exit(0)
    else:
        print("Invalid options! Please try again!")
        admin_options()

def user_options(current_user,role_type):
    print("Hi! You are logged in as "+current_user.user_name +" with role as "+role_type)
    print("Press 1 to login as another user")
    print("Press 2 to view roles")
    print("Press 3 to access resource")
    print("Press 4 to exit")
    option=int(input())
    if option==1:
        user_login()
    elif option==2:
        view_roles(current_user)
    elif option==3:
        check_access(current_user.user_name)
    elif option==4:
        exit(1)
    else:
        print("Invalid options! Please try again!")
        admin_options()

def view_roles(current_user):
    print("Roles available for "+current_user.user_name+" :")
    for role in current_user.get_roles_of_user():
        print(role.role_type)

def create_user():
    user_name=input("Enter user name: ")
    print("Roles available: ")
    for role in ROLE_TYPES:
        print(role)

    role_types=input("Enter roles (space separated): ").split(" ")
    for role_type in role_types:
        if not is_valid_role_type(role_type):
            print("Invalid role type provided , please try again! ")
            create_user()
    roles=[]
    role_found=False
    for role_type in role_types:
        for existing_role in ROLES:
            if role_type==existing_role.role_type:
                role=existing_role
                role_found=True
                break
        if role_found==False:
            role=Role(role_type)
        roles.append(role)

    new_user=User(user_name,roles)

def edit_role():
    print("Roles available to edit : ")
    for role in ROLES:
        print(role.role_type)
    role_type=input("Enter the role type you want to edit: ")
    role_found=False
    current_role=None
    for role in ROLES:
        if role.role_type==role_type:
            current_role=role
            role_found=True
            break
    if role_found==False:
        print("Invalid role type provided , please try again! ")
        edit_role()
    else:
        print("Press 1 to add resource to role")
        print("Press 2 to remove resource from the role")
        print("Press 3 to modify resource access types for role")
        option=int(input())
        if option==1:
            resource=input("Enter the resource name to add: ")
            access_types=input("Enter the access types to be added(space separated): ").split(" ")
            current_role.add_resource(resource,access_types)
        elif option==2:
            resource = input("Enter the resource name to remove: ")
            current_role.remove_resource(resource)
        elif option==3:
            resource = input("Enter the resource name to modify: ")
            current_role.modify_access_to_resource(resource)
        else:
            print("Invalid option provided , please try again!")

def check_access(user_name):
    resource, access_type = input("Enter the resource name and access type to check access (space separated): ").split(" ")
    if not is_valid_action_types([access_type]):
        print("Invalid access type provided! Please try again! ")
        check_access(user_name)
    has_access=False
    user_found=False
    for user in USERS:
        if user.user_name==user_name:
            user_found=True
            break
    if user_found==True:
        for role in user.get_roles_of_user():
            try:
                if access_type in role.access_to_resources[resource]:
                    has_access=True
            except:
                continue
    if has_access==True:
        print(user_name+" has "+ access_type+" access to the resource "+resource)
    else:
        print(user_name+" does not has "+ access_type+" access to the resource "+resource)




app_init()

while 1:
    user_login()





