import re

def atualizar_pagamento(_):
    return "Entrando na atualização de pagamento!"

def status_pedido(_):
    return "Entrando no acompanhamento de pedido!"

intent_dict = {
    r"(?i)(?:status|rastrear|pedido|entrega)": "status_pedido",
    r"(?i)(?:atualizar|mudar|cartão|pagamento)": "atualizar_pagamento",
}

action_dict = {
    "status_pedido": status_pedido,
    "atualizar_pagamento": atualizar_pagamento,
}

while True:
    command = input("Digite o que precisa:")
    if command == "sair":
        break
    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
            print(f"{action_dict[value](groups[0])}")
    print()