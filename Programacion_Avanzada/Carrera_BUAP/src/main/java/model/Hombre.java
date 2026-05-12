package model;

public class Hombre extends Asistente {

    public Hombre(String nombre, String apellidoP, String apellidoM, int edad, String facultad) {
        super(nombre, apellidoP, apellidoM, edad, facultad);
    }

    public void mostrarFoto() {
        System.out.println("Mostrando foto del corredor masculino: " + nombre);
    }
}
