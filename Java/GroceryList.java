import java.util.ArrayList;



class GroceryList
{
     ArrayList<String> groceryList=new ArrayList<String>();


     public void addgroceryItem(String item){
       groceryList.add(item);
     }

     public void printgroceryList(){
         System.out.println("You have "+groceryList.size() +" items in your grocery list");
         for(int i=0;i<groceryList.size();i++) {
             System.out.println((i + 1) + "." + groceryList.get(i));
         }
     }

     private void modifygroceryItem(int position,String newitem){
         groceryList.set(position,newitem);
     }

     public void modifygroceryItem(String currentItem,String newitem){
         int position=findItem(currentItem);
         if(position>=0)
             modifygroceryItem(position,newitem);
     }

     private void removegroceryItem(int position)
     {

         groceryList.remove(position);
     }

     public void removegroceryItem(String item){
         int position=findItem(item);
         if(position>=0)
             removegroceryItem(position);
     }

     public int findItem(String searchItem)
     {
         return groceryList.indexOf(searchItem);

     }

    public static void main(String[] args) {


         GroceryList g=new GroceryList();

         g.addgroceryItem("Milk");
         g.addgroceryItem("Cheese");
        g.addgroceryItem("Cheese");
        g.addgroceryItem("Cheese");
        g.addgroceryItem("Cheese");
        g.addgroceryItem("Cheese");
        g.addgroceryItem("Cheese");
         g.printgroceryList();
        System.out.println(g.findItem("Cheese"));
        g.modifygroceryItem("Cheese","Paneer");
        g.modifygroceryItem("Cheese","Paneer");
        g.modifygroceryItem("Cheese","Paneer");
        g.modifygroceryItem("Cheese","Paneer");
        g.removegroceryItem("Cheese");
        g.printgroceryList();





    }
}
