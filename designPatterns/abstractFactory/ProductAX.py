from CustomProduct import CustomProduct

class ProductAX(CustomProduct):

    def getNome(self):
        return "produto ax " + super().getNome()