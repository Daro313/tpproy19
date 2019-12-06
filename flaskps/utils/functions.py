from flaskps.app.users.constants import ROLES

def get_user_roles(user):
    roles = ROLES.copy()
    for r in user.roles:
        if r.name in roles.keys():
            roles.update({r.name:True})
    return roles
