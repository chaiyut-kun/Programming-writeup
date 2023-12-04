package Grading;
import java.util.Scanner;

public class Grade{
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        String a = input.nextLine(),b = input.nextLine(),c =input.nextLine();
        int a_input = Integer.parseInt(a) , b_input = Integer.parseInt(b),c_input= Integer.parseInt(c);
        int sum =a_input+b_input+c_input;

        if (sum>=80){
            System.out.println("A");
        }
        else if (sum>=75){
            System.out.println("B+");
        }
        else if (sum>=70){
            System.out.println("B");
        }
        else if (sum>=65){
            System.out.println("C+");
        }
        else if (sum>=60){
            System.out.println("C");
        }
        else if (sum>=55){
            System.out.println(("D+"));
        }
        else if (sum>=50) {
            
            System.out.println("D");
        }
        else{
            System.out.println("F");
        }
        
    }
}