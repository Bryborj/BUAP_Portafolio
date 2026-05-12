package model;

public class Usuario {
    private String username;
    private String clave;

    public Usuario(String username, String clave) {
        this.username = username;
        this.clave = clave;
    }

    public boolean autenticar(String user, String pass) {
        return username.equals(user) && clave.equals(pass);
    }
}
