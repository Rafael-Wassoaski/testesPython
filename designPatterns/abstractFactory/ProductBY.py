from CustomProduct import CustomProduct

class ProductBY(CustomProduct):
    def getNome(self):
        return "produto by " + super().getNome()