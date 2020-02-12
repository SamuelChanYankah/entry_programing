import java.util.Stack;
import java.util.Scanner;
import java.util.EmptyStackException;
import java.lang.NumberFormatException;
/* Task 18  - Refactoring
 * Ndou Pfarelo Rudolph 2019/12/12
 * Refactoring a RPN calculator and also changing the indentation
 */

public class RPN {
	public static void main(String[] args){
		/*Instructions to the user*/
		intruction();
		//RPN runner
		Scanner input = new Scanner(System.in);
		while (input.hasNextLine()){
			String elems = input.nextLine().trim();
			Stack<Integer> stack = RPNc(elems);
			if (stack.size()==1){
				System.out.println(stack.peek());
			}

			else {
				String elements = "";
				for (Integer i: stack){
					elements += i.toString() + ' ';
				}
				System.out.println(elements);
			}
		}
		input.close();//closing scanner
	}

	static Stack<Integer> RPNc(String input){
		Stack<Integer> stack = new Stack<Integer>();
		String[] tokens = input.split(" ");
		for (String token: tokens){
			switch(token){
			case "+":
			case "-":
			case "/":
			case "*":
				try {
					stack.push(calc(token, stack.pop(), stack.pop()));
				}
				catch (EmptyStackException e){
					System.err.println("Error: insufficient input for " + token + " operator.");
				}
				break;
			case "d":
				try {
					stack.push(stack.peek());
				}
				catch (EmptyStackException e){
					System.err.println("Error: Too few elements to duplicate the first element.");
				}
				break;
			case "p":
				try {
					System.out.println(stack.pop());
				}
				catch (EmptyStackException e){
					System.err.println("Error: Can't return first element as there are too few elements.");  
				}
				break;
			default:
				try {
					stack.push(Integer.parseInt(token));
				}
				catch (NumberFormatException e){
					System.err.println("Error: "+ token + " is invalid integer or operator.");  
				}
				break;
			}
		}
		return stack;
	}

	static Integer calc(String operator, Integer first, Integer second){
		Integer result = 0;
		switch (operator){
		case "+":
			result = first + second;
			break;
		case "-":
			result = first - second;
			break;
		case "/":
			result = first / second;
			break;
		case "*":
			result = first * second;
			break;
		default:

		}
		return result;
	}

	static void intruction(){//user input
		System.out.println("Please enter number in reverse polish notation: ");
	}

}
