public class TypeCasting {
  public static void main(String[] args) {
    // Converting Int to Double

    // 1. Create int type variable 
    int varInt = 50;
    System.out.println("The integer value: " + varInt);

    // 2. Convert into double type
    double varToDouble = varInt;

    System.out.println("The double value: " + varToDouble);

    // Converting Double into an Int
    
    // 1. Create double type variable
    double varDouble = 50.55;

    System.out.println("The double variable: " + varDouble);

    // 2. Convert into int type
    int varToInt = (int)varDouble;

    System.out.println("The integer value: " + varToInt);

    // Converting Int to String

    // 1. Create int type variable
    int varInt2 = 50;

    System.out.println("The integer values is: "  + varInt2);

    // 2. Convert int to string type
    String varToString = String.valueOf(varInt2);

    System.out.println("The string value is: " + varToString);

    // Convert String to Int

    // 1. Create string type variable
    String varString = "50";

    System.out.println("The string value is: " + varString);

    // 2. Convert string variable to int
    int varToInt2 = Integer.parseInt(varString);
    
    System.out.println("The integer value is: " + varToInt2);
  }

}
