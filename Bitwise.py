def main():
    u16Variable = 0  # 16 bits
    u8Variable = 0   # 8 bits
    u32Variable = 0  # 32 bits
    
    bits = int(input("Introduce el número de bits de tu variable: "))
    
    if bits in [8, 16, 32]:
        while True:
            print("\nSelecciona la operación a realizar:\n1) AND\n2) OR\n3) XOR")
            operacion = int(input())
            
            if operacion in [1, 2, 3]:
                corrimiento = int(input("Ingresa el corrimiento a realizar: "))
                
                if corrimiento >= 0:
                    if operacion == 1:
                        if bits == 8:
                            u8Variable &= ~(1 << corrimiento)
                            print(f"El resultado es {u8Variable}")
                        elif bits == 16:
                            if corrimiento < 16:
                                u16Variable &= ~(1 << corrimiento)
                                print(f"El resultado es {u16Variable}")
                            else:
                                print("\nOpción no válida")
                        else:
                            if corrimiento < 32:
                                u32Variable &= ~(1 << corrimiento)
                                print(f"El resultado es {u32Variable}")
                            else:
                                print("\nOpción no válida")
                    elif operacion == 2:
                        if bits == 8:
                            u8Variable |= (1 << corrimiento)
                            print(f"El resultado es {u8Variable}")
                        elif bits == 16:
                            if corrimiento < 16:
                                u16Variable |= (1 << corrimiento)
                                print(f"El resultado es {u16Variable}")
                            else:
                                print("\nOpción no válida")
                        else:
                            if corrimiento < 32:
                                u32Variable |= (1 << corrimiento)
                                print(f"El resultado es {u32Variable}")
                            else:
                                print("\nOpción no válida")
                    elif operacion == 3:
                        if bits == 8:
                            u8Variable ^= (1 << corrimiento)
                            print(f"El resultado es {u8Variable}")
                        elif bits == 16:
                            if corrimiento < 16:
                                u16Variable ^= (1 << corrimiento)
                                print(f"El resultado es {u16Variable}")
                            else:
                                print("\nOpción no válida")
                        else:
                            if corrimiento < 32:
                                u32Variable ^= (1 << corrimiento)
                                print(f"El resultado es {u32Variable}")
                            else:
                                print("\nOpción no válida")
                else:
                    print("Error: Ingresa un corrimiento válido (>= 0)")
            else:
                print("Error: Selecciona 1, 2 o 3")
    else:
        print("Error: Utiliza 8, 16 o 32 bits")

if __name__ == "__main__":
    main()
