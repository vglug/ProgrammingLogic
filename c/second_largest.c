#include <stdio.h>
#include <limits.h> // For INT_MIN

#define MAX_SIZE 1000     // Maximum array size 

int main()
{
    int arr[MAX_SIZE], size, i;
    //variable max1 and max2
    int max1, max2;
    //enter size of the array
    printf("Enter size of the array (1-1000): ");
    scanf("%d", &size);
    
    //enter array elements
    printf("Enter elements in the array: ");
    for(i=0; i<size; i++)
    {
        scanf("%d", &arr[i]);
    }

    max1 = max2 = INT_MIN;
    
    //check for first largest and second largest
    for(i=0; i<size; i++)
    {
        if(arr[i] > max1)
        {
            /*
             * If current element of the array is first largest
             * then make current max as second max
             * and then max as current array element
             */
            max2 = max1;
            max1 = arr[i];
        }
        else if(arr[i] > max2 && arr[i] < max1)
        {
            max2 = arr[i];
            //if current element is lesser but greater than second element then make it second largest
        }
    }

  
    printf("Second largest = %d", max2);

    return 0;
}
