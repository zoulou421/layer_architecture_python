from database    import Database
from repositories import EmployeeRepository
from services     import EmployeeService
from dtos         import EmployeeRequestDTO
from exceptions   import EmployeeNotFoundException, EmployeeValidationException

# ------------------------------------------------------------------ #
#  INJECTION DE DEPENDANCES                                            #
# ------------------------------------------------------------------ #
db      = Database()
repo    = EmployeeRepository(db)
service = EmployeeService(repo)

# ------------------------------------------------------------------ #
#  CREATE                                                              #
# ------------------------------------------------------------------ #
print("=" * 50)
print("  CREATE")
print("=" * 50)

dto1 = EmployeeRequestDTO(first_name="Bonevy", last_name="BEBY",  email="bonevy@email.com")
dto2 = EmployeeRequestDTO(first_name="Alice",  last_name="SMITH", email="alice@email.com")
dto3 = EmployeeRequestDTO(first_name="Bob",    last_name="JONES", email="bob@email.com")

r1 = service.create(dto1)
r2 = service.create(dto2)
r3 = service.create(dto3)

print(f"✅ Créé : {r1}")
print(f"✅ Créé : {r2}")
print(f"✅ Créé : {r3}")

# ------------------------------------------------------------------ #
#  READ ONE                                                            #
# ------------------------------------------------------------------ #
print("\n" + "=" * 50)
print("  READ ONE")
print("=" * 50)

employee = service.get_by_id(1)
print(f"🔍 Trouvé : {employee}")

# ------------------------------------------------------------------ #
#  READ ALL                                                            #
# ------------------------------------------------------------------ #
print("\n" + "=" * 50)
print("  READ ALL")
print("=" * 50)

tous = service.get_all()
for emp in tous:
    print(f"📋 {emp}")

# ------------------------------------------------------------------ #
#  UPDATE                                                              #
# ------------------------------------------------------------------ #
print("\n" + "=" * 50)
print("  UPDATE")
print("=" * 50)

dto_update = EmployeeRequestDTO(first_name="Bonevy", last_name="UPDATED", email="new@email.com")
updated = service.update(1, dto_update)
print(f"✏️  Mis à jour : {updated}")

# ------------------------------------------------------------------ #
#  DELETE                                                              #
# ------------------------------------------------------------------ #
print("\n" + "=" * 50)
print("  DELETE")
print("=" * 50)

service.delete(2)
print(f"🗑️  Employé id=2 supprimé")

# ------------------------------------------------------------------ #
#  GESTION DES EXCEPTIONS                                             #
# ------------------------------------------------------------------ #
print("\n" + "=" * 50)
print("  GESTION DES EXCEPTIONS")
print("=" * 50)

# Employé introuvable
try:
    service.get_by_id(999)
except EmployeeNotFoundException as e:
    print(e)

# Validation échouée
try:
    dto_invalide = EmployeeRequestDTO(first_name="", last_name="TEST", email="pas-un-email")
    service.create(dto_invalide)
except EmployeeValidationException as e:
    print(e)

# ------------------------------------------------------------------ #
#  ETAT FINAL                                                          #
# ------------------------------------------------------------------ #
print("\n" + "=" * 50)
print("  ETAT FINAL")
print("=" * 50)

tous = service.get_all()
for emp in tous:
    print(f"📋 {emp}")
