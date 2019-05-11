public class Logic<k> {
    public int logic(String line) {
        line.replaceAll( "\\s+",  "");
        return line.length();
    }

    public int ALLSUM(int n) {
        int k = 0;
        for (int i = 1; i <=n; i = i + 1) {
            String line = Trans.trans(i);
            k = k + this.logic(line);
        }
        return k;
    }
}
