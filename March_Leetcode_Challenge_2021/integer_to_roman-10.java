class Solution {
    public String intToRoman(int num) {
        String thousands[] = {"", "M", "MM", "MMM"};
        String hundreds[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String tens[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String ones[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        
        int thousand_place = num/1000;
        int hundred_place = (num % 1000) / 100;
        int ten_place = (num % 100) / 10;
        int one_place = (num % 10) / 1;
        
        return thousands[thousand_place] + hundreds[hundred_place] + tens[ten_place] + ones[one_place];
    }
}
