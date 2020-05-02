import random


def string_senha():
    lenght = 2

    part_1 = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", lenght))
    part_2 = "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", lenght))
    part_3 = "".join(random.sample("1234567890", lenght))
    part_4 = "".join(random.sample("!@#$%&^*()_+?", lenght))

    senha_bruto = part_1 + part_2 + part_3 + part_4

    return senha_bruto


tamanhoSenha = 8

senha = "".join(random.sample(string_senha(), tamanhoSenha))

print(senha)
