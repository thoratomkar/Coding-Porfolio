
import java.util.LinkedList;

public class Song
{
    public static void main(String[] args) {

    }
    private String title;
    private double duration;

    public String getTitle() {
        return title;
    }

    public Song(String title, double duration) {
        this.title = title;
        this.duration = duration;
    }

    @Override
    public String toString() {
        return this.title+" : "+this.duration;
    }






}







