class SantaGestor:
    def process_product(self, product):
        result = "El producto no está en la lista"
        if product["Type"] == "Producto físico":
            result = "Se ha generado un albarán"
        elif product["Type"] == "Libro":
            result = "Se han generado dos albaranes"
        elif product["Type"] == "Netflix":
            result = "Se ha activado la subscripción"

        return result
