"""
1. Create a greeting for your program.
2. Ask the user for the city that they grew up in.
3. Ask the user for the name of a pet.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line:
"""

msg_greeting = " 🤘 🤘 🤘 Bem vindo ao gerador de nomes de bandas! 🤘 🤘 🤘 "
msg_ask_city = "Qual cidade você cresceu?🏢🏨🚜\n"
msg_ask_pet = "Qual o nome do seu animal de estimação?🐶🐈‍⬛🦄🐹\n"


def band_name_generator():
    print(msg_greeting)
    city = input(msg_ask_city)
    pet = input(msg_ask_pet)
    print(f"Seu nome de banda é:\n 🎸🎤🥁 {pet} de {city} 🎸🎤🥁")


if __name__ == "__main__":
    band_name_generator()