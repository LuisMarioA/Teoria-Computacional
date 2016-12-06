#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>
#include <time.h>

int random(int,int);
void agregarCaracter(int,int,int,char[]);
int guardarPalabra(int);
void opcionAutomatica(void);
void opcionManual(void);
int crearArchivo(void);
int menu(void);
int repetir(int);


int main(void){
	int modo=0;
	int rep=0;
	srand(time(NULL));
	if(crearArchivo()==-1){
		printf("Error al crear el archivo");
	}
	modo=menu();
	if(modo==0){
		return 0;
	}
	do{
		rep=repetir(modo);
	}while(rep!=1);
	return 1;
}

int repetir(int modo){
	int opcion=0;
	if(modo==1){
		printf("Quieres que se repita? \n 1.Si \n 2. No \n");
		scanf("%d",&opcion);
		if(opcion==1){
			printf("Has seleccionado que se repita\n");
			opcionManual();
			return 0;
		}
		if(opcion==2){
			printf("No repetir, Adios");
			return 1;
		}
	}
	if(modo==2){
		printf("Quieres que se repita? \n 1.Si \n 2. No \n");
		opcion=random(1,2);
		if(opcion==1){
		printf("Has seleccionado que se repita\n");
		opcionAutomatica();
		return 0;
		}
		if(opcion==2){
			printf("No repetir, Adios");
			return 1;
		}
	}
}

int menu(void){
	int potencia=0;
	int opcion=0;
	printf("PROGRAMA 1\n MENU DE OPCIONES:\n 1. Operacion Manual \n2.Operacion automatica\n3.Salir\n===>  \n");
	scanf("%d",&opcion);
	if(opcion==1){
		opcionManual();
	}
	if(opcion==2){
		opcionAutomatica();
	}
	if(opcion==3){
		printf("Adios");
		return 0;
	}
	return opcion;
}

int crearArchivo(void){
	FILE * archivo;
	archivo=fopen("archivo.txt","w");
	fclose(archivo);
	if(archivo==NULL){
		return -1;
	}else{
		return 0;
	}
}

void opcionAutomatica(void){
	int potencia=0;
	printf("Opcion Automatica Seleccionada\n");
		printf("Indique la potencia a usar ===>  ");
		potencia=random(0,1000);
		printf("\nLa potencia seleccionada es %d \n",potencia);
		if(guardarPalabra(potencia)!=0){
			printf("Error con el archivo");
		}
}

void opcionManual(void){
	int potencia=0;
		printf("Opcion Manual Seleccionada\n");
		printf("Indique la potencia a usar ===>  ");
		scanf("%d",&potencia);
		printf("\nLa potencia seleccionada es %d \n",potencia);
		if(guardarPalabra(potencia)!=0){
			printf("Error con el archivo");
		}
}

void agregarCaracter(int potencia, int noPalabra,int casilla,char palabra []){
	int x=0;
	if(potencia==0){
			palabra[casilla]='e';
		}
	for(x=potencia;x>0;x--,casilla++){
		int rep=pow(2,x);
			if(x==1 && noPalabra%2==1){
				palabra[casilla]='0';
			}else{
				if(x==1 && noPalabra%2==0){
					palabra[casilla]='1';
				}else{
						if(noPalabra<=rep/2){
							palabra[casilla]='0';
						}else{
							palabra[casilla]='1';
							noPalabra=noPalabra-(rep/2);		
							}
					}
				}
	}
}

int guardarPalabra(int p){
	FILE * archivo;
	int i=0;
	int x=0;
	int potencia=0;
	for(potencia=0;potencia<=p;potencia++){
	int repeticiones=pow(2,potencia);
	int numeroPalabra=1;
	archivo=fopen("archivo.txt","a");
	fprintf(archivo,"A={");
	if(potencia==0){
		potencia++;
		char palabra [potencia];
		potencia--;
	for(i=0;i<repeticiones;i++){
		agregarCaracter(potencia,numeroPalabra,0,palabra);
			for(x=0;x<=potencia;x++){
				fprintf(archivo,"%c",palabra[x]);
			}
				if(i!=repeticiones-1){
				fprintf(archivo,",");
				}
				numeroPalabra++;
	}
	}else{
		char palabra[potencia];
		for(i=0;i<repeticiones;i++){
		agregarCaracter(potencia,numeroPalabra,0,palabra);
			for(x=0;x<potencia;x++){
				fprintf(archivo,"%c",palabra[x]);
			}
				if(i!=repeticiones-1){
				fprintf(archivo,",");
				}
				numeroPalabra++;
		}
	}
	fprintf(archivo,"}");
	fclose(archivo);
	}
	return 0;
}

int random(int limite_inf,int limite_sup){
	int num=(rand()%limite_sup) + limite_inf;
	return num;
}
