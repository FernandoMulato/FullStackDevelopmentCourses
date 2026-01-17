public class StringAndMethods {
  public static void main(String[] args) {
    // Creating a String
    String myString = new String("Hello world");

    System.out.println(myString);

    // Java String Literals 
    // Java has a shorter way of creating a new string
    String myString2 = "Hello world!";

    System.out.println(myString2);


    // Escape Characters
    /**
     *     Esc. Char      Description
     *         \\      Translated into a single \ character in the String
     *         \t      Translated into a single tab character in the string
     *         \r      Translated into a single carriage return character in the string
     *         \n      Translated into a single new line character in the string
    */
  
    String varText = "\tThis text is one tab in. \r\n";

    System.out.println(varText);

    // Java Text Blocks
    String textBlock = """
          This is a text inside a
          text block.
          You can use "quotes" in here
          without escaping them.
        """;

    System.out.println(textBlock);

    // Concatenating String
    String one = "Hello";
    String two = " World";

    String three = one + " " + two;

    System.out.println(three);

    // String Concatenation Performance
    /**
     * When concatenating Strings you have to watch 
     * out for possible performance problems. 
     * Concatenating two Strings in Java will be 
     * translated by the Java compiler to something 
     * like this:
    */
    three = new StringBuilder(one)
    .append(two).toString();

    /**
     * As you can see, a new StringBuilder is created, 
     * passing along the first String to its constructor, 
     * and the second String to its append() method, 
     * before finally calling the toString() method. This 
     * code actually creates two objects: A StringBuilder 
     * instance and a new String instance returned from 
     * the toString() method.
    */

    /**
     * When executed by itself as a single statement, 
     * this extra object creation overhead is insignificant. 
     * When executed inside a loop, however, it is a 
     * different story.
     * 
     * Here is a loop containing the above type of String
     *  concatenation:
     */ 
    String[] strings = 
      new String[]{"one", "two", "three", "four", "five"};

    String result = null;
    for(String string : strings) {
      result = result + string;
    }

    // This code will be compiled into something similar to this:
    result = null;
    for(String string : strings) {
      result = new StringBuilder(result)
                    .append(string).toString();
    }

    /**
     * The fastest way of concatenating Strings is
     * to create a StringBuilder once, and reuse 
     * the same instance inside the loop. 
     * Here is how that looks:
    */
    result = null;
    StringBuilder temp  = new StringBuilder();
    for(String string : strings) {
      temp.append(string);
    }
    result = temp.toString();

    // String Length
    int length = myString.length();
    System.out.println(length);  

    // Substrings
    /**
     * You can extract a part of a String. This is
     * called a substring. You do so using the substring() 
     * method of the String class. Here is an
     *  example:
    */
    String subString = myString.substring(0,5);

    System.out.println(subString);

    // Searching in String With indexOf()
    /**
     * You can search for substrings in Strings 
     * using the indexOf() method. Here is an 
     * example:
    */
    int index = myString.indexOf("world");

    System.out.println(index);

    /**
     * There is a version of the indexOf() method 
     * that takes an index from which the search is 
     * to start. That way you can search through a 
     * string to find more than one occurrence of a 
     * substring. Here is an example:
    */
    String theString = "is this good or is this bad?";
    String substring = "is";

    int i = theString.indexOf(substring);
    while(i != -1) {
      System.out.println(i);
      i = theString.indexOf(substring, i + 1);
    } 

    /**
     * The Java String class also has a lastIndexOf(
     * ) method which finds the last occurrence of a 
     * substring. Here is an example:
    */
    i = theString.lastIndexOf(substring);
    System.out.println(i);

    // Matching a String Against a Regular
    // Expression With matches()
    /**
     * The Java String matches() method takes a 
     * regular expression as parameter, and returns 
     * true if the regular expression matches the 
     * string, and false if not.
    */
    String text = "one two three two one";

    boolean matches = text.matches(".*two.*");

    System.out.println(matches);

    // Comparing Strings
    /**
     * Java Strings also have a set of methods used 
     * to compare Strings. These methods are:
     * 
     * - equals()
     * - equalsIgnoreCase()
     * - startsWith()
     * - endsWith()
     * - compareTo()
    */

    /**
     *  equals()
     * 
     * The equals() method tests if two Strings are 
     * exactly equal to each other. If they are, the 
     * equals() method returns true. If not, it 
     * returns false. Here is an example:
    */ 

    one   = "abc";
    two   = "def";
    three = "abc";
    String varFour  = "ABC";

    System.out.println( one.equals(two) );
    System.out.println( one.equals(three) );
    System.out.println( one.equals(varFour) );

    /**
     * equalsIgnoreCase()
     * 
     * The String class also has a method called 
     * equalsIgnoreCase() which compares two strings 
     * but ignores the case of the characters. Thus, 
     * uppercase characters are considered to be 
     * equal to their lowercase equivalents.
    */

    System.out.println( one.equalsIgnoreCase(varFour));

    /**
     * startsWith() and endsWith()
     * 
     * The startsWith() and endsWith() methods check 
     * if the String starts with a certain 
     * substring. Here are a few examples:
    */

    one = "This is a good day to code";

    System.out.println( one.startsWith("This")    );
    System.out.println( one.startsWith("This", 5) );

    System.out.println( one.endsWith  ("code")    );
    System.out.println( one.endsWith  ("shower")  );

    /**
     * compareTo()
     * The compareTo() method compares the String to 
     * another String and returns an int telling 
     * whether this String is smaller, equal to or 
     * larger than the other String. If the String 
     * is earlier in sorting order than the other 
     * String, compareTo() returns a negative 
     * number. If the String is equal in sorting 
     * order to the other String, compareTo() 
     * returns 0. If the String is after the other 
     * String in sorting order, the compareTo() 
     * method returns a positive number.
    */

    one   = "abc";
    two   = "def";
    three = "abd";

    System.out.println( one.compareTo(two)   );
    System.out.println( one.compareTo(three) );
    
    // Trimming Strings With trim()
  }
}
