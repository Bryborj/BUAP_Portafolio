import java.util.Scanner;
public class Convercion_Bin_Oct_Dec {
    public static void main(String[] args) {
        boolean continuar = true;
        Scanner scanner = new Scanner(System.in);
        while (continuar) {
            System.out.println("Seleccione la conversión que desea realizar:");
            System.out.println("1. Decimal a Binario y Octal");
            System.out.println("2. Binario a Decimal");
            System.out.println("3. Octal a Decimal");
            System.out.print("Ingrese el número de opción: ");
            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese un número decimal: ");
                    int decimal;
                    try {
                        decimal = scanner.nextInt();
                    } catch (Exception e) {
                        System.out.println("Entrada inválida. Por favor, ingrese un número entero.");
                        scanner.next();
                        break;
                    }
                    String binarioDesdeDecimal = Integer.toBinaryString(decimal);
                    System.out.println("El número binario es: " + binarioDesdeDecimal);
                    String octalDesdeDecimal = Integer.toOctalString(decimal);
                    System.out.println("El número octal es: " + octalDesdeDecimal);
                    break;
                case 2:
                    System.out.print("Ingrese un número binario: ");
                    try {
                        String binario = scanner.next();
                        int decimalDesdeBinario = Integer.parseInt(binario, 2);
                        System.out.println("El número decimal es: " + decimalDesdeBinario);
                    } catch (Exception e) {
                        System.out.println("Entrada inválida. Por favor, ingrese un número binario válido.");
                        scanner.nextLine();
                        break;
                    }
                    break;
                case 3:
                    System.out.print("Ingrese un número octal: ");
                    try {
                        String octal = scanner.next();
                        int decimalDesdeOctal = Integer.parseInt(octal, 8);
                        System.out.println("El número decimal es: " + decimalDesdeOctal);
                    } catch (Exception e) {
                        System.out.println("Entrada inválida. Por favor, ingrese un número octal válido.");
                        scanner.nextLine();
                        break;
                    }
                    
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
            System.out.print("¿Desea realizar otra conversión? (s/n): ");
            String respuesta = scanner.next();
            if (!respuesta.equalsIgnoreCase("s")) {
                continuar = false;
            }
        }
        scanner.close();
    }
}