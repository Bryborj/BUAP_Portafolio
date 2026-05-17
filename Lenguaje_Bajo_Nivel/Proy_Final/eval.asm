.MODEL SMALL ; Modelo de memoria pequeño
.STACK 100H ; Tamaño de la pila
.DATA ; Bloque de memoria para variables
    msgInit DB 'Ingresa tu calificacion (0-9): $'
    msgAprobado DB 'Alumno aprobado $'
    msgNoAprobado DB 'Alumno reprobado $'
    msgContinuar DB '¿Deseas evaluar otra calificacion? (S/N): $'
.CODE ; Bloque de memoria para instrucciones
MAIN PROC ; Proceso principal
    MOV AX, @DATA ; Direccion de segmento de datos
    MOV DS, AX 
    JMP INICIO ; Salto al proceso INICIO

INICIO:
    LEA DX, msgInit ; Mensaje de entrada
    MOV AH, 09H
    INT 21H ; Llamada al sistema para la ejecucion de la impresion de caracteres y usada adelante para otras funciones de AH

    MOV AH, 01H ; Recibir caracter
    INT 21H

    MOV BL, AL ; Uso del registro BL para guardar la entrada

; Salto de linea y retorno de carro
    MOV DL, 13
    MOV AH, 02H
    INT 21H
    MOV DL, 10
    INT 21H

; Convercion ASCII a numerico 
    SUB BL, 30H

    CMP BL, 6 ; Comparacion de la entrada
    JG APROBADO ; Si es mayor
    JE APROBADO ; Si es igual
    JL NO_APROBADO ; Si es menor

APROBADO:
    LEA DX, msgAprobado
    MOV AH, 09H
    INT 21H

    JMP CONTINUAR ; Salto al proceso CONTINUAR

NO_APROBADO:
    LEA DX, msgNoAprobado
    MOV AH, 09H
    INT 21H

    JMP CONTINUAR

CONTINUAR: ; Preguntar si desea evaluar otra calificacion
    MOV DL, 13 ; Retorno de carro
    MOV AH, 02H
    INT 21H
    MOV DL, 10 ; Salto de linea
    INT 21H

    LEA DX, msgContinuar
    MOV AH, 09H
    INT 21H

    MOV AH, 01H ; Recibir caracter
    INT 21H

    MOV BL, AL

    MOV DL, 13
    MOV AH, 02H
    INT 21H
    MOV DL, 10
    INT 21H

    CMP BL, 'S' ; Comparacion de la entrada
    JE INICIO ; Si es igual
    CMP BL, 'N' ; Si es igual
    JE FIN 

FIN:
    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN