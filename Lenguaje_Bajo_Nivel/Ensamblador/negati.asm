.MODEL SMALL
.STACK 100H
.DATA
    msg DB 'Ingresa un numero (-9 a 9): $'
    positivo DB 13,10,'El numero es positivo$'
    negativo DB 13,10,'El numero es negativo$'
    cero DB 13,10,'El numero es cero$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, msg
    MOV AH, 09H
    INT 21H

    MOV AH, 01H
    INT 21H

    CMP AL, '-'
    JE L_NEGATIVO

    CMP AL, '0'
    JE L_CERO
    JA L_POSITIVO

L_NEGATIVO:
    MOV AH, 01H
    INT 21H
    LEA DX, negativo
    JMP MOSTRAR

L_CERO:
    LEA DX, cero
    JMP MOSTRAR

L_POSITIVO:
    LEA DX, positivo

MOSTRAR:
    MOV AH, 09H
    INT 21H

    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN