package model;

public class Mujer extends Asistente {

    public Mujer(String nombre, String apellidoP, String apellidoM, int edad, String facultad) {
        super(nombre, apellidoP, apellidoM, edad, facultad);
    }

    public void mostrarFoto() {
        System.out.println("Mostrando foto de la corredora femenina: " + nombre);
    }
}
