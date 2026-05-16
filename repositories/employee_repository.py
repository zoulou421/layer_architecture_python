from interfaces.i_employee_repository import IEmployeeRepository
from mappers.employee_mapper          import EmployeeMapper
from models.employee                  import Employee
from exceptions.employee_exception    import EmployeeNotFoundException


class EmployeeRepository(IEmployeeRepository):

    def __init__(self, db):
        self.db = db

    # ------------------------------------------------------------------ #
    #  CREATE                                                              #
    # ------------------------------------------------------------------ #
    def save(self, employee: Employee) -> Employee:
        with self.db.get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO employees (first_name, last_name, email)
                VALUES (:first_name, :last_name, :email)
                """,
                {
                    "first_name": employee.first_name,
                    "last_name":  employee.last_name,
                    "email":      employee.email,
                }
            )
            conn.commit()
            employee.id = cursor.lastrowid
            return employee

    # ------------------------------------------------------------------ #
    #  READ                                                                #
    # ------------------------------------------------------------------ #
    def find_by_id(self, id: int) -> Employee:
        with self.db.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM employees WHERE id = :id",
                {"id": id}
            )
            row = cursor.fetchone()
            if not row:
                raise EmployeeNotFoundException(id)
            return EmployeeMapper.from_row(row)

    def find_by_name(self, first_name: str) -> list[Employee]:
        with self.db.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM employees WHERE first_name = :first_name",
                {"first_name": first_name}
            )
            return EmployeeMapper.from_rows(cursor.fetchall())

    def find_all(self) -> list[Employee]:
        with self.db.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM employees")
            return EmployeeMapper.from_rows(cursor.fetchall())

    # ------------------------------------------------------------------ #
    #  UPDATE                                                              #
    # ------------------------------------------------------------------ #
    def update(self, employee: Employee) -> Employee:
        with self.db.get_connection() as conn:
            conn.execute(
                """
                UPDATE employees
                SET first_name = :first_name,
                    last_name  = :last_name,
                    email      = :email
                WHERE id = :id
                """,
                {
                    "first_name": employee.first_name,
                    "last_name":  employee.last_name,
                    "email":      employee.email,
                    "id":         employee.id,
                }
            )
            conn.commit()
            return employee

    # ------------------------------------------------------------------ #
    #  DELETE                                                              #
    # ------------------------------------------------------------------ #
    def delete(self, id: int) -> None:
        with self.db.get_connection() as conn:
            conn.execute(
                "DELETE FROM employees WHERE id = :id",
                {"id": id}
            )
            conn.commit()
