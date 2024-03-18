import random
# Definição da classe Server
class Server:
    def __init__(self):
        self.working = True # Define o estado inicial do servidor como funcionando
    def produce_output(self):
        if self.working:
            if random.random() < 0.1: # Probabilidade de 20% de produzir uma saída incorreta
                #A função random.random() retorna um número de ponto flutuante aleatório no intervalo [0.0, 1.0).
                #Isso significa que o número gerado estará dentro do intervalo de 0 (inclusive) a 1 (exclusivo),
                #ou seja, pode ser qualquer número entre 0 e (mas não incluindo) 1.
                print("Producing incorrect output.") # Simula a produção de uma saída incorreta
            else:
                print("Producing correct output.") # Simula a produção de uma saída correta
        else:
            print("Server failed to produce output.") # Simula a falha do servidor em produzir uma saída

# Função principal
if __name__ == "__main__":
    server = Server() # Cria uma instância do servidor
    print("Simulating normal operation:")
    # Simula a produção de saídas pelo servidor quando está funcionando normalmente
    for i in range(5):
        server.produce_output()
        print("\nSimulating Byzantine failure:")
        # Simula a falha arbitrária do servidor
        server.working = False # Define o servidor como falho
        server.produce_output()