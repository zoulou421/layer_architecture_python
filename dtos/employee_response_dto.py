from dataclasses import dataclass, field


@dataclass
class EmployeeResponseDTO:
    """Données renvoyées à l'utilisateur ou à l'API (sortie)"""
    id:         int
    first_name: str
    last_name:  str
    email:      str  = None
    full_name:  str  = field(default=None, init=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return (
            f"EmployeeResponseDTO("
            f"id={self.id}, "
            f"full_name={self.full_name}, "
            f"email={self.email})"
        )
