#python 3.12
def chat():
    print('Escribe también "exit" para salir')
    while True:
        print("")
        usuario = input("[•] USUARIO: ¿Qué Quieres decir al chat?: ")
        print("")
        if usuario.lower() == "hola":
            print("[•] IA: Hola ¿Cómo estás usuario?")
        elif usuario.lower() == "bien":
            print("[•] IA: ¡Que bueno! ¿Me podrías decir tu nombre por favor?")
        elif usuario.lower() == "bien y tú":
            print("[•] IA: ¡Que bueno! ¿Me podrías decir tu nombre por favor?")
        elif usuario.lower() == "bien y tu":
            print("[•] IA: ¡Que bueno! ¿Me podrías decir tu nombre por favor?")
        elif usuario.lower() == "me llamo juán":
            print("[•] IA: ¡Qué bonito nombre Juán!")
        elif usuario.lower() == "me llamo nereida":
            print("[•] IA: ¡Qué bonito nombre Nereida!")
        elif usuario.lower() == "me llamo sofía":
            print("[•] IA: ¡Qué bonito nombre Sofía!")
        elif usuario.lower() == "me llamo sofia":
            print("[•] IA: ¡Qué bonito nombre sofia!")
        elif usuario.lower() == "exit":
            print("[•] OPERACIÓN: Saliendo De La Operación")
            break
if __name__ == '__main__':
    chat()
