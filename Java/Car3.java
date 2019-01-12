 class CarBase {
    int wheels,no_cylinders;
    String name;
    boolean engine;

    public CarBase( int no_cylinders, String name) {
        this.wheels = 4;
        this.no_cylinders = no_cylinders;
        this.name = name;
        this.engine = true;
    }


    public int getNo_cylinders() {
        return no_cylinders;
    }

    public String getname() {
        return name;
    }



    public String startEngine()
    {
        return "Car -- startEngine()";
    }
     public String accelerate()
     {
         return "Car -- accelerate()";
     }
     public String brake()
     {
         return "Car -- brake()";
     }



}

class I10 extends CarBase
{

    public I10(int no_cylinders, String name) {
        super(no_cylinders, name);
    }

    @Override
    public String startEngine() {
        return "I10 -- startEngine()";
    }

    @Override
    public String accelerate() {
        return "I10 -- accelerate()";
    }

    @Override
    public String brake() {
        return "I10 -- brake()";
    }
}

class Suzuki extends CarBase
{

    public Suzuki(int no_cylinders, String name) {
        super(no_cylinders, name);
    }
    @Override
    public String startEngine() {
        return "Suzuki -- startEngine()";
    }

    @Override
    public String accelerate() {
        return "Suzuki -- accelerate()";
    }

    @Override
    public String brake() {
        return "Suzuki -- brake()";
    }

}

class Maruti extends CarBase
{

    public Maruti(int no_cylinders, String name) {
        super(no_cylinders, name);
    }
    @Override
    public String startEngine() {
        return "Maruti -- startEngine()";
    }

    @Override
    public String accelerate() {
        return "Maruti -- accelerate()";
    }

    @Override
    public String brake() {
        return "Maruti -- brake()";
    }

}


class Car3
{
    public static void main(String[] args) {


        I10 i10=new I10(6,"I10 v");
        System.out.println(i10.startEngine());
        System.out.println(i10.accelerate());
        System.out.println(i10.brake());

        Maruti maruti=new Maruti(6," Dzire");
        System.out.println(maruti.startEngine());
        System.out.println(maruti.accelerate());
        System.out.println(maruti.brake());

    }
}