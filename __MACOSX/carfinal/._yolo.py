using System;

public class Test
{
    public static string lovePalindromes(string str)
    {
       //this is default OUTPUT. You can change it. 
        string result= "-404";
        
        //write your Logic here:
    if(1<=str.length()<=100)
        {
             result=   str.substring(str.length()-1,str.length);
            string palindrom=result+str;
            string reverse=Array.Reverse(palindrom);
                if(!palindrom.equlas(reverse))
                        {
                            result='z';
                            }

            }
        return result;
    }
    public static void Main()
    {
        //INPUT [uncomment & modify if required]
        string str = Console.ReadLine();

        //OUTPUT [uncomment & modify if required]
        Console.WriteLine(lovePalindromes(str));
    }
}