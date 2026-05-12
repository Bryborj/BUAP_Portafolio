package model;

import java.time.LocalDateTime;

/**
 * Clase intermedia entre Persona y sus subtipos.
 */
public abstract class Asistente extends Persona {
    protected String corredorId;
    protected String facultad;
    protected LocalDateTime fechaRegistro;

    public Asistente(String nombre, String apellidoP, String apellidoM, int edad, String facultad) {
        super(nombre, apellidoP, apellidoM, edad);
        this.facultad = facultad;
        this.fechaRegistro = LocalDateTime.now();
    }

    public void setCorredorId(String id) { this.corredorId = id; }
    public String getCorredorId() { return corredorId; }

    public boolean confirmarRegistro() {
        return nombre != null && !nombre.isEmpty();
    }

    public String toStringCompacto() {
        return corredorId + " - " + mostrarDatos() + " | Facultad: " + facultad;
    }
}
