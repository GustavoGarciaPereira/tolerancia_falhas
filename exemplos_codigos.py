import logging

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



#Falha por Colapso (Crash) com Logging


import random
import logging

def simulate_node_crash():
    node_is_operational = True
    while node_is_operational:
        if random.choice([True, False]):
            logging.info("Nó operando normalmente.")
        else:
            logging.error("Nó falhou por colapso!")
            node_is_operational = False

simulate_node_crash()



#Falha por Omissão com Logging

import random
import logging

class Server:
    def __init__(self):
        self.can_receive = True
        self.can_send = True

    def receive_message(self):
        if self.can_receive:
            logging.info("Mensagem recebida.")
        else:
            logging.warning("Falha ao receber mensagem.")

    def send_message(self):
        if self.can_send:
            logging.info("Mensagem enviada.")
        else:
            logging.warning("Falha ao enviar mensagem.")

    def simulate_failure(self):
        self.can_receive = random.choice([True, False])
        self.can_send = random.choice([True, False])

server = Server()
server.simulate_failure()
server.receive_message()
server.send_message()


#Falha por Temporização (Timing) com Logging

import time
import random
import logging

def process_request():
    delay = random.uniform(0, 2)  # Tempo de resposta varia de 0 a 2 segundos
    time.sleep(delay)
    if delay > 1:
        logging.warning(f"Falha por temporização: resposta demorada ({delay:.2f}s).")
    else:
        logging.info(f"Resposta dentro do tempo esperado ({delay:.2f}s).")

process_request()


#Falha Arbitrária (Bizantina) com Logging

import random
import logging

def server_response():
    if random.choice([True, False, False]):  # Maior chance de funcionar corretamente
        logging.info("Resposta correta do servidor.")
    else:
        logging.error("Resposta incorreta (falha arbitrária).")

server_response()