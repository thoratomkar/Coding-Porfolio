public class Car1 extends Vehicle {
    private int currentGear, wheels, gears, doors;
    private boolean isManuel;

    public Car1(String name, String size, int wheels, int gears, int doors, boolean isManuel) {
        super(name, size);
        this.currentGear = 1;
        this.wheels = wheels;
        this.gears = gears;
        this.doors = doors;
        this.isManuel = isManuel;
    }

    public void changeGear(int currentGear) {
        this.currentGear = currentGear;
        System.out.println("Car.setCurrentGear() changes to " + this.currentGear);
    }

    public void changeSpeed(int speed, int direction) {
        System.out.println("Car.move() called Moving at " + speed + "in direction " + direction);
        move(speed, direction);

    }


}
