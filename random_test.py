import random
# Definição da lista de nós
num_nodes = 5
nodes = [True] * num_nodes # Inicialmente, todos os nós estão funcionando
# Função para simular uma falha em um nó aleatório
def simulate_failure():
    node_to_fail = random.randint(0, num_nodes - 1) # Escolhe aleatoriamente um nó
    print(f"Node {node_to_fail} failed!") # Simula a falha do nó escolhido
    #f": O prefixo f antes da string indica que estamos usando uma f-string. Isso permite que usemos expressões Python dentro da string, entre chaves {}.
    nodes[node_to_fail] = False # Marca o nó como falhado
    # Função para detectar e recuperar falhas
def detect_and_recover():
    for i in range(num_nodes):
        if not nodes[i]: # Se o nó estiver falhado
            print(f"Node {i} recovered!") # Simula a recuperação do nó
            nodes[i] = True # Marca o nó como recuperado

# Função para imprimir o estado atual dos nós
def print_system_state():
    print("System state:")
    for i, node in enumerate(nodes):
        print(f"Node {i}: {'Working' if node else 'Failed'}")
    # Simulação de falha, detecção e recuperação de falhas, e impressão do estado inicial
print("Initial system state:")
print_system_state()
simulate_failure()
simulate_failure()
simulate_failure()
detect_and_recover()
print("\nSystem state after failure detection and recovery:\n")
print_system_state()