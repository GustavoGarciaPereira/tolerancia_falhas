import random
# Definição da classe Server
class Server:
    def __init__(self):
        self.working = True # Define o estado inicial do servidor como funcionando
    def receive_message(self):
        if self.working:
            print("Server received message.") # Simula a recepção da mensagem pelo servidor
        else:
            print("Server failed to receive message.") # Simula a falha do servidor em receber a mensagem
    def send_message(self):
        if self.working:
            print("Server sent message.") # Simula o envio da mensagem pelo servidor
        else:
            print("Server failed to send message.") # Simula a falha do servidor em enviar a mensagem
    def omit_receive(self):
        self.working = False # Simula a falha do servidor em receber mensagens
    def omit_send(self):
        self.working = False # Simula a falha do servidor em enviar mensagens





# Função principal
if __name__ == "__main__":
    server = Server() # Cria uma instância do servidor
    print("Simulating normal operation:")
    server.receive_message() # Simula a recepção de uma mensagem quando o servidor está funcionando normalmente
    server.send_message() # Simula o envio de uma mensagem quando o servidor está funcionando normalmente
    print("\nSimulating omission failure in receiving:")
    server.omit_receive() # Simula uma falha por omissão de recebimento
    server.receive_message() # Simula a tentativa de recepção de uma mensagem após a falha por omissão
    print("\nSimulating omission failure in sending:")
    server.omit_send() # Simula uma falha por omissão de envio
    server.send_message() # Simula a tentativa de envio de uma mensagem após a falha por omissão