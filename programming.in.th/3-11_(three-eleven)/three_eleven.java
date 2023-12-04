    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;

    public class three_eleven {
        
        public static void main(String[] args) throws IOException {
            
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String input = reader.readLine();

            int n , mod_by_3 = 0 , mod_by_11 = 0;
            
            for (char digit : input.toCharArray())
            {
                n = digit - '0';
                mod_by_3= (mod_by_3 * 10 + n) % 3;
                mod_by_11 = (mod_by_11 * 10 + n) % 11;
            }

            System.out.println(String.format("%d %d",mod_by_3 , mod_by_11));
        
        }
        
    }


