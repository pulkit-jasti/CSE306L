/*C program for lexical analyser:
Keywords:
Identifier:
Number : Integers
Relational Operators: <, <=, >, >=, ==, !=
Multi line Comments:
*/
#include <stdio.h>
#include <ctype.h>
#include <string.h>
char keyword[24][30] = {"int", "while", "break", "for", "do", "if", "float", "char", "switch", "double", "short", "long", "unsigned", "sizeof", "else", "register", "extern", "static", "auto", "case", "break", "volatile", "enum", "typedef"};
char symb_tab[100][100];
int check_keyword(char s[])
{
    for (int i = 0; i < 24; ++i)
        if (strcmp(s, keyword[i]) == 0)
            return 1;
    return 0;
}
void store_symb_tab(char id[], char symb_tab[][100]) //helps to remove duplicates
{
    int i;
    for (i = 0; strcmp(symb_tab[i], "") && i < 100; ++i)
        if (!strcmp(symb_tab[i], id))
            return;
    strcpy(symb_tab[i], id); //adds id to symb_tab
}

int main()
{
    FILE *fp1, *fp2;
    char c, id[30], num[10];
    int state = 0, i = 0, j = 0;
    fp1 = fopen("input.txt", "r");
    fp2 = fopen("output.txt", "w");
    while ((c = fgetc(fp1)) != EOF)
    {
        switch (state)
        {
        case 0:
            if (isalpha(c) || c == '_')
            {
                state = 1;
                id[i++] = c;
            }
            else if (isdigit(c))
            {
                state = 3;
                num[j++] = c;
            }
            else if (c == '<' || c == '>')
            {
                state = 5;
            }
            else if (c == '=' || c == '!')
            {
                state = 8;
            }
            else if (c == '/')
            {
                state = 10;
            }
            else if (c == ' ' || c == '\t' || c == '\n' || c == '\r')
            {
                state = 0;
            }
            else
            {
                fprintf(fp2, "\n%c", c);
            }
            break;
        case 1:
            if (isalnum(c) || c == '_')
            {
                state = 1;
                id[i++] = c;
            }
            else
            {
                id[i] = '\0';
                if (check_keyword(id))
                {
                    fprintf(fp2, " \n%s : keyword ", id);
                }
                else
                {
                    store_symb_tab(id, symb_tab);
                    fprintf(fp2, "\n%s : identifier", id); // calling the function which stores id in symbol table
                }
                state = 0;
                i = 0;
                ungetc(c, fp1);
            }
            break;
        case 3:
            if (isdigit(c))
            {
                num[j++] = c;
                state = 3;
            }
            else
            {
                num[j] = '\0';
                fprintf(fp2, " \n%s: number", num);
                state = 0;
                j = 0;
                ungetc(c, fp1);
            }
            break;
        case 5:
            if (c == '=')
            {
                fseek(fp1, -2, SEEK_CUR);
                c = fgetc(fp1);
                if (c == '<')
                {
                    fprintf(fp2, "\n<=: relational operator Less Than or Equal To");
                }
                else
                {
                    fprintf(fp2, "\n<=: relational operator Greater Than or Equal To");
                }
                c = fgetc(fp1);
                state = 0;
            }
            else
            {
                fseek(fp1, -2, SEEK_CUR);
                c = fgetc(fp1);
                if (c == '<')
                {
                    fprintf(fp2, "\n<: relational operator Less Than");
                }
                else
                {
                    fprintf(fp2, "\n>: relational operator Greater Than");
                }
                state = 0;
            }
            break;
        case 8:
            if (c == '=')
            {
                fseek(fp1, -2, SEEK_CUR);
                c = fgetc(fp1);
                if (c == '=')
                {
                    fprintf(fp2, "\n==: relational operator Equal To");
                }
                else
                {
                    fprintf(fp2, "\n!=: relational operator Not Equal To");
                }
                c = fgetc(fp1);
                state = 0;
            }
            else
            {
                fprintf(fp2, "\n!");
                ungetc(c, fp1);
                state = 0;
            }
            break;
        case 10:
            if (c == '*')
            {
                state = 11;
            }
            else
            {
                fprintf(fp2, "\n/%c: invalid lexeme", c);
                state = 0;
            }
            break;
        case 11:
            if (c == '*')
            {
                state = 12;
            }
            break;
        case 12:
            if (c == '*')
            {
                state = 12;
            }
            else if (c == '/')
            {
                state = 0;
            }
            else
            {
                state = 11;
            }
            break;
        }
    }
    if (state == 11)
    {
        fprintf(fp2, "\nComment Not Closed");
    }
    fprintf(fp2, "\n\n\nIdentifiers in the given text file are as follows\n");
    fprintf(fp2, "S.No - Identifier\n");
    for (int i = 0; strcmp(symb_tab[i], "") && i < 20; ++i)
        fprintf(fp2, "%d - %s\n", i + 1, symb_tab[i]);
    fclose(fp1);
    fclose(fp2);
    return 0;
}