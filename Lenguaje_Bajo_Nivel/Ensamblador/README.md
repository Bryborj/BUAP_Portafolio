### Código Fuente (ASM)

```assembly
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
```

---

### Documentación del Programa

# Determinador de Signo Numérico (8086)

Este programa para el microprocesador 8086 solicita al usuario la entrada de un dígito (con opción de signo negativo) y determina si el valor pertenece a la categoría de **positivo**, **negativo** o **cero**.

## Especificaciones Técnicas
- **Arquitectura:** x86 (16 bits).
- **Modelo de memoria:** `SMALL` (Segmentos de datos y código menores a 64KB).
- **Entorno:** Emuladores DOS (como DOSBox) o hardware original 8086/8088.

## Lógica de Control
El programa utiliza comparaciones directas sobre el valor ASCII capturado en el registro `AL`:

1. **Detección de Negativos:** Compara el carácter con el símbolo `-` (2Dh). Si es igual, asume que el número es negativo y consume el siguiente carácter (el dígito) para limpiar el buffer.
2. **Detección de Cero:** Compara el carácter con el valor ASCII `0` (30h).
3. **Detección de Positivos:** Si el valor es mayor que `0` en la tabla ASCII y no fue precedido por un signo menos, se clasifica como positivo.



## Estructura de Saltos Condicionales
El flujo se bifurca mediante las siguientes instrucciones de salto:
- `JE` (Jump if Equal): Se activa si el resultado de `CMP` indica igualdad.
- `JA` (Jump if Above): Se activa si el valor es mayor (considerando comparaciones sin signo).
- `JMP` (Unconditional Jump): Utilizado para saltar a la sección de salida y evitar la ejecución secuencial de otras etiquetas.

## Registros Utilizados
| Registro | Propósito |
| :--- | :--- |
| **AX / AH** | Gestión de interrupciones de DOS (01h para lectura, 09h para escritura). |
| **DS** | Inicialización del segmento de datos. |
| **DX** | Almacena la dirección de memoria (`LEA`) de las cadenas de texto a imprimir. |
| **AL** | Almacena temporalmente el carácter ingresado por el teclado. |


Autor:
Bryan Albino Borges.

> [!NOTE]
El codigo que se encuentra aqui ha sido probado con dosbox (Fedora 43 GNU/Linux).