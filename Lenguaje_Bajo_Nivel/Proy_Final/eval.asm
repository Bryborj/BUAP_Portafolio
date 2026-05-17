.MODEL SMALL
.STACK 100H
.DATA
    msgInit DB 'Ingresa tu calificacion (0-9): $'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, msgInit
    MOV AH, 09H
    INT 21H

    MOV AH, 01H
    INT 21H

    SUB AL, 30H

END MAIN