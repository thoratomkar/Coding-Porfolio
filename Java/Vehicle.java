// class for implementing vehicle

public class Vehicle
{
    private int currentDirection, currentSpeed;
    private String name, size;

    public int getCurrentDirection() {
        return currentDirection;
    }

    public int getCurrentSpeed() {
        return currentSpeed;
    }

    public String getName() {
        return name;
    }

    public String getSize() {
        return size;
    }

    public Vehicle(String name, String size) {
        this.name = name;
        this.size = size;
        this.currentDirection=0;

        this.currentSpeed=0;
    }
    public void steer(int direction)
    {
        this.currentDirection+=direction;
        System.out.println("Vehicle.steer() called.Steering at "+currentDirection+"degrees");

    }
    public void move(int speed,int direction)
    {
        currentDirection=direction;
        currentSpeed=speed;
        System.out.println("Vehicle.move() called Moving at "+currentSpeed+"in direction"+currentDirection);
    }
    public void stop()
    {
        this.currentSpeed=0;
    }


}


