def dia_semana(numero):
    dias = {1: "lunes", 2: "martes", 3: "miércoles", 4: "jueves", 5: "viernes", 6: "sábado", 7: "domingo"}
    dia = dias.get(numero)
    print(f"El día es {dia}.")

if __name__ == "__main__":
    dia_semana(7)
