// -------------------------------------------#
// _____Universidad de Costa Rica_____#
// __Escuela de Ingenieria Electrica___#
// __Laboratorio1: Introduccion a C_#

// Autor: Carlos Andres Cordero Retana B92317

// Descripcion del programa:

/* EL siguiente programa calcula el maximo 
comun divisor dado dos numeros enteros en la 
linea de comandos. Si se ingresan mas de 2 
argumentos o menos de 2, el programa imprime
en pantalla un mensaje de error. Asimismo, se
imprime un error cuando ambos numeros son 0 o
alguno de ellos es negativo. */

# include <stdio.h>
# include <stdlib.h> // Para emplear la funcion atoi
# include <string.h> // Dado que se trabajan con strings


int mcd(int x, int y){
    /* Funcion que calcula el MCD de dos numeros enteros x y y , 
    donde x>y.
    
    :param int x:  numero entero mayor.
    :param int y: numero entero menor.

    :return int x: valor del MCD de los 2 numeros ingresados.
    
     */

    if(y==0){
        return x;
    }else{
        int mod = x%y;
        mcd(y,mod);
    }
}



int main (int argc, char *argv[]) {

    int MCD;

    // Se verifica si la cantidad de argumentos es correcta
    if(argc == 3){

        // Se convierten a enteros
        int x = atoi(argv[1]);
        int y = atoi(argv[2]);

        // Si ambos argumentos son 0, ocurre un error
        if(x == 0 && y==0){
            printf("Error: Ambos argumentos son 0\n ");}

        else{

            // Si alguno de los argumentos son negativos, ocurre un error
            if(x<0 || y<0 ){
                printf(" Error: Alguno de los parametros es negativo\n");}
            
            else{  
                // Se detecta quien es mayor, y así se llama a la funcion mcd
                if(x>y){
                    MCD = mcd(x,y);
                    printf("MCD(%d,%d)= %d\n",x,y,MCD);} 
                    
                else{
                    MCD = mcd(y,x);
                    printf("MCD(%d,%d)= %d\n",y,x,MCD);};
                }   
            }           
    }else{
        printf("Error:La cantidad de argumentos es incorrecta\n");
        }

    return 0;
 }