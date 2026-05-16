from models.employee            import Employee
from dtos.employee_request_dto  import EmployeeRequestDTO
from dtos.employee_response_dto import EmployeeResponseDTO


class EmployeeMapper:

    @staticmethod
    def from_request_dto(dto: EmployeeRequestDTO) -> Employee:
        """DTO Requête → Modèle métier"""
        return Employee(
            first_name=dto.first_name,
            last_name=dto.last_name,
            email=dto.email
        )

    @staticmethod
    def to_response_dto(employee: Employee) -> EmployeeResponseDTO:
        """Modèle métier → DTO Réponse"""
        return EmployeeResponseDTO(
            id=employee.id,
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email
        )

    @staticmethod
    def from_row(row: tuple) -> Employee:
        """Ligne base de données → Modèle métier"""
        return Employee(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            email=row[3] if len(row) > 3 else None
        )

    @staticmethod
    def from_rows(rows: list) -> list[Employee]:
        """Plusieurs lignes base de données → Liste de Modèles"""
        return [EmployeeMapper.from_row(row) for row in rows]

    @staticmethod
    def to_response_dtos(employees: list[Employee]) -> list[EmployeeResponseDTO]:
        """Liste de Modèles → Liste de DTOs Réponse"""
        return [EmployeeMapper.to_response_dto(e) for e in employees]
