from abc import ABC, abstractmethod
from dtos.employee_request_dto  import EmployeeRequestDTO
from dtos.employee_response_dto import EmployeeResponseDTO


class IEmployeeService(ABC):

    @abstractmethod
    def create(self, dto: EmployeeRequestDTO) -> EmployeeResponseDTO:
        """Créer un nouvel employé"""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> EmployeeResponseDTO:
        """Obtenir un employé par son id"""
        pass

    @abstractmethod
    def get_all(self) -> list[EmployeeResponseDTO]:
        """Obtenir tous les employés"""
        pass

    @abstractmethod
    def update(self, id: int, dto: EmployeeRequestDTO) -> EmployeeResponseDTO:
        """Mettre à jour un employé"""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Supprimer un employé"""
        pass
