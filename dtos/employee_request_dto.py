from dataclasses import dataclass


@dataclass
class EmployeeRequestDTO:
    """Données reçues de l'utilisateur ou de l'API (entrée)"""
    first_name: str
    last_name:  str
    email:      str = None

    def validate(self):
        """Valide les données avant traitement"""
        if not self.first_name or not self.first_name.strip():
            raise ValueError("Le prénom est obligatoire")
        if not self.last_name or not self.last_name.strip():
            raise ValueError("Le nom est obligatoire")
        if self.email and "@" not in self.email:
            raise ValueError(f"Email invalide : {self.email}")
