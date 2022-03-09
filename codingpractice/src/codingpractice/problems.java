package codingpractice;
import java.lang.String;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.*;
import java.util.*;

public class problems {
	
	/*We'd probably reference a Database instead of an HashMap here, but we would still probably
	* use a separate data structure than our Database anyway.
	* HashMap over an ArrayList here since its a little faster than iterating over what might be
	* a massive amount of similar user accounts. 
	*/
	public static HashMap<String, Integer> IDs = new HashMap<String, Integer>();
	
	public static String createID(String str) {
		
		try {
			
			//There are names with only 2 chars, so we fill in the blanks for now rather than throw an error
			while (str.length() < 3) {
				str = str + "-";
			}
			String nameFormat = str.substring(0, 3);
			nameFormat = nameFormat.toUpperCase();
			
			String resultID = "";
				
			//If our Formatted Name exists in the HashMap, we'll just get the current ID number, 
			//add 5 then replace the nameFormat Key value with out new latest ID number.
			if ( IDs.containsKey(nameFormat) ) {
				
				int newID = (IDs.get(nameFormat) + 5); 
				IDs.replace(nameFormat, newID);
				
				resultID = String.format(nameFormat + "%03d", newID);
			} 
			//If our Formatted name hasn't been used yet, put it in the HashMap with the initial
			//ID number value of 5.
			else {
				IDs.put(nameFormat, 5);
				resultID = String.format(nameFormat + "%03d", 5);
			}
			
			//Check if our ID exceeds the 6 char limit
			if(resultID.length() > 6) {
				System.out.println("Exceeded Character Limit");
				return "error";
			}
			
			System.out.println(resultID);
			return resultID;
		}
		catch (Exception e){
			System.out.println("Something went wrong");
			e.printStackTrace();
			return "error";
		}
	}
	
	public static void readCSV() {
		
		String line = "";
		
		try {
		
			//Grab our filepath and open a reader.
			Path csvPath = FileSystems.getDefault().getPath("CsvExample.csv");
			BufferedReader csv = Files.newBufferedReader(csvPath.toAbsolutePath());
			
			//While we have new lines, use a Regex to ignore commas in quotations and split the string
			while(  (line = csv.readLine()) != null ) {
		        String[] tokens = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
		        
		        //Print each split token
		        for(String t : tokens) {
		            System.out.println("> "+t);
		        }
			}
			csv.close();
		}
		catch (IOException e){  
			System.out.println("Something went wrong");
			e.printStackTrace();
		}
		
	}
	
	public static void userMenu() {
		
		boolean exitMenu = false;
		String userInput = "";
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		try {
		
			/* Initial Menu Layout for giving users input.
			 * Could flesh out the menu a bit more to have more responsiveness for users (Refreshing the menu,
			 * Adding Success notifications, etc.) But the UI might be basic by design.
			 */
			System.out.print("Welcome to the Phone/SSN Formatter.\n"
					+ "Enter '1' to enter a Phone Number.\n"
					+ "Enter '2' to enter a SSN.\n"
					+ "Enter 'Q' to quit the program.\n");

			while (!exitMenu) {
				
				userInput = input.readLine();
				
				//Uppercase our string incase users lazily exit with a lowercase q.
				switch(userInput.toUpperCase()) {
					
					case "1":
						userInput = input.readLine();
						

						
						//While out user Input isn't a String of Exactly 10 digits, throw an error.
						while ( !userInput.matches("^\\d{10}$") ) {
							System.out.println("Error! Phone numbers should be 10 digits long and only numbers.");
							userInput = input.readLine();
						}
						
						//Construct the output from a three way split of user input
						String areaCode = userInput.substring(0,3);
						String midThree = userInput.substring(3,6);
						String lastFourP = userInput.substring(6,10);
						
						String formattedPhone = ("(" + areaCode + ")" + midThree + "-" + lastFourP);
						System.out.println(formattedPhone);
						break;
						
					case "2":
						userInput = input.readLine();
						
						//While our user Input isn't a String of Exactly 9 digits, throw an error
						String SSNRegex = "^\\d{9}$";
						while ( !userInput.matches(SSNRegex) ) {
							System.out.println("Error! SSN Numbers should only be 9 digits long and only numbers.");
							userInput = input.readLine();
						}
						
						//Again, constructing from a three way split string.
						String firstThree = userInput.substring(0,3);
						String midTwo = userInput.substring(3,5);
						String lastFourS = userInput.substring(5,9);
						
						String formattedSSN = (firstThree + "-" + midTwo + "-" + lastFourS);
						System.out.println(formattedSSN);
						break;
						
					case "Q":
						//Set our exit boolean to true to break the menu loop.
						
						System.out.println("Exiting");
						input.close();
						exitMenu = true;
						break;
						
					default:
						System.out.println("Error! Please enter a valid Menu option.");
						break;
				}
			}
		} catch (Exception e){
			System.out.println("Something went wrong.");
			e.printStackTrace();
		}
		
	}

	public static void main(String[] args) {
		
		createID("Jen");
		createID("Yi");
		createID("J");
		createID("Jen");
		createID("Tom");
		createID("Vito");
		createID("Jennifer");
		System.out.println("\n-----------------\n");
		
		readCSV();
		
		System.out.println("\n-----------------\n");
		
		userMenu();
	
		IDs.clear();
	}

}
