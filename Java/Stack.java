
public class Stack
{
    final int n=10;
    int a[]=new int [n];
    int top;

    public static void main(String[] args)
    {
        Stack s=new Stack();
        s.push(5);
        s.push(6);
        s.push(7);
        s.pop();

    }

    Stack()
    {
        top=-1;
    }

    public void push(int data)
    {
        if(top>(n-1))
        {
            System.out.println("Stack full");
        }
        else
        {
            top++;
            a[top]=data;
            System.out.println(data+" pushed into stack");
        }
    }

    public void pop()
    {
        if(top<0)
        {
            System.out.println("Stack underflow");
        }
        else
        {
            System.out.println(a[top]+" popped from stack");
            a[top]=a[top--];

        }
    }

    public void display()
    {
        for(int i=0;i<=n-1;i++)
            System.out.println(a[i]);

    }

}
