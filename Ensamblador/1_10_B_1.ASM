; Lineas obligatorias para compilacion en dosbox (msdos)
.model small
.data
    msg db 'BOOM $'
.code
org 100h

start:
    ; Inicializacion de segmento de datos
    mov ax, @DATA
    mov ds, ax

    mov cx, 5 ; Iniciando contador

timer:
    mov dx, cx
    add dl, 30h

    mov ah, 02h
    int 21h
  
    mov dl, 13   
    mov ah, 02h 
    int 21h
    mov dl, 10    
    int 21h

    sub cx, 1
    cmp cx, 0
    je boom
    jmp timer

boom:
    mov dx, offset msg
    mov ah, 09h
    int 21h

    mov ax, 4C00h
    int 21h

END start
