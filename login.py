class Login:
    idLogin          = int
    correo      = str
    contraseña  = str
    
    def __init__(self, idLogin, correo, contraseña):
        self.idLogin        = idLogin
        self.correo         = correo
        self.contraseña     = contraseña