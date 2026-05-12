package model;

import javax.swing.*;
import java.awt.*;

public class FPanel extends JPanel {
    private Image imgBackground;

    public FPanel(String imgPath) {
        try {
            java.net.URL url = getClass().getResource(imgPath);
            if (url != null) {
                imgBackground = new ImageIcon(url).getImage();
            } else {
                System.err.println("No se encontró " + imgPath + " en el classpath");
            }
        } catch (Exception e) {
            System.err.println("Error loading background image: " + e.getMessage());
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (imgBackground != null) {
            g.drawImage(imgBackground, 0, 0, getWidth(), getHeight(), this);
        }
    }
}
