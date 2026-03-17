import java.util.Scanner;

class fibonacci
  {
    public static void main(String[] args)
    {
       Scanner sc = new Scanner(System.in);
      int num;
       System.out.println("\n---------------FIBONACCI SERIES------------------");
      System.out.print("Enter a Number: ");
      num = sc.nextInt();

      int a = 0;
      int b = 1;
      int next;

      System.out.println("\n-------------------------------------------------");

      for(int i = 0; i <= num; i++)
        {
          System.out.print(" " + a + " ");
          next = a + b;
          a = b;
          b = next;
          
        }
      System.out.println();

    }
 
  }
