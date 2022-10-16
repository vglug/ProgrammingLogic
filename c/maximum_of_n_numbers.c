#include<stdio.h>
void main(){
int n,i,arr[500],max=0;
printf("Enter total number of element you need to find max:");
scanf("%d",&n);
printf("Enter the value one by one\n");
for (i=0;i<n;i++)
{
scanf("%d",&arr[i]);
if(arr[i]>max)
{
max=arr[i];
}
}
printf("The maximum element you entered is %d\n",max);
}
