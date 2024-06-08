import json

class Contacto:
    def __init__(self, name: str, number: str, direction: str, relation: str) -> None:
        self.name = name
        self.number = number
        self.direction = direction
        self.relation = relation
    
    def __json__(self):
        return {
            'name': self.name,
            'number': self.number,
            'direction': self.direction,
            'relation': self.relation
        }

class Agenda:
    def __init__(self):
        self.contactos = []
        self.path = "pw2Teo/tarea3/data.txt"

    def search(self, name: str):
        for i, contacto in enumerate(self.contactos):
            if contacto.name == name:
                return i, contacto
        return None, None
    
    def add(self, contacto):
        index, _ = self.search(contacto.name)
        if index is not None:
            self.edit(index, contacto)
        else:
            self.contactos.append(contacto)
    
    def edit(self, i, contacto):
        self.contactos[i] = contacto

    def remove(self, name: str):
        index, _ = self.search(name)
        if index is not None:
            del self.contactos[index]
            print(f"Contacto {name} eliminado.")
        else:
            print(f"Contacto {name} no encontrado.")

    def __str__(self):
        str_result = ""
        for i, contacto in enumerate(self.contactos):
            str_result += f"\nNombre: {contacto.name}, Numero: {contacto.number}, Dirección: {contacto.direction}, Relación: {contacto.relation}"
        return str_result

    def guardar(self):
        contactos_json = [c.__json__() for c in self.contactos]
        json_string = json.dumps(contactos_json)
        with open(self.path, "w") as file:
            file.write(json_string)
        print("Contactos guardados correctamente.")
    
    def recuperar(self):
        try:
            with open(self.path, "r") as file:
                json_string = file.read()
            contactos_json = json.loads(json_string)
            self.contactos = [Contacto(c["name"], c["number"], c["direction"], c["relation"]) for c in contactos_json]
            print("Contactos recuperados correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. No se pudieron recuperar los contactos.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. No se pudieron recuperar los contactos.")

class Principal:
    def main():
        contacto1 = Contacto("Fulanoo", "99999999", "Calle A", "UNSA")
        contacto2 = Contacto("Ciclano", "88888888", "Calle B", "TECSUP")
        contacto3 = Contacto("Beltrano", "88889999", "Calle C", "Infancia")
        agenda = Agenda()

        agenda.add(contacto1)
        agenda.add(contacto2)
        agenda.add(contacto3)

        print("Agenda inicial:")
        print(agenda.__str__())

        agenda.guardar()

        contacto4 = Contacto("Fulano", "77777777", "Calle D", "UNSA")
        agenda.add(contacto4)
        
        print("\nAgenda después de añadir/modificar a Fulano:")
        print(agenda.__str__())

        agenda.remove("Ciclano")
        
        print("\nAgenda después de eliminar a Ciclano:")
        print(agenda.__str__())

        agenda.guardar()
        agenda.recuperar()

        print("\nAgenda después de recuperar del archivo:")
        print(agenda.__str__())

if __name__ == "__main__":
    Principal.main()
