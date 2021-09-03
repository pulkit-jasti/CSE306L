id [a-zA-Z][a-zA-Z0-9]*
numbers [+-]?[0-9]+
unsignednumber [0-9]*
decimals [+-]?[0-9]+(\.[0-9])?(\E[+-]?[0-9])?

%{
#include<stdio.h>
#include<string.h>
int n=0,flag=0,i=0,com=0,scom=0,count=0;
char symbol_table[30][30];
%}

%%
\n {scom=0;count++;}
"//" {scom=1;fprintf(yyout," \n single line comment\n\n");}
"/*" {com=1;fprintf(yyout," \n comment start\n");}
"*/" {com=0;fprintf(yyout," \n comment end\n");}
"<=" {if(!com&&!scom) fprintf(yyout," \n %s is a relational operator less than or equal to",yytext);}
"<" {if(!com&&!scom) fprintf(yyout," \n %s is a relational operator less than",yytext);}
">=" {if(!com&&!scom) fprintf(yyout," \n %s is a relational operator greater than or equal to",yytext);}
">" {if(!com&&!scom) fprintf(yyout," \n %s is a relational operator greater than",yytext);}
"==" {if(!com&&!scom) fprintf(yyout," \n %s is a relational operator equal to",yytext);}
"!=" {if(!com&&!scom) fprintf(yyout," \n %s is a relational operator not equal to",yytext);}
"=" {if(!com&&!scom) fprintf(yyout," \n %s is assignment opertor",yytext);}
auto | double | int | struct | break | else | long | switch | case | enum | register | typedef | char | extern | return | union | continue | for | signed | void | do | if | static | while | default | goto | sizeof | volatile | const | float | short {if(!com&&!scom) fprintf(yyout," \n %s is a keyword",yytext);}
{id} {if(!com&&!scom) fprintf(yyout," \n %s is an identifier",yytext);
                         if(!com&&!scom){
                         for(i=0;i<n;i++){
			 if (strcmp(symbol_table[i], yytext) == 0){
			 flag = 1;
			 break;}}
			 if (flag == 0){
			 strcpy(symbol_table[n++], yytext);}
			 flag = 0;}
                     }
{unsignednumber} {if(!com&&!scom) fprintf(yyout," \n %s is an Unsigned integer",yytext);}
{numbers} {if(!com&&!scom) fprintf(yyout," \n %s is an integer",yytext);}
{decimals} {if(!com&&!scom) fprintf(yyout," \n %s is a floating point number",yytext);}
.
%%

int main()
{
	yyin =fopen("input.txt","r");
	yyout=fopen("output.txt","w");
	yylex();
	printf("\n the contents of symbol table are :\n");
	for(i=0;i<n;i++)
	{
	    printf("\n %s",symbol_table[i]);
	}
	printf("\n no of identifiers in the symbol table = %d",n);
	printf(" \n no of lines in the input file = %d\n\n",count);
	return 0;
}

int yywrap()
{
return 1;
}
