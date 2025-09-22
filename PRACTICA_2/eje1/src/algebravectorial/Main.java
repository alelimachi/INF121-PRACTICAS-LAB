/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package algebravectorial;

/**
 *
 * @author user
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        AlgebraVectorial v1 = new AlgebraVectorial(1, 2);
        AlgebraVectorial v2 = new AlgebraVectorial(2, 4);

        System.out.println("Vector 1: " + v1);
        System.out.println("Vector 2: " + v2);

        System.out.println("Suma: " + v1.sum(v2));
        System.out.println("Resta: " + v1.rest(v2));
        System.out.println("Prod punto: " + v1.prodPunto(v2));
        System.out.println("Mód v1: " + v1.mod());
        System.out.println("¿perpendiculares?: " + v1.Perpe(v2));
        System.out.println("¿paralelos?: " + v1.Paral(v2));
        System.out.println("Proyección de v1 sobre v2: " + v1.proyeccionSobre(v2));
        System.out.println("Componente de v1  dirección  v2: " + v1.compEn(v2));
    }
}

