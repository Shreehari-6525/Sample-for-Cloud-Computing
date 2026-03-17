import java.util.*;

class factorial
  {
    public static void main(String[] args)
    {
      System.out.println("------------FACTORIAL PROGRAM----------");

      Scanner sc = new Scanner(System.in);
      System.out.print("Enter a number: ");
      int num;
      num = sc.nextInt();
      int fact = 1;

      for(int i = 1; i <= num; i++)
        {
          fact = fact * i;
        }
      System.out.println("---------------------------------------");
      System.out.println("Factorial of " + num + "is: " + fact);        
      
    }
  }
