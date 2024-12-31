
# include <stdio.h>
# include <stdlib.h>

# define GRADMAX 20

typedef struct _Rx_{
  int g;
  double c[GRADMAX+1];
}Rx;

Rx leeP(void)
{
  Rx ret;
  int i;

  printf("digite el grado:");
  scanf("%d", &(ret.g));
  for (i=0; i<=ret.g; i++){
    printf("digite el coeficiente del monomio x^%d:", i);
    scanf("%lf", &(ret.c[i]));
  }
  
  while(ret.g>=0 && ret.c[ret.g]==0.0) ret.g--;

  return ret;
}

int escP(Rx C)
{
  int i;

  if (C.g<0) printf("0");
  else {
  	if(C.g>1){
  	if(C.c[C.g]==1.0||C.c[C.g]==-1.0)
  		printf("%s^%d", C.c[C.g]==1.0?"x":"-x", C.g);
  	else 
	  printf("%lgx^%d ", C.c[C.g], C.g);	
	}
  	
    
	for (i=C.g-1; i>1; i--)
      if (C.c[i]!=0.0)
	  	if(C.c[i]==1.0||C.c[i]==-1.0) 
		  printf("%s^%d", C.c[i]==1.0?"+x":"-x", i);
	  	else 
		  printf("%+lgx^%d ", C.c[i], i);
    
    if(C.g==1)
    	if(C.c[1]==1.0||C.c[1]==-1.0) 
		  printf("%s", C.c[1]==1.0?"x":"-x");
		else
		printf("%lgx ", C.c[1]);
	else
	
		if (C.g>=1 && C.c[1]!=0.0) 
			if(C.c[1]==1.0||C.c[1]==-1.0) 
		  	printf("%s", C.c[1]==1.0?"+x":"-x");
			else
			printf("%+lg x ", C.c[1]);
	
	if(C.g==0)printf("%lg ", C.c[0]);
	else
    	if (C.c[0]!=0.0) printf("%+lg ", C.c[0]);
  }
    return 0;
}

Rx prodP(Rx A, Rx B)
{
  int i, j;
  Rx C;

  C.g = A.g + B.g;
  for(i=0; i<=C.g; i++)
  	C.c[i] = 0.0;
  
  for(i=0; i<=A.g; i++)
  	for(j=0; j<=B.g; j++)
  		C.c[i+j] += A.c[i]*B.c[j];
  
  while(C.g>=0 && C.c[C.g]==0.0) C.g--;

  return C;
}

Rx polinomioInterpolante();

int main(int argc, char *argv[])
{
  Rx a, b, q;

  printf("Por leer los polinomios.\n");
  a=leeP();
  b=leeP();
  
  printf("Los polinomios son:\na = ");
  escP(a);
  printf("\nb = ");
  escP(b);
  
  q = prodP(a, b);
  printf("\nEl producto es: \n");
  escP(q);

  printf("\n\nFin del programa\n");

  system("pause");
  return 0;
}
