package figuras;

import java.util.Random;

public class Figuras {

    public static void main(String[] args) {
        Random rand = new Random();
        Figura[] figuras = new Figura[5];

        for (int i = 0; i < figuras.length; i++) {
            int tipo = rand.nextInt(2) + 1; 
            String color = (rand.nextBoolean()) ? "Rojo" : "Azul";

            if (tipo == 1) {
                double lado = 1 + rand.nextInt(10);
                figuras[i] = new Cuadrado(color, lado);
            } else {
                double radio = 1 + rand.nextInt(10);
                figuras[i] = new Circulo(color, radio);
            }
        }
        for (Figura f : figuras) {
            System.out.println(f);
            System.out.println("Área: " + f.area());
            System.out.println("Perímetro: " + f.perimetro());

            if (f instanceof Coloreado) {
                System.out.println(((Coloreado) f).comoColorear());
            }

            System.out.println("-------------------------");
        }
    }
}
   