// program to implement while and do while

public class While_Do_while
{

    public static void main(String []args)
    {
        int count=0;
      for(int i=5;i<=20;i++)
      {
          boolean x;
          x = isEvenNumber(i);

          if (x)
          {
              if (count == 5)
              {
                  break;
              }
              count++;
              System.out.println(i + " is even");
          }
      }
        System.out.println("Total no of even nos is "+count);
    }
    public static boolean isEvenNumber(int n)
    {

        if(n%2==1)
        {
            return false;
        }
        return true;
    }

}
