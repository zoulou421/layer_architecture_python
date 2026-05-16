## Architecture en Couches Complète

projet/
│
├── app.py                          → Point d'entrée
│
├── config/
│   └── database_config.py          → Configuration DB
│
├── database/
│   └── connection.py               → Connexion à la base
│
├── models/
│   └── employee.py                 → Entité métier
│
├── dtos/
│   ├── employee_request_dto.py     → DTO entrée (requête)
│   └── employee_response_dto.py    → DTO sortie (réponse)
│
├── mappers/
│   └── employee_mapper.py          → Conversion Model ↔ DTO
│
├── interfaces/
│   ├── i_employee_repository.py    → Interface Repository
│   └── i_employee_service.py       → Interface Service
│
├── repositories/
│   └── employee_repository.py      → Accès base de données
│
├── services/
│   └── employee_service.py         → Logique métier
│
└── exceptions/
    └── employee_exception.py       → Exceptions personnalisées