package ui;

import javax.swing.*;
import java.awt.*;
import model.Usuario;
import model.Carrera;
import model.FPanel;

public class LoginFrame extends JFrame {
    private JTextField txtUsuario;
    private JPasswordField txtClave;
    private Carrera carrera;

    public LoginFrame() {
        carrera = new Carrera();
        setTitle("Carrera BUAP 2025 - Login");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        String imgPath = "/images/A CU2_6 (1).png";
        FPanel back = new FPanel(imgPath);
        setContentPane(back);
        back.setLayout(new GridBagLayout());
        JPanel panelCentral = new JPanel();
        panelCentral.setLayout(null);
        panelCentral.setBackground(new Color(0, 51, 200, 100));
        
        panelCentral.setPreferredSize(new Dimension(500, 280)); 

        JLabel lblBanner = new JLabel("CARRERA BUAP 2025", SwingConstants.CENTER);
        lblBanner.setFont(new Font("Segoe UI", Font.BOLD, 26));
        lblBanner.setForeground(Color.WHITE);
        lblBanner.setBounds(0, 10, 500, 40);
        panelCentral.add(lblBanner);

        java.net.URL escudoUrl = getClass().getResource("/images/escudo_negativo.png");
        if (escudoUrl != null) {
            ImageIcon icon = new ImageIcon(escudoUrl);
            Image escudo = icon.getImage().getScaledInstance(120, 120, Image.SCALE_SMOOTH);
            JLabel lblEscudo = new JLabel(new ImageIcon(escudo));
            lblEscudo.setBounds(40, 80, 120, 120);
            panelCentral.add(lblEscudo);
        } else {
            System.err.println("No se encontró /images/logo_buap.jpg en el classpath");
        }

        JLabel lblUsuario = new JLabel("Usuario:");
        JLabel lblClave = new JLabel("Contraseña:");
        lblUsuario.setForeground(Color.WHITE);
        lblClave.setForeground(Color.WHITE);
        lblUsuario.setFont(new Font("Segoe UI", Font.BOLD, 14));
        lblClave.setFont(new Font("Segoe UI", Font.BOLD, 14));

        txtUsuario = new JTextField();
        txtClave = new JPasswordField();

        lblUsuario.setBounds(190, 90, 100, 25);
        txtUsuario.setBounds(290, 90, 150, 25);
        lblClave.setBounds(190, 130, 100, 25);
        txtClave.setBounds(290, 130, 150, 25);

        panelCentral.add(lblUsuario);
        panelCentral.add(txtUsuario);
        panelCentral.add(lblClave);
        panelCentral.add(txtClave);

        JButton btnIngresar = new JButton("Ingresar");
        JButton btnSalir = new JButton("Salir");
        btnIngresar.setBounds(100, 220, 100, 35);
        btnSalir.setBounds(300, 220, 100, 35);
        panelCentral.add(btnIngresar);
        panelCentral.add(btnSalir);

        btnIngresar.setBackground(new Color(255, 215, 0)); // dorado BUAP
        btnSalir.setBackground(new Color(200, 0, 0));
        btnIngresar.setForeground(Color.BLACK);
        btnSalir.setForeground(Color.WHITE);
        btnIngresar.setFocusPainted(false);
        btnSalir.setFocusPainted(false);

        btnSalir.addActionListener(e -> msg());
        btnIngresar.addActionListener(e -> validarLogin());

        GridBagConstraints gbc = new GridBagConstraints();
        back.add(panelCentral, gbc); 
    }

    private void validarLogin() {
        String usuario = txtUsuario.getText();
        String clave = new String(txtClave.getPassword());

        Usuario u1 = new Usuario("lola", "1234");
        Usuario u2 = new Usuario("emma", "12345678");
        Usuario u3 = new Usuario("laura", "alb2c3");

        if (u1.autenticar(usuario, clave) ||
            u2.autenticar(usuario, clave) ||
            u3.autenticar(usuario, clave)) {

            JOptionPane.showMessageDialog(this, "Bienvenido/a " + usuario + "!");
            VentanaPrincipal vp = new VentanaPrincipal(carrera, this);
            vp.setVisible(true);
            this.setVisible(false);
        } else {
            JOptionPane.showMessageDialog(this, "Usuario o contraseña incorrectos.",
                    "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void msg(){
        int op = JOptionPane.showConfirmDialog(this, "¿Está seguro de salir?",
                "Confirmación", JOptionPane.YES_NO_OPTION);

        if (op == JOptionPane.YES_OPTION) {
            System.exit(0);
        }
    }
}