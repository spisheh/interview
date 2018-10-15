/*
Objective
In this challenge, we will learn some basic concepts of C that will get you started with the language.
You will need to use the same syntax to read input and write output in many C challenges.

Task:
This challenge requires you to print  on a single line, and then print the already provided input string to stdout.
Note: You do not need to read any input in this challenge.

Input Format:
You do not need to read any input in this challenge.

Output Format:
Print  on the first line, and the string from the given input on the second line.

Sample Input 0
Sam

Sample Output 0
Hello, World!
Welcome to C programming, Sam.
*/

#include <stdio.h>

int main() 
{
	char *buffer;
    size_t bufsize = 32;
    buffer = (char *)malloc(bufsize * sizeof(char));
    printf("What is your Name: ");
    getline(&buffer,&bufsize,stdin);
  	printf("Hello, World!\nWelcome to C programming, %s",buffer);
    free(buffer);
    return 0;
}