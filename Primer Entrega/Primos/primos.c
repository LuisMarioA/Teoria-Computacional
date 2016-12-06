#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int random(int,int);
int elementos(int);
void generarPrimos(int [],int);
void guardarDecimales(int,int []);
int crearArchivo(void);
void convertirBinario(int [],int);
int leerModo(void);
int menu(int);
int opcionAutomatica(void);
int opcionManual(void);
int repetir(int);

int main(void){
	srand(time(NULL));
	int modo=leerModo();
	int limite=menu(modo);
	if(crearArchivo()!=0){
		printf("Error al crear archivo");
	}
	while(limite!=0){
		int noElementos=elementos(limite);
		int primos [noElementos];
		generarPrimos(primos,limite);
		guardarDecimales(noElementos,primos);
		convertirBinario(primos,noElementos);
		limite=repetir(modo);
		}
}

int repetir(int modo){
	int opc=0;
	int r=0;
	int invalido=0;
	if(modo==1){
		do{
		printf("Quieres que se repita? \n 1.Si \n 2. No \n");
		scanf("%d",&opc);
		if(opc<1||opc>2){
			printf("Opcion Invalida\n");
			invalido=1;
		}else{
			if(opc==1){
				printf("Has seleccionado que se repita\n");
				r=opcionManual();
				return r;
			}else{
				if(opc==2){
					printf("No repetir, Adios");
					return 0;
					}
				}
			}
		}while(invalido==1);
	}
	if(modo==2){
		printf("Quieres que se repita? \n 1.Si \n 2. No \n");
		opc=random(1,2);
		if(opc==1){
		printf("Has seleccionado que se repita\n");
		r=opcionAutomatica();
		return r;
		}
		if(opc==2){
			printf("No repetir, Adios");
			return 0;
		}
	}
}

int leerModo(void){
	int num=0;
	printf("PROGRAMA 1\n MENU DE OPCIONES:\n 1. Operacion Manual \n2.Operacion automatica\n3.Salir\n===>  \n");
	scanf("%d",&num);
	return num;
}

int menu(int modo){
	int limite=0;
	if(modo==1){
		limite=opcionManual();
	}
	if(modo==2){
		limite=opcionAutomatica();
	}
	if(modo==3){
		printf("Adios");
	}
	return limite;
}

int opcionAutomatica(void){
	int limite=0;
	printf("Opcion Automatica Seleccionada\n");
		printf("Indique el limite ===>  ");
		limite=random(1,1000);
		printf("\nEl limite seleccionado es %d \n",limite);
		return limite;
}

int opcionManual(void){
	int limite=0;
		printf("Opcion Manual Seleccionada\n");
		printf("Indique el limite ===>  ");
		scanf("%d",&limite);
		printf("\nEl limite seleccionado es %d \n",limite);
		return limite;
}

int elementos(int limite){
	int x=0;
	int i=0;
	int np=0;
	int elementos=0;
		for(x=2;x<=limite;x++){
			np=0;
			for(i=1;i<x;i++){
				if(x%i==0){
					np++;
				}
			}
			if(np==1){
				elementos++;
			}
		}
	return elementos+1;
}

void guardarDecimales(int nElementos, int primos []){
	FILE *fp;
	int x=0;
	fp=fopen("archivo.txt","a");
	fprintf(fp,"D={");
	for(x=0;x<nElementos;x++){
	fprintf(fp,"%d",primos[x]);
		if(x!=nElementos-1){
			fprintf(fp,",");
		}
	}
	fprintf(fp,"}");
}

void generarPrimos(int primos[],int limite){
	primos[0]=1;
	int i=0;
	int x=0;
	int np=0;
	int casilla=1;
	for(x=2;x<=limite;x++){
		np=0;
		for(i=1;i<x;i++){
			if(x%i==0){
			np++;
			}
		}
	if(np==1){
			primos[casilla]=x;
			casilla++;
		}
	}
}

void convertirBinario(int primos[],int nElem){
	FILE *fp;
	fp=fopen("archivo.txt","a");
	int res=0;
	int x=0;
	int i=0;
	int c=0;
	char aux[10];
	char cadena[10];
	fprintf(fp,"B={");
	for(c=0;c<nElem;c++){
		x=0;
		do{
		res=primos[c]%2;
		itoa(res,aux,10);
		cadena[x]=aux[0];
		primos[c]=primos[c]/2;
		x++;
		}while(primos[c]!=0);
			for(i=x-1;i>=0;i--){
			fprintf(fp,"%c",cadena[i]);
			}
				if(c<nElem-1){
				fprintf(fp,",");
				}
	}
	fprintf(fp,"}");
}

int crearArchivo(void){
	FILE *fp;
	fp=fopen("archivo.txt","w");
	fclose(fp);
	if(fp==NULL){
		return -1;
	}else{
		return 0;
	}
}

int random(int limite_inf,int limite_sup){
	int num=(rand()%limite_sup) + limite_inf;
	return num;
}
