public class Honda extends Car1
{
    private int roadServiceMonths;
    public Honda(int roadServiceMonths) {
        super("Honda","2WD" , 5, 6, 5, false);
        this.roadServiceMonths=roadServiceMonths;
    }
    public void accelerate(int rate)
    {
        int newSpeed=getCurrentSpeed()+rate;
        if(newSpeed==0) {
            stop();
            changeGear(1);
        }
        else if(newSpeed>0 && newSpeed<=10)
        {
            changeGear(1);
        }else if(newSpeed>10 && newSpeed<=20)
        {
            changeGear(2);
        }
        else if(newSpeed>20 && newSpeed<=30)
        {
            changeGear(3);
        }
        else{
            changeGear(4);
        }
        if(newSpeed>0)
        {
            changeSpeed(newSpeed,getCurrentDirection());

        }
    }

}

