public class Car
{
    private int doors,wheels;
    private String model,engine,color;

    public void setModel(String model) {
        String validModel=model.toLowerCase();
        if(validModel.equals("carrera")) {
            this.model = model;
        }
            else {
            this.model = "Unknown";
        }
    }
    public String getModel() {
       return this.model;


    }
}
