class EmployeeNotFoundException(Exception):
    def __init__(self, id: int):
        super().__init__(f"❌ Employé avec l'id '{id}' introuvable")
        self.id = id


class EmployeeAlreadyExistsException(Exception):
    def __init__(self, name: str):
        super().__init__(f"❌ L'employé '{name}' existe déjà")
        self.name = name


class EmployeeValidationException(Exception):
    def __init__(self, message: str):
        super().__init__(f"❌ Erreur de validation : {message}")
        self.message = message
