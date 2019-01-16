class MinStack {

    public int t=-1;
    int a[]=new int[100];
    int n=a.length;

    /** initialize your data structure here. */
    public MinStack()
    {



    }

    public void push(int x)
    {
        if(t>n-1)
            System.out.println("OverFlow");
        else
            t++;
            a[t]=x;
            System.out.println(x+" pushed");

    }

    public void pop()
    {
        if(t>0)
        {
            System.out.println(a[t]+" popped from stack");
            t--;

        }
        else
        {
            System.out.println("Stack underflow");
        }


    }

    public int top()
    {

        return a[t];
    }

    public int getMin()
    {
        int min=a[0];
        for(int i=1;i<=t;i++)
            if(min>a[i])
                min=a[i];
        return min;
    }

    public void display()
    {
        for(int i=0;i<=t;i++)
            System.out.print(a[i]+" ");
    }

    public static void main(String[] args)
    {
        MinStack obj = new MinStack();
        obj.push(4);
        obj.push(5);
        obj.push(6);
        obj.push(7);
        obj.push(8);
        obj.pop();
        int param_3 = obj.top();
        System.out.println("Top is "+param_3);
        int param_4 = obj.getMin();
        System.out.println("Minimum is "+param_4);
        obj.display();
        int b=obj.top();
        System.out.println("Top is "+b);
    }
}
