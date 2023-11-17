import re

def atualizar_pagamento():
    return "Entrando na atualização de pagamento"

def status_pedido():
    return "Entrando no acompanhamento de pedido"

def sair():
    return False

intent_dict = {
    r"(?i)(?:status|rastrear|pedido|entrega)": "status_pedido",
    r"(?i)(?:atualizar|mudar|cartão|pagamento)": "atualizar_pagamento",
    r"(?i)(?:sair)": "sair"
}

action_dict = {
    "status_pedido": status_pedido,
    "atualizar_pagamento": atualizar_pagamento,
    "sair": sair
}

while True:
    command = input("Digite o que precisa:")
    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(f"{action_dict[value](groups[0])}", end=" ")
    print()