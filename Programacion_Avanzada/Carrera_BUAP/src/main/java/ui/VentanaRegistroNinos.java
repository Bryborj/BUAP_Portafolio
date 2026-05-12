package ui;

import javax.swing.*;
import java.awt.*;
import model.*;
import ui.*;

public class VentanaRegistroNinos extends JFrame {
    private Carrera carrera;
    private JTextField txtNombre, txtApellidoP, txtApellidoM, txtEdad;
    private JTextField txtTutor, txtTelefono, txtEscuela;
    private JFrame ventanaPrincipal;

    public VentanaRegistroNinos(Carrera carrera, JFrame ventanaPrincipal) {
        this.carrera = carrera;
        this.ventanaPrincipal = ventanaPrincipal;
        String imgFondo = "../images/Niños.png";
        FPanel back = new FPanel(imgFondo);

        setTitle("Registro de Niños");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        setLocationRelativeTo(null);
        getContentPane().setBackground(new Color(0,51,102));
        setLayout(new BorderLayout(0,10));

        JPanel pHeader = new JPanel();
        pHeader.setLayout(new BoxLayout(pHeader, BoxLayout.Y_AXIS));
        pHeader.setBorder(BorderFactory.createEmptyBorder(20, 0, 20, 0));
        pHeader.setBackground(new Color(0, 51, 102));
        pHeader.setOpaque(false);

        JLabel lblTitulo = new JLabel("CARRETA BUAP 2025");
        lblTitulo.setFont(new Font("Serif", Font.PLAIN, 36));
        lblTitulo.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblTitulo.setForeground(Color.WHITE);

        JLabel lblSubtitulo = new JLabel("REGISTRO DE ASISTENTES NIÑOS");
        lblSubtitulo.setFont(new Font("Serif", Font.PLAIN, 20));
        lblSubtitulo.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblSubtitulo.setForeground(Color.WHITE);

        pHeader.add(lblTitulo);
        pHeader.add(Box.createRigidArea(new Dimension(0, 10)));
        pHeader.add(lblSubtitulo);

        add(pHeader, BorderLayout.NORTH);

        JPanel pFooter = new JPanel(new FlowLayout(FlowLayout.CENTER, 15,25));
        pFooter.setBorder(BorderFactory.createEmptyBorder(1, 0, 0, 0));
        pFooter.setOpaque(false);

        JButton btnRegistrar = new JButton("REGISTRAR");
        btnRegistrar.setBackground(Color.GREEN);
        btnRegistrar.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        JButton btnListar1 = new JButton("LISTAR 1");
        btnListar1.setBackground(Color.WHITE);
        btnListar1.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        JButton btnListar2 = new JButton("LISTAR 2");
        btnListar2.setBackground(Color.WHITE);
        btnListar2.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        JButton btnBuscar = new JButton("BUSCAR");
        btnBuscar.setBackground(Color.CYAN);
        btnBuscar.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        JButton btnRegresar = new JButton("REGRESAR");
        btnRegresar.setBackground(Color.RED);
        btnRegresar.setForeground(Color.WHITE);
        btnRegresar.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));

        pFooter.add(btnRegistrar);
        pFooter.add(btnListar1);
        pFooter.add(btnListar2);
        pFooter.add(btnBuscar);
        pFooter.add(btnRegresar);
        add(pFooter, BorderLayout.SOUTH);

        JPanel pBody = new JPanel(new GridLayout(1, 2, 40, 0));
        pBody.setBorder(BorderFactory.createEmptyBorder(20, 40, 20, 40));
        pBody.setOpaque(false);

        JPanel pFoto = back;
        pFoto.setBackground(new Color(0,51,102));
        pBody.add(pFoto);

        JPanel pForm = new JPanel(new GridBagLayout());
        pForm.setOpaque(false);
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 8, 10, 8);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        JLabel lbl1 = new JLabel("Nombre:");
        lbl1.setForeground(Color.WHITE);
        JLabel lbl2 = new JLabel("Paterno:");
        lbl2.setForeground(Color.WHITE);
        JLabel lbl3 = new JLabel("Materno:");
        lbl3.setForeground(Color.WHITE);
        JLabel lbl4 = new JLabel("Edad:");
        lbl4.setForeground(Color.WHITE);
        JLabel lbl5 = new JLabel("Tutor:");
        lbl5.setForeground(Color.WHITE);
        JLabel lbl6 = new JLabel("Teléfono:");
        lbl6.setForeground(Color.WHITE);
        JLabel lbl7 = new JLabel("Escuela:");
        lbl7.setForeground(Color.WHITE);

        txtNombre = new JTextField(20);
        txtApellidoP = new JTextField(20);
        txtApellidoM = new JTextField(20);
        txtEdad = new JTextField(20);
        txtTutor = new JTextField(20);
        txtTelefono = new JTextField(20);
        txtEscuela = new JTextField();

        gbc.gridx = 0; gbc.gridy = 0; gbc.anchor = GridBagConstraints.LINE_END; // Label a la derecha
        pForm.add(lbl1, gbc);
        gbc.gridx = 1; gbc.gridy = 0; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0; // TextField a la izq.
        pForm.add(txtNombre, gbc);

        gbc.gridx = 0; gbc.gridy = 1; gbc.anchor = GridBagConstraints.LINE_END; gbc.weightx = 0;
        pForm.add(lbl2, gbc);
        gbc.gridx = 1; gbc.gridy = 1; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0;
        pForm.add(txtApellidoP, gbc);

        gbc.gridx = 0; gbc.gridy = 2; gbc.anchor = GridBagConstraints.LINE_END; gbc.weightx = 0;
        pForm.add(lbl3, gbc);
        gbc.gridx = 1; gbc.gridy = 2; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0;
        pForm.add(txtApellidoM, gbc);

        gbc.gridx = 0; gbc.gridy = 3; gbc.anchor = GridBagConstraints.LINE_END; gbc.weightx = 0;
        pForm.add(lbl4, gbc);
        gbc.gridx = 1; gbc.gridy = 3; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0;
        pForm.add(txtEdad, gbc);

        gbc.gridx = 0; gbc.gridy = 4; gbc.anchor = GridBagConstraints.LINE_END; gbc.weightx = 0;
        pForm.add(lbl5, gbc);
        gbc.gridx = 1; gbc.gridy = 4; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0;
        pForm.add(txtTutor, gbc);

        gbc.gridx = 0; gbc.gridy = 5; gbc.anchor = GridBagConstraints.LINE_END; gbc.weightx = 0;
        pForm.add(lbl6, gbc);
        gbc.gridx = 1; gbc.gridy = 5; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0;
        pForm.add(txtTelefono, gbc);

        gbc.gridx = 0; gbc.gridy = 6; gbc.anchor = GridBagConstraints.LINE_END; gbc.weightx = 0;
        pForm.add(lbl7, gbc);
        gbc.gridx = 1; gbc.gridy = 6; gbc.anchor = GridBagConstraints.LINE_START; gbc.weightx = 1.0;
        pForm.add(txtEscuela, gbc);

        pBody.add(pFoto);
        pBody.add(pForm);
        add(pBody, BorderLayout.CENTER);

        btnRegistrar.addActionListener(e -> registrarNino());
        btnRegresar.addActionListener(e -> {
            ventanaPrincipal.setVisible(true);
            this.dispose();
        });
        btnBuscar.addActionListener(e -> {
            String txt = JOptionPane.showInputDialog("Ingrese nombre o apellido");
            if (txt.isEmpty()) {
                return;
            } else {
                carrera.buscar(txt);
            }
        });
        btnListar1.addActionListener(e -> carrera.listar1());
        btnListar2.addActionListener(e -> carrera.listar2());
    }

    private void registrarNino() {
        try {
            String nombre = txtNombre.getText();
            String apP = txtApellidoP.getText();
            String apM = txtApellidoM.getText();
            int edad = Integer.parseInt(txtEdad.getText());
            String tutor = txtTutor.getText();
            String telefono = txtTelefono.getText();
            String escuela = txtEscuela.getText();

            Nino n = new Nino(nombre, apP, apM, edad, tutor, telefono, escuela);
            if (carrera.registrarAsistente(n)) {
                JOptionPane.showMessageDialog(this, "Registro exitoso!");
            } else {
                JOptionPane.showMessageDialog(this, "Error al registrar.");
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Verifica los datos ingresados.");
        }
    }
}
