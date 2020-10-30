// Import the Scanner class
import java.util.Scanner;

// creating class
public class Calculator_JAVA {

    public static void main(String[] args) {
	
	// Create a Scanner object
        Scanner reader = new Scanner(System.in);

	//Print imformation
        System.out.print("Enter two numbers: ");

	// take input from the user
        double first = reader.nextDouble();
        double second = reader.nextDouble();
	
	// Print information
        System.out.print("Enter an operator (+, -, *, /): ");

	// take input from the user
        char operator = reader.next().charAt(0);
	
	// initialize variables
        double result;
	
        switch(operator)
        {
	    // statements
            case '+':
                result = first + second;
                break;

	    // statements
            case '-':
                result = first - second;
                break;

	    // statements
            case '*':
                result = first * second;
                break;

	    // statements
            case '/':
                result = first / second;
                break;

	    // default statements
            default:
                System.out.printf("Error! operator is not correct");
                return;
        }

	// Output of the calculated data
        System.out.printf("%.1f %c %.1f = %.1f", first, operator, second, result);
    }
}