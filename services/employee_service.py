from interfaces.i_employee_service    import IEmployeeService
from interfaces.i_employee_repository import IEmployeeRepository
from mappers.employee_mapper          import EmployeeMapper
from dtos.employee_request_dto        import EmployeeRequestDTO
from dtos.employee_response_dto       import EmployeeResponseDTO
from exceptions.employee_exception    import EmployeeValidationException


class EmployeeService(IEmployeeService):

    def __init__(self, repo: IEmployeeRepository):
        self.repo = repo

    # ------------------------------------------------------------------ #
    #  CREATE                                                              #
    # ------------------------------------------------------------------ #
    def create(self, dto: EmployeeRequestDTO) -> EmployeeResponseDTO:
        try:
            dto.validate()                              # 1. Validation
            employee = EmployeeMapper.from_request_dto(dto)  # 2. DTO → Modèle
            saved    = self.repo.save(employee)         # 3. Sauvegarde
            return EmployeeMapper.to_response_dto(saved)     # 4. Modèle → DTO Réponse
        except ValueError as e:
            raise EmployeeValidationException(str(e))

    # ------------------------------------------------------------------ #
    #  READ                                                                #
    # ------------------------------------------------------------------ #
    def get_by_id(self, id: int) -> EmployeeResponseDTO:
        employee = self.repo.find_by_id(id)             # Lève EmployeeNotFoundException si absent
        return EmployeeMapper.to_response_dto(employee)

    def get_all(self) -> list[EmployeeResponseDTO]:
        employees = self.repo.find_all()
        return EmployeeMapper.to_response_dtos(employees)

    # ------------------------------------------------------------------ #
    #  UPDATE                                                              #
    # ------------------------------------------------------------------ #
    def update(self, id: int, dto: EmployeeRequestDTO) -> EmployeeResponseDTO:
        try:
            dto.validate()
            employee = self.repo.find_by_id(id)         # Vérification existence
            employee.first_name = dto.first_name
            employee.last_name  = dto.last_name
            employee.email      = dto.email
            updated = self.repo.update(employee)
            return EmployeeMapper.to_response_dto(updated)
        except ValueError as e:
            raise EmployeeValidationException(str(e))

    # ------------------------------------------------------------------ #
    #  DELETE                                                              #
    # ------------------------------------------------------------------ #
    def delete(self, id: int) -> None:
        self.repo.find_by_id(id)                        # Vérification existence
        self.repo.delete(id)
