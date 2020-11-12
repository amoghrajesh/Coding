# include <stdio.h>
# include <stdlib.h>
# include <math.h>
 
int MinimumSum(int arr[], int length)
{
    int count = 0;
    int l, r, min_sum, sum, min_l, min_r;
    if (length < 2)
    {
        return 0;
    }
    min_l = 0;
    min_r = 1;
    min_sum = arr[0] + arr[1];
    for (l = 0; l < length - 1; l++)
    {
        for (r = l + 1; r < length; r++)
        {
            sum = arr[l] + arr[r];
            if (abs(min_sum) > abs(sum))
            {
                min_sum = sum;
                min_l = l;
                min_r = r;
            }
        }
    }
    return min_sum;
}