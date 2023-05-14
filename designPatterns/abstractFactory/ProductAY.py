from CustomProduct import CustomProduct

class ProductAY(CustomProduct):
    def getNome(self):
        return "produto ay " + super().getNome()