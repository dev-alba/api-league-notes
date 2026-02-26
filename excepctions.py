class InvalidCredentials(Exception):
    def __init__(self, message='Credenciais inválidas. Por favor, verifique os dados e tente novamente.'):
        self.message=message

class UserNotFound(Exception):
    def __init__(self, message='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.'):
        self.message=message

class UserAlreadyExists(Exception):
    def __init__(self, message='Usuário já existente no sistema. Por favor, digite outro nickname/email e tente novamente.'):
        self.message=message

class UserCannotBeDeleted(Exception):
    def __init__(self, message='O usuário não pode ser removido no momento. Por favor, tente novamente mais tarde'):
        self.message=message


class ProfileNotFound(Exception):
    pass

class ProfilesNotFound(Exception):
    pass

class ProfileAlreadyExists(Exception):
    pass

class NoteNotFound(Exception):
    pass

class NotesNotFound(Exception):
    pass

