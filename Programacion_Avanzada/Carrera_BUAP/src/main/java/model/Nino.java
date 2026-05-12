package model;

public class Nino extends Asistente {
    private String tutor;
    private String telefono;
    private String escuela;

    public Nino(String nombre, String apellidoP, String apellidoM, int edad,
                String tutor, String telefono, String escuela) {
        super(nombre, apellidoP, apellidoM, edad, "N/A");
        this.tutor = tutor;
        this.telefono = telefono;
        this.escuela = escuela;
    }

    public void mostrarFoto() {
        System.out.println("Mostrando foto del niño participante: " + nombre);
    }

    @Override
    public String toStringCompacto() {
        return corredorId + " - " + mostrarDatos() + " | Tutor: " + tutor +
                " | Tel: " + telefono + " | Escuela: " + escuela;
    }
}
