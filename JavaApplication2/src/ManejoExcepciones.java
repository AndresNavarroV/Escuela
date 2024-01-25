public class ManejoExcepciones {

    public static void main(String[] args) {
        try {
            // Código que podría generar un error
            int divisor = 0;
            int resultado = 10 / divisor;

            // Este código no se ejecutará si se produce una excepción antes
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            // Manejo de la excepción específica para la división por cero
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            // Manejo de cualquier otra excepción
            System.err.println("Error desconocido: " + e.getMessage());
        } finally {
            // Este bloque se ejecutará siempre, independientemente de si se produjo una excepción o no
            System.out.println("Bloque finally: Operación finalizada");
        }
    }
}
