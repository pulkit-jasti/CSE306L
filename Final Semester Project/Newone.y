%{
#include<stdio.h>
#include <ctype.h>
%}
%token NUMBER LT GT ASSIGN IF ID PRINT COLON ELSE FOR IN RANGE WHILE INDENT
%left '-' '+' '*' '/' ','
%%
S: P {$$ = $1;printf("%s",$$);}
| A {$$ = $1;       if(isdigit($$))
                    {
                        printf("%d",$$);
                    }
                    else
                    {
                        printf("%s",$$);
                    };
}
| I {printf("\nCorrect Syntax for If-Else Statement");}
| W {printf("\nCorrect Syntax for While Loop");}
| F {printf("\nCorrect Syntax for for Loop");}
;
W: WHILE '(' ID LT NUMBER ')' COLON INDENT P {int i=0;
                                              while(i<$5)
                                              {
                                                  printf("%s\n",$9);
                                                  i=i+1;
                                              };
                                              }
| WHILE '(' ID GT NUMBER ')' COLON INDENT P {if($3 <= $5)
                                              {
                                                  break;
                                              }
                                              else
                                              {
                                                  while($3 > $5)
                                                  {
                                                      printf("%s\n",$9);
                                                  }
                                              };
                                              }
| WHILE '(' NUMBER GT NUMBER ')' COLON INDENT P {if($3 <= $5)
                                              {
                                                  break;
                                              }
                                              else
                                              {
                                                  while($3 > $5)
                                                  {
                                                      printf("%s\n",$9);
                                                  }
                                              };
                                              }
| WHILE '(' NUMBER LT NUMBER ')' COLON INDENT P {if($3 >= $5)
                                              {
                                                  break;
                                              }
                                              else
                                              {
                                                  while($3 < $5)
                                                  {
                                                      printf("%s\n",$9);
                                                  }
                                              };
                                              }
;
F : FOR ID IN RANGE '(' NUMBER ')' COLON INDENT P { int i = 0;
                                                    for(i =0; i<$6; i++)
                                                    {
                                                        printf("%s\n",$10);
                                                    }

;}
;
COMP: NUMBER GT NUMBER {if($1 > $3)
                        {
                            $$ = 1;
                        }
                        else
                        {
                            $$ = 0;
                        };}
| NUMBER LT NUMBER {if($1 < $3)
                        {
                            $$ = 1;
                        }
                        else
                        {
                            $$ = 0;
                        };}
;
I: IF '(' COMP ')'COLON INDENT P ELSE COLON INDENT P {if($3==1)
                                        {
                                            printf("%s",$7);
                                        }
                                        else
                                        {
                                            printf("%s",$11);
                                        }
                                       ;}
;
A: ID ASSIGN STRING {$$ = $3;}
| ID ASSIGN E {$$ = $3;}
| ID ASSIGN LIST {$$ = $3;}
| ID ASSIGN DICT {$$ = $3;}
;
DICT: '{' MATTER '}' {$$ = $2;}
; 
TUPLE: '(' MATTER ')' {$$ = $2;}
;
LIST: '[' MATTER ']' {$$ = $2;}
;
MATTER: NUMBER ',' MATTER {$$ = $1 , $3;}
| STRING ',' MATTER {$$ = $1 , $3;}
| LIST ',' MATTER {$$ = $1 , $3;}
| TUPLE ',' MATTER {$$ = $1 , $3;}
| DICT ',' MATTER {$$ = $1 , $3;}
| NUMBER COLON MATTER
| STRING COLON MATTER 
| LIST COLON MATTER 
| TUPLE COLON MATTER 
| DICT COLON MATTER
| NUMBER {$$ = $1;}
| STRING {$$ = $1;}
| LIST {$$ = $1;}
| TUPLE {$$ = $1;}
| DICT {$$ = $1;}
;
P: PRINT'('E')' {$$ = $3;printf("%s",$3);}
| PRINT'('STRING')' {$$ = $3;}
;
STRING: '"'ID'"' {$$ = $2;}
;
E: E '+' E { $$ = $1 + $3; }
| E '-' E { $$ = $1 - $3; }
| E '*' E { $$ = $1 * $3; }
| E '/' E { if($3 == 0)yyerror("Divide by zero");else$$ = $1 / $3; }
| '(' E ')' { $$ = $2; }
| NUMBER { $$ = $1; }
;
%%
int main(){
yyparse();
}
int yywrap(){
return 1;
}
void yyerror(char *s)
{
    printf("Error %s",s);
}