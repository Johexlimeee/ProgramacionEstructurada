from funciones import * 

def main():
  palabra = seleccionarPalabra()
  alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
  jugada = ["_"]*len(palabra)

  for turno in range(5):
    print(f"\nTurno: {turno+1}")
    print("-"*20)
  
    imprimirActualizacion(alfabeto, jugada)
    letra = entradaUsuario()
    jugada = actualizarJugada(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
    imprimirActualizacion(alfabeto, jugada)
    
    check = input("Desea adivinar la palabra? (s/n): ")
    
    if check.lower() == "s":
      suposicion = input ("introdusca su respuesta: ").lower()
      success = verificarJugada(suposicion, palabra)
  
      if success:
        print("+"*20)
        print("Madle mia willy, que haces aqui compañero?")
        print("+"*20)
        break
      else:
        print("+"*20)
        print("la suposicion es incorrecta...")
        print("+"*20)
        
    if turno == 4:
      print("-"*20)
      print("Omaiga papulince -10 prro mal momo")
      print(":'v"*20)

if __name__=="__main__":
  main()