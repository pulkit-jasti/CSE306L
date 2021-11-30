%{
#include "Newone.tab.h"
%}
%%
[0-9]+ {yylval=atoi(yytext);
return NUMBER;
}
"else" {yylval=strdup(yytext);return ELSE;}
"print" {yylval=strdup(yytext);return PRINT;}
"while" {yylval=strdup(yytext);return WHILE;}
"for" {yylval=strdup(yytext);return FOR;}
"in" {yylval=strdup(yytext);return IN;}
"range" {yylval=strdup(yytext);return RANGE;}
"<" {yylval=strdup(yytext);return LT;}
">" {yylval=strdup(yytext);return GT;}
"="     {yylval = strdup(yytext);return ASSIGN;}
"if" {yylval = strdup(yytext);return IF;}
":" {yylval = strdup(yytext);return COLON;}
\n\t return INDENT;
[a-zA-Z0-9]+ {yylval=strdup(yytext);return ID;}
. return yytext[0];
%%