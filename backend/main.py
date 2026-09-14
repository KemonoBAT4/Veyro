# NOTE: see this chat for basic infrastructure

# DEPS:
# install fastapi
# install sqlalchemy
# install sqlmodel

class User(..., table=True):
    username: str
    
    name: str
    surname: str

    email: str
    phone: str

    profile_picture_path: str # the path to the cdn for the pfp file

    setting_uname: str = ... # reference to the settings model for app settings (app theme, ecc)
    setting: Setting = ...

    status: UserStatusEnum = ... # the status enumerative (active, deactivated, banned, ecc...)
# #endclass User

class Setting(..., table=True):
    ...
# #endclass Setting

"""
# TODO:
- [ ] implement fastapi
    - [ ] all the get / post routes
    - [ ] all the socket connections for the chat
- [ ] implement docker w/ the db
    - [ ] use postgreSQL for the db

## MODELS TO CREATE:
- [ ] User
    - one user can have more than one permissions & roles
    - one user can have more than one groups & chats
- [ ] Permission

- [ ] Roles

- [ ] Groups
    - [ ] Group members

- [ ] Chat

- [ ] Setting
"""
