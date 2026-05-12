package model;

public class AutorInfo {
    private String nombreCompleto = "Bryan Albino Borges";
    private String curso = "Programación Avanzada";
    private String matricula = "202423701";
    private int numeroLista = 2;

    public void mostrarAutor() {
        System.out.println("Autor: " + nombreCompleto);
        System.out.println("Curso: " + curso);
        System.out.println("Matrícula: " + matricula);
        System.out.println("Número de lista: " + numeroLista);
    }
}
