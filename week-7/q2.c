#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
int i=0,top=0;
char stack[20],ip[20];

void push(char c)
{
	if (top>=20)
		printf("Stack Overflow");
	else
		stack[top++]=c;
}

void pop(void)
{
	if(top<0)
		printf("Stack underflow");
	else
		top--;
}

void error(void)
{
    printf("\n\nSyntax Error!!! String is invalid\n");
    getch();
    exit(0);
}

int main()
{
    int n;
    
    printf("The given grammar is\n\n");
    printf("E -> TC\n");
    printf("C -> +TC | epsilon\n");
    printf("T -> FD\n");
    printf("D -> *FD | epsilon\n");
    printf("F -> (E) | d\n\n");
    printf("Enter the string to be parsed:\n");
    scanf("%s",ip);
    n=strlen(ip);
    ip[n]='$';
    ip[n+1]='\0';
    push('$');
    push('E');
    printf("\ninput\t\taction\n");
    while(ip[i]!='\0')
    { 
        if(ip[i]=='$' && stack[top-1]=='$')
        {
            printf("\n\n Successful parsing of string \n");
            return(1);
            
        }
        else if(ip[i]==stack[top-1])
    	{
    	    printf("match of %c occured ",ip[i]);
    	    i++;
    	    pop();
    	}
    	else
    	{
    		if(stack[top-1]=='E' && ip[i]=='d')
    		{
    		    printf("\nE ->TC\t\t");
    		    pop();
    		    push('C');
    		    push('T');
    		}
    		else if(stack[top-1]=='E' && ip[i]=='(')
    		{
    		    printf("\nE ->TC\t\t");
    			pop();
    			push('C');
    			push('T');
    		}
    		else if(stack[top-1]=='C' && ip[i]=='+')
    		{
    		    printf("\nC -> +TC\t");
    		    pop();
    		    push('C');
    		    push('T');
    		    push('+');
    		}
    		else if(stack[top-1]=='C' && ip[i]==')')
    		{
    		    printf("\nC -> epsilon\t");
    		    pop();
    		}
    		else if(stack[top-1]=='C' && ip[i]=='$')
    		{
    		    printf("\nC -> epsilon\t");
    		    pop();
    		}
    		else if(stack[top-1]=='T' && ip[i]=='d')
    		{
    		    printf("\nT ->FD\t\t");
    		    pop();
    		    push('D');
    		    push('F');
    		}
    		else if(stack[top-1]=='T' && ip[i]=='(')
    		{
    		    printf("\nT ->FD\t\t");
    			pop();
    			push('D');
    			push('F');
    		}
    		else if(stack[top-1]=='D' && ip[i]=='+')
    		{
    		    printf("\nD -> epsilon\t");
    		    pop();
    		}
    		else if(stack[top-1]=='D' && ip[i]=='*')
    		{
    		    printf("\nD -> *FD\t");
    		    pop();
    		    push('D');
    		    push('F');
    		    push('*');
    		}
    		else if(stack[top-1]=='D' && ip[i]==')')
    		{
    		    printf("\nD -> epsilon\t");
    		    pop();
    		}
    		else if(stack[top-1]=='D' && ip[i]=='$')
    		{
    		    printf("\nD -> epsilon\t");
    		    pop();
    		}
    		else if(stack[top-1]=='F' && ip[i]=='d')
    		{
    		    printf("\nF -> d\t\t");
    		    pop();
    		    push('d');
    		}
    		else if(stack[top-1]=='F' && ip[i]=='(')
    		{
    		    printf("\nF -> (E)\t");
    		    pop();
    		    push(')');
    		    push('E');
    		    push('(');
    		}
    		else
    		{
    		    error();
    		}
    	}
     }
}