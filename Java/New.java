import java.util.*;
import java.lang.*;

class Person {
    protected String firstName;
    protected String lastName;
    protected int idNumber;

    // Constructor
    Person(String firstName, String lastName, int identification)
    {
        this.firstName = firstName;
        this.lastName = lastName;
        this.idNumber = identification;
    }


    // Print person data
    public void printPerson(){
        System.out.println(
                "Name: " + lastName + ", " + firstName
                        + 	"\nID: " + idNumber);
    }

}
class Student extends Person{
    private int[] testScores;



    /*
     *   @param firstName - A string denoting the Person's first name.
     *   @param lastName - A string denoting the Person's last name.
     *   @param id - An integer denoting the Person's ID number.
     *   @param scores - An array of integers denoting the Person's test scores.
     */

    public Student(String firstName, String lastName, int identification, int[] testScores) {
        super(firstName, lastName, identification);
        this.testScores = testScores;

        n = testScores.length;
    }

    int j,score=0;
    char grade;
    private int n;

    public char calculate() {
        for (j = 0; j<n; j++)
        {
            score =score+ testScores[j];
        }
        score = score/j;
        if (score >= 90) {
            grade = 'O';
        } else if (score >= 80)
            grade = 'E';
        else if (score >= 70)
            grade = 'A';
        else if (score >= 55)
            grade = 'P';
        else if (score >= 40)
            grade = 'D';
        else
            grade = 'T';
        return grade;
    }
    }

class Solution3 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = scan.next();
        String lastName = scan.next();
        int id = scan.nextInt();
        int numScores = scan.nextInt();
        int[] testScores = new int[numScores];
        for(int i = 0; i < numScores; i++)
        {
            testScores[i] = scan.nextInt();
        }
        scan.close();

        Student s = new Student(firstName,lastName,id,testScores);
        s.printPerson();
        System.out.println("Grade: " + s.calculate() );
    }
}