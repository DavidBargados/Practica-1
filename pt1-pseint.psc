Algoritmo CalcularAños
    Definir Año1, Año2, AñoTraspaso Como Entero
    Escribir "Introduce el primer año: "
    Leer Año1
    Escribir "Introduce el segundo año: "
    Leer Año2

    Mientras Año1 <= 0 o Año2 <= 0 Hacer
        Escribir "Los años tienen que ser mayor a cero"
        Escribir "Introduce el primer año de nuevo: "
        Leer Año1
        Escribir "Introduce el segundo año de nuevo: "
        Leer Año2
    FinMientras

    Escribir "Años de traspaso entre ", Año1, " y ", Año2, ":"
    Para i = Año1 Hasta Año2 Hacer
        Si (i MOD 4 = 0 Y (i MOD 100 <> 0 O i MOD 400 = 0)) Entonces
            Escribir i
        FinSi
    FinPara
FinAlgoritmo
