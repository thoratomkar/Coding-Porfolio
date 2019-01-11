import java.sql.SQLOutput;

public class BST
{
    BST left,right;
    int data;
    public BST(int data)
    {
        this.data=data;
    }

    public void insert(int value)
    {
        if(value <= data) {
            if (left == null)
                left = new BST(value);
            else
                left.insert(value);
        }
        else
        {
            if(right==null)
                right=new BST(value);
            else
                right.insert(value);
        }

    }

    public boolean contains(int value)
    {
        if(value==data)
        {
            return true;
        }
        else if(value< data) {
            if (left == null)
                return false;
            else
                return left.contains(value);
        }
        else
            if(right==null)
                return false;
            else
                return right.contains(value);
    }

    public void inOrder()
    {
     if(left!=null)
     {
         left.inOrder();
     }
     System.out.println(data);

     if(right!=null)
     {
         right.inOrder();
     }

    }


    public void preOrder()
    {
        System.out.println(data);
        if(left!=null)
        {
            left.preOrder();
        }


        if(right!=null)
        {
            right.preOrder();
        }

    }

    public void postOrder()
    {
        if(left!=null)
        {
            left.postOrder();
        }


        if(right!=null)
        {
            right.postOrder();
        }
        System.out.println(data);

    }



    public static void main(String[] args)
    {
        BST b=new BST(11);
        b.insert(5);
        b.insert(8);
        b.insert(15);
        b.insert(9);
        b.insert(10);
        //b.postOrder();
        System.out.println(b.contains(9));
    }
}


