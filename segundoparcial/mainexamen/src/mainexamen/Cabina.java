
package mainexamen;

import java.util.ArrayList;

public class Cabina {
    int nroCabina;
    ArrayList<Persona> personasAbordo;

    public Cabina(int nroCabina) {
        this.nroCabina = nroCabina;
        this.personasAbordo = new ArrayList<>();
    }
    public boolean agregarPersona(Persona p) {
        if (personasAbordo.size() >= 10)
            return false;

        float pesoTotal = 0;
        for (Persona per : personasAbordo)
            pesoTotal += per.pesoPersona;

        if (pesoTotal + p.pesoPersona > 850)
            return false;

        personasAbordo.add(p);
        return true;
    }
    public boolean reglasOk() {
        if (personasAbordo.size() > 10)
            return false;

        float peso = 0;
        for (Persona p : personasAbordo)
            peso += p.pesoPersona;

        return peso <= 850;
    }
    public float calcularIngreso() {
        float total = 0;
        for (Persona p : personasAbordo) {
            if (p.edad < 25 || p.edad > 60)
                total += 1.5f;
            else
                total += 3f;
        }
        return total;
    }
}

    
