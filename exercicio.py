#--------------------------------------------
# classe base: ANIMAL
#--------------------------------------------

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som"
    
    def apresentar(self):
        return f"Olá, sou{self.nome}, e tenho {self.idade} anos."
    
#--------------------------------------------
# classe derivada: CACHORRO
#--------------------------------------------

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au Au!"
    
    def apresentar(self):
        return f"Olá, sou {self.nome}, um cachorro da raça {self.raca}, e tenho {self.idade} anos."
    
#--------------------------------------------
# classe derivada: GATO
#--------------------------------------------

class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"
    
    def apresentar(self):
        return f"Olá, sou {self.nome}, um gato de cor {self.cor_pelo}, e tenho {self.idade} anos."
    
#--------------------------------------------
# classe derivada: VACA 
#--------------------------------------------   

class Vaca(Animal):
    def __init__(self, nome, idade, producao_leite_litros):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros  # atributo privado

    def emitir_som(self):
        return "Muu!"
    
    def apresentar(self):
        return f"Olá, sou {self.nome}, uma vaca que produz {self.__producao_leite_litros} litros de leite por dia, e tenho {self.idade} anos."

#--------------------------------------------
# getter
# Encapsulamento (Proteção de Dados)
#--------------------------------------------

    def get_producao_leite(self):
        return self.__producao_leite_litros
    
#--------------------------------------------
# setter
# Encapsulamento (Proteção de Dados)
#--------------------------------------------

    def set_producao_leite(self, litros):
        if litros >= 0:
            self.__producao_leite_litros = litros
        else:
            print("Valor inválido! A produção de leite não pode ser negativa.")

#--------------------------------------------
# teste das classes
#-------------------------------------------- 

if __name__ == "__main__":
    cachorro = Cachorro("Rex", 3, "Labrador")
    gato = Gato("Mimi", 5, "Branco")
    vaca = Vaca("Mimosa", 7, 25.0)

    #--------------------------------------------
    # Teste dos metodos apresentar e emitir_som 
    #--------------------------------------------

    print(cachorro.apresentar())
    print(cachorro.emitir_som())

    print(gato.apresentar())
    print(gato.emitir_som())

    print(vaca.apresentar())
    print(vaca.emitir_som())

    # --------------------------------------------
    # Teste do getter da classe Vaca
    # --------------------------------------------

    print(f"Produção de leite atual: {vaca.get_producao_leite()} litros por dia")
    vaca.set_producao_leite(28.0)
    print(f"Nova produção de leite: {vaca.get_producao_leite()} litros por dia")