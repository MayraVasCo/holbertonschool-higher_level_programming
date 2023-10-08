#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumentos = sys.argv[1:]
    suma = 0
    for arg in argumentos:
        suma += int(arg)
    print(suma)
