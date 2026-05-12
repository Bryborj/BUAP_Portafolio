package model;

public class Persona {
    protected String nombre;
    protected String apellidoP;
    protected String apellidoM;
    protected int edad;

    public Persona(String nombre, String apellidoP, String apellidoM, int edad) {
        this.nombre = nombre;
        this.apellidoP = apellidoP;
        this.apellidoM = apellidoM;
        this.edad = edad;
    }

    public String getNombre() { return nombre; }
    public String getApellidoP() { return apellidoP; }
    public String getApellidoM() { return apellidoM; }
    public int getEdad() { return edad; }

    public String mostrarDatos() {
        return String.format("%s %s %s (%d años)", nombre, apellidoP, apellidoM, edad);
    }
}
