import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;

// program to implement Linked List

public class Demo {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<String>();
        add(linkedList,"Sydney");
        add(linkedList,"Melbourne");
        add(linkedList,"Adelaide");
        add(linkedList,"Darwin");
        add(linkedList,"Cairns");
        add(linkedList,"Canberra");
        add(linkedList,"Darwin");

        printPlacesToVisit(linkedList);
    }

    private static void printPlacesToVisit(LinkedList<String> linkedList) {
        Iterator<String> i = linkedList.iterator();
        while (i.hasNext())
            System.out.println("Now visiting " + i.next());
        System.out.println("==============");
    }

    private static boolean add(LinkedList<String> linkedList, String newCity) {
        ListIterator<String> stringListIterator = linkedList.listIterator();
        while (stringListIterator.hasNext()) {
            int comparison = stringListIterator.next().compareTo(newCity);
            if (comparison == 0) {
                System.out.println(newCity + " already in list");
                return false;
            } else if (comparison > 0) {
                stringListIterator.previous();
                stringListIterator.add(newCity);
                return true;
            } else if (comparison < 0) {

            }
        }

        stringListIterator.add(newCity);
        return true;
    }
}

