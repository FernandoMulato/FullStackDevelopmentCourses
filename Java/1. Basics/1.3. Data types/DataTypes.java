import java.util.ArrayList;

public class DataTypes {
  public static void main(String[] args) {
    // In java you declare a variable like this:
    /*
    BASIC FORM. 
    DataType dataName;. 
    
    MULTIPLE DECLARATION FORM. 
    DataType data1, data2, data3;

    FORM DECLARE AND INITIALIZE. 
    DataType data1 = value; 
    DataType data2 = value2, data3 = value3;
    */

    // Primitive data types

    /**  
    * Type: integer
    * Occupies: 1 byte
    * Range: -128 to 127
    */
    byte varByte;

    /**  
    * Type: integer
    * Occupies: 2 byte
    * Range: -32768 to 32767
    */
    short varShort;

    /**  
    * Type: integer
    * Occupies: 4 byte
    * Range: 2*109
    */
    int varInt;
    
    /**  
    * Type: integer
    * Occupies: 8 byte
    * Range: Very long
    */
    long varLong;

    /**  
    * Type: Simple decimal
    * Occupies: 4 byte
    * Range: Very long
    */
    float varFloat;

    /**  
    * Type: Double decimal
    * Occupies: 8 byte
    * Range: Very long
    */
    double varDouble;

    /**  
    * Type: Character. 
    * Use single quotes
    * Occupies: 2 byte
    * Range: Very long
    */
    char varChar;
    
    /**  
    * Type: value: true or false. 
    * Occupies: 1 byte
    */
    boolean varBoolean;

    // Object types

    // Java standard library types
    /**  
    * Type: text strings
    */
    String objString;
    /**
     *  Many others (e.g. Scanner, TreeSet,
     *  ArrayList…)
    */ 
  
    /**
     * Types of wrapper (Equivalent to 
     * primitive types but as objects...)
    */
    Byte objByte;
    Short objShort;
    Character objChar;
    Integer objInt;
    Long objLong;
    Float objFloat;
    Double objDouble;
    Boolean objBoolean;

    // Variable assignment
    varByte = 127;
    varDouble = 199.99;
    objString = "This is a text";
    
    // Variable reading
    System.out.println(objString);

    // Local-Variable Type Inference
    var myVarString = "A string";
    var myVarInt = 12;
  }
}
