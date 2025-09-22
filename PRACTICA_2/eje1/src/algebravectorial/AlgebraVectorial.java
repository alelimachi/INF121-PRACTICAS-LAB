
package algebravectorial;
public class AlgebraVectorial {
    public double x;
    public double y;

    public AlgebraVectorial(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public AlgebraVectorial sum(AlgebraVectorial v) {
        return new AlgebraVectorial(this.x + v.x, this.y + v.y);
    }

    public AlgebraVectorial rest(AlgebraVectorial v) {
        return new AlgebraVectorial(this.x - v.x, this.y - v.y);
    }

    public double prodPunto(AlgebraVectorial v) {
        return this.x * v.x + this.y * v.y;
    }
    public double mod() {
        return Math.sqrt(this.x * this.x + this.y * this.y);
    }
    public boolean Perpe(AlgebraVectorial v) {
        return this.prodPunto(v) == 0;
    }

    public boolean Paral(AlgebraVectorial v) {
        return this.x * v.y == this.y * v.x;
    }

    public AlgebraVectorial proyeccionSobre(AlgebraVectorial b) {
        double esc = this.prodPunto(b) / (b.prodPunto(b));
        return new AlgebraVectorial(b.x * esc, b.y * esc);
    }
    
    public double compEn(AlgebraVectorial b) {
        return this.prodPunto(b) / b.mod();
    }
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
    
