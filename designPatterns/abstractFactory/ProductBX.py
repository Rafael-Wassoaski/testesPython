from CustomProduct import CustomProduct

class ProductBX(CustomProduct):
    def getNome(self):
        return "produto bx " + super().getNome()