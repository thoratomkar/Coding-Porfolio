
// small java program for printer status and ink level

public class Printer {

private int tonerLevel,pagesPrinted;
private boolean duplexPrinter;

    public Printer(int tonerLevel, boolean duplexPrinter) {
        if(tonerLevel>=1 && tonerLevel<=100) {
            this.tonerLevel = tonerLevel;
        }
        else{
            this.tonerLevel=-1;
        }
        this.duplexPrinter = duplexPrinter;
        this.pagesPrinted=0;

    }



    public int fillToner(int ink) {
        if (ink > 0 && ink <= 100) {
            if (this.tonerLevel <= 100)
            {
                this.tonerLevel += ink;
            }
            if (this.tonerLevel > 100)
            {
                this.tonerLevel = 100;
            }
            return this.tonerLevel;
        }
        else
            return -1;
    }

    public int getTonerLevel() {
        return tonerLevel;
    }

    public int printPage(int pages)
    {
        int pagesToPrint=pages;
        if(this.duplexPrinter){
            pagesToPrint=(pages/2)+(pages%2);
            System.out.println("Printing in duplex mode");
        }

        System.out.println("Page printed");
        this.pagesPrinted+=pagesToPrint;
        return pagesToPrint;
    }

    public int getPagesPrinted() {
        return pagesPrinted;
    }
}
