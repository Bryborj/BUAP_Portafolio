package ui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import model.Carrera;
import model.FPanel;
import model.AutorInfo;

public class VentanaPrincipal extends JFrame {
    private JFrame LoginFrame;
    private Carrera carrera;
    private AutorInfo autorInfo;

    public VentanaPrincipal(Carrera carrera, JFrame LoginFrame) {
        this.LoginFrame = LoginFrame;
        this.carrera = carrera;
        String imgCarrera = "../images/Carrera.jpg";
        String imgBUAP = "../images/escudo_negativo.png";
        FPanel backCorredor = new FPanel(imgCarrera);
        FPanel backBUAP = new FPanel(imgBUAP);

        setTitle("Carrera BUAP 2025 - Menú Principal");
        this.setExtendedState(JFrame.MAXIMIZED_BOTH);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        

        setLayout(new BorderLayout());

        JPanel panelHeader = new JPanel();
        panelHeader.setLayout(new BoxLayout(panelHeader, BoxLayout.Y_AXIS));
        panelHeader.setBorder(BorderFactory.createEmptyBorder(20, 0, 20, 0));
        panelHeader.setBackground(new Color(0, 51, 102));

        JLabel lblTitulo = new JLabel("CARRERA BUAP 2025");
        lblTitulo.setFont(new Font("Monospaced", Font.BOLD, 36));
        lblTitulo.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblTitulo.setForeground(Color.WHITE);

        JLabel lblSubtitulo = new JLabel("MENU GENERAL");
        lblSubtitulo.setFont(new Font("Serif", Font.PLAIN, 24));
        lblSubtitulo.setAlignmentX(Component.CENTER_ALIGNMENT);
        lblSubtitulo.setForeground(Color.WHITE);

        panelHeader.add(lblTitulo);
        panelHeader.add(Box.createRigidArea(new Dimension(0, 10)));
        panelHeader.add(lblSubtitulo);

        JPanel panelFooter = new JPanel();
        panelFooter.setLayout(new BorderLayout(10, 10));
        panelFooter.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createMatteBorder(1, 0, 0, 0, Color.GRAY), 
                BorderFactory.createEmptyBorder(10, 20, 10, 20) 
        ));
        panelFooter.setBackground(new Color(0, 51, 102));


        JButton btnAutor = new JButton("AUTOR");
        btnAutor.setBackground(new Color(255, 215, 0));
        btnAutor.setForeground(Color.BLACK);
        btnAutor.setFocusPainted(false);
        btnAutor.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));


        JButton btnSalir = new JButton("SALIR");
        btnSalir.setBackground(new Color(255, 0, 0));
        btnSalir.setForeground(Color.WHITE);
        btnSalir.setFocusPainted(false);
        btnSalir.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));

        panelFooter.add(btnAutor, BorderLayout.WEST);
        panelFooter.add(btnSalir, BorderLayout.EAST);

        JPanel panelBody = new JPanel();
        panelBody.setLayout(new GridLayout(1, 3, 30, 0));
        panelBody.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panelBody.setBackground(new Color(0, 51, 102));

        JPanel panelIzquierdo = backCorredor;

        JPanel panelCentro = new JPanel(new GridBagLayout());
        panelCentro.setBackground(new Color(0, 51, 102));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(15, 0, 15, 0);
        gbc.gridx = 0;

        Font botonFont = new Font("Arial", Font.BOLD, 16);

        JButton btnHombres = new JButton("HOMBRES");
        btnHombres.setFont(botonFont);
        btnHombres.setBackground(new Color(255, 215, 0));
        btnHombres.setForeground(Color.BLACK);
        btnHombres.setFocusPainted(false);
        btnHombres.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        gbc.gridy = 0;
        panelCentro.add(btnHombres, gbc);

        JButton btnMujeres = new JButton("MUJERES");
        btnMujeres.setFont(botonFont);
        btnMujeres.setBackground(new Color(255, 215, 0));
        btnMujeres.setForeground(Color.BLACK);
        btnMujeres.setFocusPainted(false);
        btnMujeres.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        gbc.gridy = 1;
        panelCentro.add(btnMujeres, gbc);

        JButton btnNinos = new JButton("NIÑOS");
        btnNinos.setFont(botonFont);
        btnNinos.setBackground(new Color(255, 215, 0));
        btnNinos.setForeground(Color.BLACK);
        btnNinos.setFocusPainted(false);
        btnNinos.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        gbc.gridy = 2;
        panelCentro.add(btnNinos, gbc);
        
        JPanel panelDerecho = backBUAP;
        panelDerecho.setBackground(new Color(0, 51, 102));

        panelBody.add(panelIzquierdo);
        panelBody.add(panelCentro);
        panelBody.add(panelDerecho);

        add(panelHeader, BorderLayout.NORTH);
        add(panelBody, BorderLayout.CENTER);
        add(panelFooter, BorderLayout.SOUTH);

        btnHombres.addActionListener(e -> this.showRegistroHombres());
        btnMujeres.addActionListener(e -> this.showRegistroMujeres());
        btnNinos.addActionListener(e -> showRegistroNinos());
        btnAutor.addActionListener(e -> showAutorMsg());

        btnSalir.addActionListener(e -> {
            LoginFrame.setVisible(true);
            this.dispose();
        });

        configClose();
    }

    private void configClose() {
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                LoginFrame.setVisible(true);
            }
        });
    }

    private void showRegistroHombres() {
        new VentanaRegistroHombres(carrera, this).setVisible(true);
        this.setVisible(false);
    }

    private void showRegistroMujeres() {
        new VentanaRegistroMujeres(carrera, this).setVisible(true);
        this.setVisible(false);
    }
    
    private void showRegistroNinos() {
        new VentanaRegistroNinos(carrera, this).setVisible(true);
        this.setVisible(false);
    }

    private void showAutorMsg() {
        JOptionPane.showMessageDialog(this, "Autor: Bryan Albino Borges\n"
                   + "Curso: Programación Avanzada\n"
                   + "Proyecto: Carrera BUAP 2025\n"
                   + "Número de lista: 2", 
                "Autor", JOptionPane.INFORMATION_MESSAGE);
    }
}