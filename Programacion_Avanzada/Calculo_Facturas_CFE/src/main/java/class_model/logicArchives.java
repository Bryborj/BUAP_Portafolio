package class_model;

import java.io.*;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class logicArchives {
    private int totalCustomers = 0;
    private int[] customersAreaCount = new int[4];
    private double addSubtotal = 0;
    private double addIVA = 0;
    private double addTotal = 0;

    public void process(String nameArchive) throws IOException {
        File fileIn = new File(nameArchive);

        if (!fileIn.exists()) {
            throw new FileNotFoundException("El archivo no existe: " + nameArchive);
        }

        String suffix = "SALIDA";
        if (nameArchive.startsWith("Clientes-") && nameArchive.endsWith(".txt")) {
            suffix = nameArchive.substring(9, nameArchive.length() - 4);
        }

        resetCounters();

        try (Scanner read = new Scanner(fileIn);
                BufferedWriter writingRoster = new BufferedWriter(new FileWriter("Nomina-" + suffix + ".txt"))) {
                    
            while (read.hasNext()) {
                if (read.hasNextLong()) {
                    long meter = read.nextLong();
                    String paternname = read.next();
                    String lastname = read.next();
                    String name = read.next();
                    String area = read.next();
                    int kw = read.nextInt();

                    Customer customer = new Customer(meter, paternname, lastname, name, area, kw);

                    writingRoster.write(customer.generateReceipt());

                    updateStatistics(customer);
                } else {
                    read.next();
                }
            }

            generateReceipt(suffix);

            JOptionPane.showMessageDialog(null, "Porceso terminado exitosamente.\nArchivos generados: Nomina y Resumen");
        }
    }
    
    public void updateStatistics(Customer customer) {
        totalCustomers++;
        addSubtotal += customer.calculateSubtotal();
        addIVA += customer.calculateIVA();
        addTotal += customer.calculateTotal();

        switch (customer.getArea().toUpperCase()) {
            case "A" -> customersAreaCount[0]++;
            case "B" -> customersAreaCount[1]++;
            case "C" -> customersAreaCount[2]++;
            case "D" -> customersAreaCount[3]++;
        }
    }

    public void generateReceipt(String suffix){
        try (BufferedWriter writingSummary = new BufferedWriter(new FileWriter("Resumen-" + suffix + ".txt"))) {
            writingSummary.write("RESUMEN DE FACTURACION CFE\n");
            writingSummary.write("---------------------------------------\n");
            writingSummary.write(String.format("TOTAL DE CLIENTES: %d\n", totalCustomers));
            writingSummary.write(String.format("TOTAL CLIENTES ZONA A: %d\n", customersAreaCount[0]));
            writingSummary.write(String.format("TOTAL CLIENTES ZONA B: %d\n", customersAreaCount[1]));
            writingSummary.write(String.format("TOTAL CLIENTES ZONA C: %d\n", customersAreaCount[2]));
            writingSummary.write(String.format("TOTAL CLIENTES ZONA D: %d\n", customersAreaCount[3]));
            writingSummary.write(String.format("TOTAL SUBTOTAL: %.2f\n", addSubtotal));
            writingSummary.write(String.format("TOTAL IMPUESTO: %.2f\n", addIVA));
            writingSummary.write(String.format("TOTAL GENERAL: %.2f\n", addTotal));
            writingSummary.write("---------------------------------------\n");
        } catch (IOException e) {
        }
    }

    public void resetCounters() {
        totalCustomers = 0;
        customersAreaCount = new int[4];
        addSubtotal = 0;
        addIVA = 0;
        addTotal = 0;
    }
}
