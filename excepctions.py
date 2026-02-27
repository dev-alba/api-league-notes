class InvalidCredentials(Exception):
    def __init__(self, message='Credenciais inválidas. Por favor, verifique os dados e tente novamente.'):
        self.message=message

#       USERS

class UserNotFound(Exception):
    def __init__(self, message='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.'):
        self.message=message

class UserAlreadyExists(Exception):
    def __init__(self, message='Usuário já existente no sistema. Por favor, digite outro nickname/email e tente novamente.'):
        self.message=message

class UserCannotBeDeleted(Exception):
    def __init__(self, message='O usuário não pode ser removido no momento. Por favor, tente novamente mais tarde.'):
        self.message=message

#       PROFILES

class ProfileNotFound(Exception):
    def __init__(self, message='Perfil não encontrado no sistema. Por favor verifique os dados e tente novamente.'):
        self.message=message

class ProfilesNotFound(Exception):
    def __init__(self, message='Nenhum perfil encontrado no sistema. Por favor verifique os dados e tente novamente.'):
        self.message=message

class ProfileAlreadyExists(Exception):
    def __init__(self, message='O nome de usuário/tagline digitado já existe no sistema. Por favor tente novamente com outra combinação.'):
        self.message=message

class ProfileCannotBeDeleted(Exception):
    def __init__(self, message='O perfil não pode ser removido no momento. Por favor, tente novamente mais tarde.'):
        self.message=message

#       NOTES

class NoteNotFound(Exception):
    def __init__(self, message='Nenhuma nota com esse ID encontrada no sistema. Por favor verifique se o perfil informado possui essa nota e tente novamente.'):
        self.message=message

class NotesNotFound(Exception):
    def __init__(self, message='Nenhuma nota encontrada para o perfil. Por favor verifique se o perfil informado possui alguma nota e tente novamente.'):
        self.message=message
