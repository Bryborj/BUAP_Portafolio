package model;

import java.util.*;
import javax.swing.JOptionPane;

public class Carrera {
    private List<Hombre> hombres = new ArrayList<>();
    private List<Mujer> mujeres = new ArrayList<>();
    private List<Nino> ninos = new ArrayList<>();
    private int consecutivoH = 1, consecutivoM = 1, consecutivoN = 1;

    public boolean registrarAsistente(Asistente a) {
        if (!a.confirmarRegistro())
            return false;
        asignarIdYAgregar(a);
        return true;
    }

    public void asignarIdYAgregar(Asistente a) {
        if (a instanceof Hombre) {
            a.setCorredorId("H-" + String.format("%04d", consecutivoH++));
            hombres.add((Hombre) a);
        } else if (a instanceof Mujer) {
            a.setCorredorId("M-" + String.format("%04d", consecutivoM++));
            mujeres.add((Mujer) a);
        } else if (a instanceof Nino) {
            a.setCorredorId("N-" + String.format("%04d", consecutivoN++));
            ninos.add((Nino) a);
        }
    }

    
    public void listar1() {
        StringBuilder sb = new StringBuilder();
        sb.append("--- LISTADO INDIVIDUAL ---\n");
        if (hombres.isEmpty()) {
            sb = new StringBuilder();
            sb.append("No hay participantes registrados.\n");
            JOptionPane.showMessageDialog(null, sb.toString());
            return;
        } else {
            for (Asistente a : getTodos()) {
                JOptionPane.showMessageDialog(null, a.toStringCompacto(),
                        "Participante", JOptionPane.INFORMATION_MESSAGE);
            }
        }
    }

    
    public void listar2() {
        List<Asistente> todos = new ArrayList<>(getTodos());
        todos.sort(Comparator.comparing(a -> a.nombre));
        StringBuilder sb = new StringBuilder("=== LISTADO ORDENADO ===\n");
        for (Asistente a : todos)
            sb.append(a.toStringCompacto()).append("\n");
        if (todos.isEmpty()) {
            sb = new StringBuilder();
            sb.append("No hay participantes registrados.\n");
            JOptionPane.showMessageDialog(null, sb.toString());
            return;
        }
        JOptionPane.showMessageDialog(null, sb.toString());
        listarInformes();
    }

    
    public void buscar(String texto) {
        List<Asistente> encontrados = new ArrayList<>();
        for (Asistente a : getTodos()) {
            if (a.nombre.equalsIgnoreCase(texto)
                    || a.apellidoP.equalsIgnoreCase(texto)
                    || a.apellidoM.equalsIgnoreCase(texto)) {
                encontrados.add(a);
            }
        }

        if (encontrados.isEmpty()) {
            JOptionPane.showMessageDialog(null, "No se encontró ningún participante con ese nombre.");
        } else {
            StringBuilder sb = new StringBuilder("Resultados de búsqueda:\n");
            for (Asistente a : encontrados)
                sb.append(a.toStringCompacto()).append("\n");
            JOptionPane.showMessageDialog(null, sb.toString());
        }
    }

    
    private List<Asistente> getTodos() {
        List<Asistente> todos = new ArrayList<>();
        todos.addAll(hombres);
        todos.addAll(mujeres);
        todos.addAll(ninos);
        return todos;
    }

    // Para depuración o consola
    public void listarInformes() {
        System.out.println("=== HOMBRES ===");
        hombres.forEach(h -> System.out.println(h.toStringCompacto()));
        System.out.println("=== MUJERES ===");
        mujeres.forEach(m -> System.out.println(m.toStringCompacto()));
        System.out.println("=== NIÑOS ===");
        ninos.forEach(n -> System.out.println(n.toStringCompacto()));
    }
}
