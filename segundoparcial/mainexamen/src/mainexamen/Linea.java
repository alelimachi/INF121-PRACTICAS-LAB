package mainexamen;

import java.util.ArrayList;

public class Linea {
    String color;
    ArrayList<Persona> filaPersonas;
    ArrayList<Cabina> cabinas;
    int cantidadCabinas;

    public Linea(String color) {
        this.color = color;
        filaPersonas = new ArrayList<>();
        cabinas = new ArrayList<>();
        cantidadCabinas = 0;
    }

    public void agregarPersona(Persona p) {
        filaPersonas.add(p);
    }

    public void agregarCabina(int nroCab) {
        cabinas.add(new Cabina(nroCab));
        cantidadCabinas++;
    }

    public boolean agregarPrimeraPersonaACabina(int nroX) {
        if (filaPersonas.isEmpty())
            return false;

        for (Cabina c : cabinas) {
            if (c.nroCabina == nroX) {
                Persona p = filaPersonas.remove(0);
                return c.agregarPersona(p);
            }
        }
        return false;
    }

    public boolean reglasLineaOk() {
        for (Cabina c : cabinas) {
            if (!c.reglasOk())
                return false;
        }
        return true;
    }

    public float ingresoTotal() {
        float total = 0;
        for (Cabina c : cabinas)
            total += c.calcularIngreso();
        return total;
    }

    public float ingresoRegular() {
        float total = 0;
        for (Cabina c : cabinas) {
            for (Persona p : c.personasAbordo) {
                if (p.edad >= 25 && p.edad <= 60)
                    total += 3f;
            }
        }
        return total;
    }
}
    
