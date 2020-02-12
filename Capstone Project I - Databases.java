/* Capstone Project I - Databases
 * Ndou Pfarelo Rudolph 2020/01/27
 * Program that can be used by a bookstore clerk.
 */
import java.util.*;
import java.sql.*;

public class BookClerk {
	public static void main ( String [] args ) {
		try (
				// Allocate a database 'Connection' object
				Connection conn = DriverManager . getConnection (
						"jdbc:mysql://localhost:3306/library_db?useSSL=false&allowPublicKeyRetrieval=true", //Establish connection with database.
		                "myuser", "xxxx" );
				// Allocate a 'Statement' object in the Connection
				Statement stmt = conn . createStatement ();
				) {
			
			Scanner input = new Scanner(System.in);
			int selection = 0;
			
			//Menu for action selection and user input
			while(selection != 5) {
				System.out.println("Please enter the number corresponding to the action you would like to take:\n"
						+ "1. Enter book\n"
						+ "2. Update book\n"
						+ "3. Delete book\n"
						+ "4. Search books\n"
						+ "5. Exit");
				selection = input.nextInt();
			
				//Selection sorting
				if(selection == 1) {
					//Collecting book information
					input.nextLine(); //Any lines identical to this just clear the line issue going from nextInt() to nextLine()
					System.out.print("Please enter the Title of the book you would like to put into the system: ");
					String title = input.nextLine();
					System.out.print("Please enter the Author of said book: ");
					String author = input.nextLine();
					System.out.print("Please enter the number of said book currently in stock: ");
					int qty = input.nextInt();
				
					//Sending info to the addBook method
					addBook(title, author, qty, stmt);
				} else if(selection == 2) {
					//Collecting book information
					System.out.println("Please enter the id of the book you would like to update: ");
					int id = input.nextInt();
				
					//Sending info to the updateBook method
					updateBook(id, stmt, input);
				} else if(selection == 3) {
					//Collecting book information
					System.out.print("Please enter the id of the book you would like to delete from the system: ");
					int id = input.nextInt();
				
					//Sending info to deleteBook method
					deleteBook(id, stmt);
				} else if(selection == 4) {
					searchStore(stmt, input);
				} else if(selection == 5) {
					System.out.println("Goodbye");
					input.close();
				} else { //Invalid entry handler
					System.out.println("Sorry, that isn't a valid selection.");
				}
			}
			
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}
	
	public static void addBook(String title, String author, int qty, Statement stmt) {
		try {
			//Automatically assigns the book's id as 1 above the current max
			String strMaxId = "select max(id) from books";
			ResultSet rset = stmt.executeQuery(strMaxId);
			rset.next();
			int id = rset.getInt(1) + 1;
		
			//Putting quotes around string values
			title = '"' + title + '"';
			author = '"' + author + '"';
		
			//Inserting the book into the system
			String strInsert = "insert into books "
					+ "values(" + id + ", " + title + ", " + author + ", " + qty + ")";
			int countInserted = stmt.executeUpdate(strInsert);
			System.out.println(countInserted + " book has been entered.\n");
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}

	public static void updateBook(int id, Statement stmt, Scanner input) {
		try {
			//Shows the information of the book to be updated
			String strDisplay = "select * from books "
					+ "where id = " + id;
			ResultSet rset = stmt.executeQuery(strDisplay);
			rset.next();
			String rTitle = rset.getString("Title");
			String rAuthor = rset.getString("Author");
			int rQty = rset.getInt("Qty");
			System.out.println("Here is the current information on the selected book:");
			System.out.println("Title: " + rTitle + "\n"
					+ "Author: " + rAuthor + "\n"
					+ "Quantity: " + rQty + "\n");
		
			//Asks the user which field they want to change and collects the response
			int selection = 0;
		
			while(selection != 4) {
				System.out.println("Please enter the number corresponding to the field you would like to change:\n"
						+ "1. Title\n"
						+ "2. Author\n"
						+ "3. Quantity\n"
						+ "4. Return");
				selection = input.nextInt();
		
				if(selection == 1) { //Updates the title
					input.nextLine();
					System.out.print("Please enter the new title: ");
					String newTitle = "'" + input.nextLine() + "'";
			
					String strUpdate = "update books "
							+ "set Title = " + newTitle + " "
							+ "where id = " + id;
					int countUpdate = stmt.executeUpdate(strUpdate);
					System.out.println(countUpdate + " book has been updated.\n");
				} else if(selection == 2) { //Updates the author
					input.nextLine();
					System.out.print("Please enter the new author: ");
					String newAuthor = "'" + input.nextLine() + "'";
			
					String strUpdate = "update books "
							+ "set Author = " + newAuthor + " "
							+ "where id = " + id;
					int countUpdate = stmt.executeUpdate(strUpdate);
					System.out.println(countUpdate + " book has been updated.\n");
				} else if(selection == 3) { //Updates the quantity
					System.out.print("Please enter the new quantity: ");
					int newQty = input.nextInt();
			
					String strUpdate = "update books "
							+ "set Qty = " + newQty + " "
							+ "where id = " + id;
					int countUpdate = stmt.executeUpdate(strUpdate);
					System.out.println(countUpdate + " book has been updated.\n");
				} else if(selection == 4) { //Returns to the main menu
					System.out.println("Returning to main menu.\n");
				} else { //Invalid entry handler
					System.out.println("Sorry, that isn't a valid selection.\n");
				}
			}
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}

	public static void deleteBook(int id, Statement stmt) {
		try {
			//Deletes the book with the entered id from the database
			String strDelete = "delete from books "
					+ "where id = " + id;
			int countDeleted = stmt.executeUpdate(strDelete);
			if(countDeleted == 1) {
				System.out.println(countDeleted + " book has been deleted.\n");
			} else {
				System.out.println("No books have been deleted.\n");
			}
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}

	public static void searchStore(Statement stmt, Scanner input) {
		try {
			//Asks the user which field to search by and collects the response
			int selection = 0;
			while(selection != 5) {
				System.out.println("What field would you like to search for? Please enter the corresponding number:\n"
						+ "1. ID\n"
						+ "2. Title\n"
						+ "3. Author\n"
						+ "4. Quantity\n"
						+ "5. Return");
				selection = input.nextInt();
		
				if(selection == 1) { //Searches via a specific id
					System.out.print("Please enter the ID of the book: ");
					int bookData = input.nextInt();
			
					//Searches the database for the given ID
					String strSelect = "select * from books "
							+ "where id = " + bookData;
					ResultSet rset = stmt.executeQuery(strSelect);
			
					System.out.println("\nHere is the book with the given ID:");
					resultSetPrinter(rset); //ResultSet sent to resultSetPrinter to show results
				} else if(selection == 2) { //Searches via a full or partial Title
					input.nextLine();
					System.out.print("Please enter a full or partial title for the book: ");
					String bookData = input.nextLine();
			
					//Searches the database for the given Title
					String strSelect = "select * from books "
							+ "where Title = '=" + bookData + "='";
					ResultSet rset = stmt.executeQuery(strSelect);
			
					System.out.println("\nHere are the books that contain the given title:");
					resultSetPrinter(rset); //ResultSet sent to resultSetPrinter to show results
			
				} else if(selection == 3) { //Searches via a full or partial Author
					input.nextLine();
					System.out.print("Please enter a full or partial author name for a list of their books: ");
					String bookData = input.nextLine();
			
					//Searches the database for the given Author
					String strSelect = "select * from books "
							+ "where Author = '=" + bookData + "='";
					ResultSet rset = stmt.executeQuery(strSelect);
			
					System.out.println("\nHere are the books that were written by authors containing your entry:");
					resultSetPrinter(rset); //ResultSet sent to resultSetPrinter to show results
				} else if(selection == 4) { //Searches via the number in stock
					System.out.print("Please enter a quantity and books with that quantity or less in stock will be shown: ");
					int bookData = input.nextInt();
			
					//Searches the database for the given quantity
					String strSelect = "select * from books "
						+ "where Qty <= " + bookData;
					ResultSet rset = stmt.executeQuery(strSelect);
			
					System.out.println("\nHere are the books that have a quantity of or below your entry:");
					resultSetPrinter(rset); //ResultSet sent to resultSetPrinter to show results
				} else if(selection == 5) { //Returns to the main selection menu
					System.out.println("Returning to main menu.\n");
				} else {
					System.out.println("Sorry, that isn't a valid selection.");
				}
			}
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}

	public static void resultSetPrinter(ResultSet rset) {
		try {
			if(rset.next()) {
				while(rset.next()) {
					int id = rset.getInt("id");
					String title = rset.getString("Title");
					String author = rset.getString("Author");
					int qty = rset.getInt("Qty");
					System.out.println("ID: " + id + "\nTitle: " + title + "\nAuthor: " + author + "\nNumber in stock: " + qty + "\n");
				}
			} else {
				System.out.println("No records for the entry could be found.\n");
			}
		} catch(SQLException ex) {
			ex.printStackTrace();
		}
	}
}
