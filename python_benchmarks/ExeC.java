import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.PrintWriter;
import java.io.OutputStreamWriter;

public class ExeC{
    public static void main(String args[]){
        try{

            ProcessBuilder builder = new ProcessBuilder("./read2.py");
            builder.redirectErrorStream(true);
            Process p = builder.start();
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
            PrintWriter stdOut = new PrintWriter(new OutputStreamWriter(p.getOutputStream()));

            String s=null;
            for(int i=0;i<12;i++){
                stdOut.println("bedri"+i);
                stdOut.flush();
                s = stdInput.readLine();
		if(s.length()!=0){
		    System.out.println("CPROCESS:"+s);
		}
            }

            stdOut.close();
            stdInput.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
}




