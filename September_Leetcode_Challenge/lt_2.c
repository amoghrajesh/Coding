#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int removeAlternateDigits(int n)
{
	char str[32];
	int temp, i;
	itoa(n, str, 10);

	temp = 0;
	for (i = 0; i < strlen(str); i = i + 2)
	{
		temp = temp * 10 + (str[i] - '0');
	}

	return temp;

}
int main()
{
	int n;
	scanf("%d", &n);

	n = removeAlternateDigits(n);

	printf(n);

}