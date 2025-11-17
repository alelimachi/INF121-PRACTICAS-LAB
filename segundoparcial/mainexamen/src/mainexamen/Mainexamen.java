
package mainexamen;

public class Mainexamen {

    public static void main(String[] args) {
        MiTeleferico mt = new MiTeleferico();
        mt.agregarLinea(new Linea("Amarillo"));
        mt.agregarLinea(new Linea("Rojo"));
        mt.agregarLinea(new Linea("Verde"));

        mt.agregarCabina("Amarillo", 1);
        mt.agregarCabina("Amarillo", 2);

        mt.agregarPersonaFila(new Persona("Ana", 20, 60), "Amarillo");
        mt.agregarPersonaFila(new Persona("Luis", 30, 80), "Amarillo");
        mt.agregarPersonaFila(new Persona("Carlos", 70, 70), "Amarillo");

        Linea amarilla = mt.lineas.get(0);
        amarilla.agregarPrimeraPersonaACabina(1);
        amarilla.agregarPrimeraPersonaACabina(1);
        System.out.println("Reglas: " + mt.verificarReglas());
        System.out.println("Total ingresos: " + mt.calcularTotalIngresos());
        Linea mejor = mt.lineaMasIngresoRegular();
        System.out.println("Línea con más ingreso regular: " + mejor.color);
    }
}

    
    
