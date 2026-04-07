#       AUTH
class LeagueNotesException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

#       SECURITY
class InvalidCredentials(LeagueNotesException):
    def __init__(self, message='Credenciais inválidas. Por favor, verifique os dados e tente novamente.'):
        super().__init__(message, status_code=401)

class InvalidToken(LeagueNotesException):
    def __init__(self, message='Token inválido.'):
        super().__init__(message, status_code=401)

class ExpiredInvalidToken(LeagueNotesException):
    def __init__(self, message='Token inválido ou expirado.'):
        super().__init__(message, status_code=401)

class Unauthorized(LeagueNotesException):
    def __init__(self, message='Requisição não autorizada.'):
        super().__init__(message, status_code=401)

#       USERS
class UserNotFound(LeagueNotesException):
    def __init__(self, message='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.'):
        super().__init__(message, status_code=404)

class UserAlreadyExists(LeagueNotesException):
    def __init__(self, message='Usuário já existente no sistema. Por favor, digite outro nickname/email e tente novamente.'):
        super().__init__(message, status_code=409)

class UserCannotBeDeleted(LeagueNotesException):
    def __init__(self, message='O usuário não pode ser removido no momento. Por favor, tente novamente mais tarde.'):
        super().__init__(message, status_code=409)

#       PROFILES
class ProfileNotFound(LeagueNotesException):
    def __init__(self, message='Perfil não encontrado no sistema. Por favor verifique os dados e tente novamente.'):
        super().__init__(message, status_code=404)

class ProfilesNotFound(LeagueNotesException):
    def __init__(self, message='Nenhum perfil encontrado no sistema. Por favor verifique os dados e tente novamente.'):
        super().__init__(message, status_code=404)

class ProfileAlreadyExists(LeagueNotesException):
    def __init__(self, message='O nome de usuário/tagline digitado já existe no sistema. Por favor tente novamente com outra combinação.'):
        super().__init__(message, status_code=409)

class ProfileCannotBeDeleted(LeagueNotesException):
    def __init__(self, message='O perfil não pode ser removido no momento. Por favor, tente novamente mais tarde.'):
        super().__init__(message, status_code=409)

#       NOTES
class NoteNotFound(LeagueNotesException):
    def __init__(self, message='Nenhuma nota com esse ID encontrada no sistema. Por favor verifique se o perfil informado possui essa nota e tente novamente.'):
        super().__init__(message, status_code=404)

class NotesNotFound(LeagueNotesException):
    def __init__(self, message='Nenhuma nota encontrada para o perfil. Por favor verifique se o perfil informado possui alguma nota e tente novamente.'):
        super().__init__(message, status_code=404)

#       CHAMPIONS
class ChampNotFound(LeagueNotesException):
    def __init__(self, message='Campeão não localizado no sistema.'):
        super().__init__(message, status_code=404)

class ChampAlreadyExists(LeagueNotesException):
    def __init__(self, message='Campeão já existente no sistema.'):
        super().__init__(message, status_code=409)

class ChampionsNotFound(LeagueNotesException):
    def __init__(self, message='Nenhum campeão localizado no sistema.'):
        super().__init__(message, status_code=404)        

#       MATCHUPS
class MatchupNotFound(LeagueNotesException):
    def __init__(self, message='Matchup não localizada no sistema.'):
        super().__init__(message, status_code=404)

class MatchupAlreadyExists(LeagueNotesException):
    def __init__(self, message='Matchup já existente no sistema.'):
        super().__init__(message, status_code=409)