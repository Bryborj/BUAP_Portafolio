package class_model;

public class Customer {
    private long meter;
    private String paternname;
    private String lastname;
    private String name;
    private String area;
    private int kw;

    public Customer(long meter, String paternname, String lastname, String name, String area, int kw) {
        this.meter = meter;
        this.paternname = paternname;
        this.lastname = lastname;
        this.name = name;
        this.area = area;
        this.kw = kw;
    }

    public double calculateSubtotal() {
        double price = 0;
        price = switch (area) {
            case "A" -> 5.00;
            case "B" -> 10.00;
            case "C" -> 15.00;
            case "D" -> 20.00;
            default -> 0;
        };
        return kw * price;
    }

    public double calculateIVA() {
        return calculateSubtotal() * 0.16;
    }

    public double calculateTotal() {
        return calculateSubtotal() + calculateIVA();
    }

    public String generateReceipt() {
        StringBuilder receipt = new StringBuilder();

        receipt.append("---------------------------------------\n");
        receipt.append("|               CFE                   |\n");
        receipt.append("|        DELEGACION PUEBLA            |\n");
        receipt.append("---------------------------------------\n");
        receipt.append(String.format("|PATERNO: %-28s|\n", paternname));
        receipt.append(String.format("|MATERNO: %-28s|\n", lastname));
        receipt.append(String.format("|NOMBRE:  %-28s|\n", name));
        receipt.append("---------------------------------------\n");
        receipt.append(String.format("|MED: %-12d|ZONA: %-13s|\n", meter, area));
        receipt.append("---------------------------------------\n");
        receipt.append(String.format("|CONSUMO: %-28d|\n", kw));
        receipt.append("---------------------------------------\n");
        receipt.append(String.format("|SUBTOTAL: %27.2f|\n", calculateSubtotal()));
        receipt.append(String.format("|IMPUESTO: %27.2f|\n", calculateIVA()));
        receipt.append(String.format("|TOTAL:    %27.2f|\n", calculateTotal()));
        receipt.append("---------------------------------------\n\n");

        return receipt.toString();
    }

    public String getArea() {
        return area;
    }
}
