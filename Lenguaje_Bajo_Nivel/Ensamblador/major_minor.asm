.model small
.data
    msg db 'Ingresa el primer numero: $'
    msg2 db 'Ingresa el segundo numero: $'
    primer db 'El numero mayor es el primer numero $'
    segundo db 'El numero mayor es el segundo numero $'
    igualesmsg db 'Los numeros son iguales $'

.code
org 100h
start:
    mov ax, @DATA
    mov ds, ax

    mov dx, offset msg
    mov ah, 09h
    int 21h

    mov ah, 01h
    int 21h
    mov bl, al

    mov dl, 13   
    mov ah, 02h 
    int 21h
    mov dl, 10    
    int 21h

    mov dx, offset msg2
    mov ah, 09h
    int 21h

    mov ah, 01h
    int 21h
    mov bh, al

    mov dl, 13   
    mov ah, 02h 
    int 21h
    mov dl, 10    
    int 21h

    cmp bl, bh
    jg mayor_num
    jl menor_num
    je iguales

mayor_num:
    mov dx, offset primer
    mov ah, 09h
    int 21h
    jmp salir

menor_num:
    mov dx, offset segundo
    mov ah, 09h
    int 21h
    jmp salir

iguales:
    mov dx, offset igualesmsg
    mov ah, 09h
    int 21h
    jmp salir

salir:
    mov ax, 4C00h
    int 21h

END start