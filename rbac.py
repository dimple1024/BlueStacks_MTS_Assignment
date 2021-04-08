from role import Role
from user import User
from config import ROLE_TYPES,ACTION_TYPES,ROLES,USERS


#Initialisation with some users and resources
def app_init():
    admin_role=Role("ADMIN")
    user_role=Role("USER")

    admin_role.assign_access_to_resource("BACKEND_SERVER_CONFIG",["READ","WRITE","DELETE"])
    admin_user=User("admin",[admin_role,user_role])
    user=User("User1",[user_role])

def user_login():
    users_count=1
    print("Users in the system:")
    print("S.NO  User ")
    for user in USERS:
            print(str(users_count)+"  "+user.user_name)
            users_count+=1

    user_found=False
    user_name=input("Enter the user name to login:")
    for user in USERS:
        if user.user_name==user_name:
            current_user=user
            user_found=True
            break
    if user_found==False:
        print("Invalid user name provided! Try again! ")
        user_login()
    else:
        if current_user.user_name == "admin":
            admin_options(current_user)
        else:
            user_options(current_user)

def admin_options(current_user):
    print("Hi! You are logged in as "+current_user.user_name)
    print("Press 1 to login as another user")
    print("Press 2 to create user")
    print("Press 3 to edit role")
    option=int(input())
    if option==1:
        user_login()
    elif option==2:
        create_user()
    elif option==3:
        edit_role(current_user)
    else:
        print("Invalid options! Please try again!")
        admin_options()

def user_options(current_user):
    print("Hi! You are logged in as "+current_user.user_name)
    print("Press 1 to login as another user")
    print("Press 2 to view roles")
    print("Press 3 to access resource")
    option=int(input())
    if option==1:
        user_login()
    elif option==2:
        create_user()
    elif option==3:
        check_access(current_user.user_name)
    else:
        print("Invalid options! Please try again!")
        admin_options()

def create_user():
    user_name=input("Enter user name: ")
    print("Roles available: ")
    for role in ROLE_TYPES:
        print(role)

    role=input("Enter role type: ")
    if role not in ROLE_TYPES:
        print("Invalid role type provided , please try again! ")
        create_user()
    new_user=User(user_name,[role])

def edit_role(current_user):
    print("Roles assigned to "+ current_user.user_name+" : ")
    user_roles=[role.role_type for role in current_user.roles]
    for role in user_roles:
        print(role)
    role=input("Enter the role type you want to edit: ")
    if role not in user_roles:
        print("Invalid role type provided , please try again! ")
        edit_role(current_user)
    else:
        print("Press 1 to add resource access to role")
        print("Press 2 to remove resource access to role")
        print("Press 3 to create a new role")
        option=int(input())
        if option==1 or option==2:
            resource=input("Enter the resource name: ")
            #TODO: Call methods of instance current user









def check_access(user_name):
    resource, access_type = input("Enter the resource name and access type to check access").split(" ")
    if access_type not in ACTION_TYPES:
        print("Invalid access type provided! Please try again! ")
        check_access(user_name)
    has_access=False
    user_found=False
    for user in USERS:
        if user.user_name==user_name:
            user_found=True
            break
    if user_found==True:
        for role in user.roles:
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
user_login()





