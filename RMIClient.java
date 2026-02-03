import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("16.171.10.19", 1099);

            Calculator calc = (Calculator) registry.lookup("CalcService");

            System.out.println("Addition: " + calc.add(10, 5));
            System.out.println("Subtraction: " + calc.subtract(20, 3));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
