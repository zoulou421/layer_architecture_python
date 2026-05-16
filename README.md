# 🏢 Employee Management — Architecture en Couches (Python + SQLite)

> Projet Python démontrant une architecture professionnelle en couches complète :  
> **DTOs · Mappers · Interfaces · Repository · Service · Exceptions**

---

## 📋 Table des matières

- [À propos du projet](#-à-propos-du-projet)
- [Architecture](#-architecture)
- [Structure des fichiers](#-structure-des-fichiers)
- [Flux des données](#-flux-des-données)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Principes SOLID appliqués](#-principes-solid-appliqués)
- [Technologies utilisées](#-technologies-utilisées)
- [Améliorations possibles](#-améliorations-possibles)
- [Auteur](#-auteur)

---

## 🎯 À propos du projet

Ce projet implémente un système de gestion d'employés en Python en suivant une **architecture en couches professionnelle**, telle qu'utilisée en entreprise avec des frameworks comme **Java Spring Boot** ou **C# .NET**.

### Objectifs pédagogiques

- Séparer clairement les responsabilités de chaque couche
- Utiliser des **interfaces (ABC)** pour découpler les dépendances
- Transporter les données proprement via des **DTOs**
- Convertir les données entre les couches via des **Mappers**
- Gérer les erreurs via des **exceptions personnalisées**
- Respecter les principes **SOLID**

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│                   app.py                    │  ← Point d'entrée
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│              EmployeeService                │  ← Logique métier
│         (implements IEmployeeService)       │
└─────────────────┬───────────────────────────┘
                  │  utilise
┌─────────────────▼───────────────────────────┐
│           EmployeeRepository                │  ← Accès base de données
│      (implements IEmployeeRepository)       │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│              SQLite Database                │  ← Persistance
└─────────────────────────────────────────────┘

        Couches transversales
┌──────────────────────────────────────────────┐
│  DTOs        │  Mappers    │  Exceptions      │
│  Models      │  Interfaces │  Config          │
└──────────────────────────────────────────────┘
```

---

## 📁 Structure des fichiers

```
projet/
│
├── app.py                              # Point d'entrée principal
│
├── config/
│   ├── __init__.py
│   └── database_config.py             # Variables de configuration (env)
│
├── database/
│   ├── __init__.py
│   └── connection.py                  # Connexion SQLite + création des tables
│
├── models/
│   ├── __init__.py
│   └── employee.py                    # Entité métier (dataclass)
│
├── dtos/
│   ├── __init__.py
│   ├── employee_request_dto.py        # DTO entrée + validation
│   └── employee_response_dto.py       # DTO sortie + full_name calculé
│
├── mappers/
│   ├── __init__.py
│   └── employee_mapper.py             # Conversions entre toutes les couches
│
├── interfaces/
│   ├── __init__.py
│   ├── i_employee_repository.py       # Contrat du repository (ABC)
│   └── i_employee_service.py          # Contrat du service (ABC)
│
├── repositories/
│   ├── __init__.py
│   └── employee_repository.py         # Implémentation CRUD SQLite
│
├── services/
│   ├── __init__.py
│   └── employee_service.py            # Implémentation logique métier
│
├── exceptions/
│   ├── __init__.py
│   └── employee_exception.py          # Exceptions personnalisées
│
├── .env                               # Variables d'environnement (non versionné)
├── .env.example                       # Modèle de configuration
├── .gitignore
└── README.md
```

---

## 🔄 Flux des données

### Création d'un employé (CREATE)

```
Utilisateur
    │
    ▼
EmployeeRequestDTO      ← Données brutes + validation
    │
    ▼  (Mapper)
Employee (Model)        ← Entité métier pure
    │
    ▼
EmployeeRepository      ← INSERT INTO employees ...
    │
    ▼
SQLite Database         ← Persistance
    │
    ▼  (Mapper)
Employee (Model)        ← Avec id généré
    │
    ▼  (Mapper)
EmployeeResponseDTO     ← Données formatées pour l'utilisateur
    │
    ▼
Utilisateur
```

### Rôle de chaque couche

| Couche | Fichier | Rôle |
|---|---|---|
| **Config** | `database_config.py` | Lit les variables d'environnement |
| **Database** | `connection.py` | Gère la connexion SQLite |
| **Model** | `employee.py` | Représente l'entité métier pure |
| **DTO Request** | `employee_request_dto.py` | Reçoit et valide les données entrantes |
| **DTO Response** | `employee_response_dto.py` | Formate les données sortantes |
| **Mapper** | `employee_mapper.py` | Convertit entre Model ↔ DTO ↔ Row |
| **Interface Repository** | `i_employee_repository.py` | Définit le contrat CRUD |
| **Interface Service** | `i_employee_service.py` | Définit le contrat métier |
| **Repository** | `employee_repository.py` | Exécute les requêtes SQL |
| **Service** | `employee_service.py` | Orchestre la logique métier |
| **Exception** | `employee_exception.py` | Gère les erreurs métier |

---

## ✅ Prérequis

- Python **3.10+**
- pip

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-username/employee-management.git
cd employee-management
```

### 2. Créer un environnement virtuel

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install python-dotenv
```

### 4. Configurer les variables d'environnement

```bash
# Copier le fichier exemple
cp .env.example .env
```

Contenu du fichier `.env` :

```env
DB_PATH=maBase.db
DB_TIMEOUT=30
```

### 5. Lancer le projet

```bash
python app.py
```

---

## 🖥️ Utilisation

### Résultat attendu

```
==================================================
  CREATE
==================================================
✅ Créé : EmployeeResponseDTO(id=1, full_name=Bonevy BEBY, email=bonevy@email.com)
✅ Créé : EmployeeResponseDTO(id=2, full_name=Alice SMITH, email=alice@email.com)
✅ Créé : EmployeeResponseDTO(id=3, full_name=Bob JONES, email=bob@email.com)

==================================================
  READ ONE
==================================================
🔍 Trouvé : EmployeeResponseDTO(id=1, full_name=Bonevy BEBY, email=bonevy@email.com)

==================================================
  READ ALL
==================================================
📋 EmployeeResponseDTO(id=1, full_name=Bonevy BEBY, email=bonevy@email.com)
📋 EmployeeResponseDTO(id=2, full_name=Alice SMITH, email=alice@email.com)
📋 EmployeeResponseDTO(id=3, full_name=Bob JONES, email=bob@email.com)

==================================================
  UPDATE
==================================================
✏️  Mis à jour : EmployeeResponseDTO(id=1, full_name=Bonevy UPDATED, email=new@email.com)

==================================================
  DELETE
==================================================
🗑️  Employé id=2 supprimé

==================================================
  GESTION DES EXCEPTIONS
==================================================
❌ Employé avec l'id '999' introuvable
❌ Erreur de validation : Le prénom est obligatoire

==================================================
  ETAT FINAL
==================================================
📋 EmployeeResponseDTO(id=1, full_name=Bonevy UPDATED, email=new@email.com)
📋 EmployeeResponseDTO(id=3, full_name=Bob JONES, email=bob@email.com)
```

### Exemple de code

```python
from database     import Database
from repositories import EmployeeRepository
from services     import EmployeeService
from dtos         import EmployeeRequestDTO

# Injection de dépendances
db      = Database()
repo    = EmployeeRepository(db)
service = EmployeeService(repo)

# Créer un employé
dto = EmployeeRequestDTO(first_name="Bonevy", last_name="BEBY", email="bonevy@email.com")
response = service.create(dto)
print(response)  # EmployeeResponseDTO(id=1, full_name=Bonevy BEBY, ...)

# Lire tous les employés
tous = service.get_all()

# Mettre à jour
dto_update = EmployeeRequestDTO(first_name="Bonevy", last_name="NEW", email="new@email.com")
service.update(1, dto_update)

# Supprimer
service.delete(1)
```

---

## 🧱 Principes SOLID appliqués

| Principe | Description | Application dans ce projet |
|---|---|---|
| **S** — Single Responsibility | Une classe = une responsabilité | Chaque couche a un rôle unique |
| **O** — Open/Closed | Ouvert à l'extension, fermé à la modification | Nouvelles implémentations sans modifier l'existant |
| **L** — Liskov Substitution | Les sous-classes remplacent les classes parentes | `EmployeeRepository` remplace `IEmployeeRepository` |
| **I** — Interface Segregation | Interfaces spécifiques plutôt que générales | `IEmployeeRepository` et `IEmployeeService` séparés |
| **D** — Dependency Inversion | Dépendre des abstractions, pas des implémentations | `EmployeeService` dépend de `IEmployeeRepository` |

---

## 🔧 Changer de base de données

Grâce aux interfaces, passer de SQLite à PostgreSQL ne nécessite qu'une seule modification :

```python
# Créer une nouvelle implémentation
class PostgresEmployeeRepository(IEmployeeRepository):
    def save(self, employee): ...
    def find_by_id(self, id): ...
    # ...

# Dans app.py — UNE SEULE ligne change
repo    = PostgresEmployeeRepository(db)  # ← ici
service = EmployeeService(repo)           # ← rien ne change
```

---

## 🛠️ Technologies utilisées

| Technologie | Version | Usage |
|---|---|---|
| **Python** | 3.10+ | Langage principal |
| **SQLite** | Intégré | Base de données |
| **python-dotenv** | latest | Variables d'environnement |
| **abc (ABC)** | Intégré | Interfaces / Classes abstraites |
| **dataclasses** | Intégré | Models et DTOs |

---

## 🚀 Améliorations possibles

- [ ] Remplacer SQLite par **PostgreSQL** avec `psycopg2`
- [ ] Ajouter **SQLAlchemy** comme ORM
- [ ] Exposer une **API REST** avec **FastAPI**
- [ ] Ajouter des **tests unitaires** avec `pytest`
- [ ] Ajouter un système de **logging**
- [ ] Implémenter la **pagination** dans `find_all()`
- [ ] Ajouter **Docker** pour la conteneurisation
- [ ] Mettre en place une **CI/CD** avec GitHub Actions

---

## 👤 Auteur

**Votre Nom**  
📧 votre.email@example.com  
🔗 [GitHub](https://github.com/votre-username)  
🔗 [LinkedIn](https://linkedin.com/in/votre-profil)

---

## 📄 Licence

Ce projet est sous licence **MIT** — voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

> 💡 **Note** : Ce projet a été réalisé dans le cadre de travaux pratiques à **SWISS UMEF University**.  
> Il illustre les bonnes pratiques de développement logiciel professionnel en Python.
