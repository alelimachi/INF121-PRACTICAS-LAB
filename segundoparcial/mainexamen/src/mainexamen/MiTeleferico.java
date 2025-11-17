
package mainexamen;

import java.util.ArrayList;
public class MiTeleferico {
    ArrayList<Linea> lineas;
    float cantidadIngresos;

    public MiTeleferico() {
        lineas = new ArrayList<>();
        cantidadIngresos = 0;
    }

    public void agregarLinea(Linea l) {
        lineas.add(l);
    }

    public void agregarPersonaFila(Persona p, String lineaColor) {
        for (Linea l : lineas)
            if (l.color.equals(lineaColor))
                l.agregarPersona(p);
    }

    public void agregarCabina(String lineaColor, int nroCab) {
        for (Linea l : lineas)
            if (l.color.equals(lineaColor))
                l.agregarCabina(nroCab);
    }

    public boolean verificarReglas() {
        for (Linea l : lineas)
            if (!l.reglasLineaOk())
                return false;
        return true;
    }

    public float calcularTotalIngresos() {
        cantidadIngresos = 0;
        for (Linea l : lineas)
            cantidadIngresos += l.ingresoTotal();
        return cantidadIngresos;
    }

    public Linea lineaMasIngresoRegular() {
        Linea mejor = null;
        float max = -1;

        for (Linea l : lineas) {
            float ingreso = l.ingresoRegular();
            if (ingreso > max) {
                max = ingreso;
                mejor = l;
            }
        }
        return mejor;
    }
    
}
