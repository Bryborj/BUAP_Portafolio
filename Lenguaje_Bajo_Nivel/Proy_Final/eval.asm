.MODEL SMALL
.STACK 100H
.DATA
    msgInit DB 'Ingresa tu calificacion (0-9): $'
    msgAprobado DB 'Alumno aprobado $
    msgNoAprobado DB 'Alumno reprobado $'
    msgContinuar DB '¿Deseas evaluar otra calificacion? (S/N): $'
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

    CMP AL, 6
    JG APROBADO
    JE APROBADO
    JL NO_APROBADO

APROBADO:
    LEA DX, msgAprobado
    MOV AH, 09H
    INT 21H

    JMP CONTINUAR

NO_APROBADO:
    LEA DX, msgNoAprobado
    MOV AH, 09H
    INT 21H

    JMP CONTINUAR

CONTINUAR:
    LEA DX, msgContinuar
    MOV AH, 09H
    INT 21H

    CMP AL, 'S'
    JE INICIO
    CMP AL, 'N'
    JE FIN


FIN:
    MOV AH, 4CH
    INT 21H
END MAIN