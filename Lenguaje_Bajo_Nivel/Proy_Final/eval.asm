.MODEL SMALL
.STACK 100H
.DATA
    msgInit DB 'Ingresa tu calificacion (0-9): $'
    msgAprobado DB 'Alumno aprobado $'
    msgNoAprobado DB 'Alumno reprobado $'
    msgContinuar DB '¿Deseas evaluar otra calificacion? (S/N): $'
.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    JMP INICIO

INICIO:
    LEA DX, msgInit
    MOV AH, 09H
    INT 21H

    MOV AH, 01H
    INT 21H

    MOV BL, AL

    MOV DL, 13
    MOV AH, 02H
    INT 21H
    MOV DL, 10
    INT 21H

    SUB BL, 30H

    CMP BL, 6
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
    MOV DL, 13
    MOV AH, 02H
    INT 21H
    MOV DL, 10
    INT 21H

    LEA DX, msgContinuar
    MOV AH, 09H
    INT 21H

    MOV AH, 01H
    INT 21H

    MOV BL, AL

    MOV DL, 13
    MOV AH, 02H
    INT 21H
    MOV DL, 10
    INT 21H

    CMP BL, 'S'
    JE INICIO
    CMP BL, 'N'
    JE FIN

FIN:
    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN