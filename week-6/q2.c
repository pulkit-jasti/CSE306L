#include<stdio.h>
#include<string.h>
int S(),Ldash(),L();
char *ip;
char string[50];
int main()
{
    printf("Enter the string\n");
    scanf("%s",string);
    ip=string;
    printf("\n\nInput\t\tAction\n");
    if(S() && *ip=='\0')
    {
        printf("\n String is successfully parsed\n");
    }
    else
    {
        printf("Error in parsing String\n");
    }
}
int S()
{
    if(*ip=='(')
    {
        printf("%s\t\tS->(L) \n",ip);
        ip++;
        if(L())
        {
            if(*ip==')')
            {
                ip++;
                return 1;
            }
            else
            {
                return 0;
            }
        }
        else
        {
            return 0;   
        }
    }
    else if(*ip=='a')
    {
        ip++;
        printf("%s\t\tS->a \n",ip);
        return 1;
    }
    else
    {
        return 0;   
    }
}
int L()
{
    printf("%s\t\tL->SL' \n",ip);
    if(S())
    {
        if(Ldash())
        {
            return 1;
        }
        else
        {
            return 0;   
        }
    }
    else
    {
        return 0;   
    }
}
int Ldash()
{
    if(*ip==',')
    {
        printf("%s\t\tL'->,SL' \n",ip);
        ip++;
        if(S())
        {
            if(Ldash())
            {
                return 1;
            }
            else
            {
                return 0;   
            }
        }
        else
        {
            return 0;   
        }
    }
    else
    {
        printf("%s\t\tL'->^ \n",ip);
        return 1;
    }
}
