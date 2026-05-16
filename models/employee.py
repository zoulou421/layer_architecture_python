from dataclasses import dataclass, field


@dataclass
class Employee:
    first_name: str
    last_name:  str
    email:      str = None
    id:         int = field(default=None)

    def __repr__(self):
        return (
            f"Employee("
            f"id={self.id}, "
            f"name={self.first_name} {self.last_name}, "
            f"email={self.email})"
        )
