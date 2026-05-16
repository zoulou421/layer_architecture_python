from abc import ABC, abstractmethod
from models.employee import Employee


class IEmployeeRepository(ABC):

    @abstractmethod
    def save(self, employee: Employee) -> Employee:
        """Insérer un nouvel employé"""
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Employee:
        """Rechercher un employé par son id"""
        pass

    @abstractmethod
    def find_by_name(self, first_name: str) -> list[Employee]:
        """Rechercher des employés par prénom"""
        pass

    @abstractmethod
    def find_all(self) -> list[Employee]:
        """Récupérer tous les employés"""
        pass

    @abstractmethod
    def update(self, employee: Employee) -> Employee:
        """Mettre à jour un employé existant"""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Supprimer un employé par son id"""
        pass
