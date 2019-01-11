public class Queue
{
    int n=100;
    int a[]=new int[n];
    int front=-1;
    int rear=-1;
    public static void main(String[] args)
    {
        Queue q=new Queue();
        q.insert(5);
        q.insert(7);
        q.insert(9);
        q.insert(10);
        q.insert(2);
        q.insert(12);
        q.display();
        q.delete();
        q.delete();
        q.delete();
        q.display();
        q.destroy();

        q.normalDisplay();


    }

    public void insert(int data)
    {
        if(rear==n-1)
        {
            System.out.println("Queue full");
        }
        else
        {
            rear++;
            a[rear]=data;
            if(front==-1)
                front++;
        }
    }

    public void delete()
    {
        if(front==-1)
        {
            System.out.println("Queue underflow ie empty");
        }
        else
        {
            System.out.println("Element deleted "+a[front]);
            if(front==rear)
                front=rear=-1;
            else
                front++;

        }

    }

    public void display()
    {
        if(front==-1)
            System.out.println("Queue underflow");
        for(int i=front;i<=rear;i++)
        {
            System.out.print(a[i]+ " ");
        }
        System.out.println(" ");

    }

    public void destroy()
    {
        front=rear=-1;
    }

    public void normalDisplay()
    {
        for(int i=0;i<=n-1;i++)
            System.out.print(a[i] +" ");

    }
}

