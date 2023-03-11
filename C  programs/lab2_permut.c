// -------------------------------------------#
// _____Universidad de Costa Rica______#
// ___Escuela de Ingenieria Electrica___#
// ____Laboratorio2: Permutaciones_______#

// Autor: Carlos Andres Cordero Retana B92317

// Descripcion del programa:

/* EL siguiente programa calcula todas las 
permutaciones de cualquier array ingresado 
por el usuario. Para ello, se construye la 
funcion: perm , la cual emplea el algoritmo
mostrado a continuacion (para un array de
3 elementos):

                ABC
        ABC     BAC      CBA
    ABC ACB   BAC BCA   CBA  CAB
    
Por ende, haciendo uso de dos punteros y de 
la recursion, se logra imprimir los arrays 
obtenidos en el ultimo nivel. Ahora bien,
si el usuario ingresa más de un array o no 
ingresa ninguno, se imprime un mensaje de 
error.*/


# include <stdio.h>
# include <string.h>


void perm(int bflag, char array[30]){
    /* La siguiente funcion imprime en pantalla todas las permutaciones
    del array ingresado. Los elementos del array no se deben repetir. Para ello, 
    se requieren de dos punteros: bflag y oflag, los cuales se iran moviendo a 
    través del array para poder intercambiar los elementos señalados por estos, 
    en diferentes instantes de tiempo, de acuerdo al algoritmo empleado.  */
    
    if( bflag < strlen(array)){


        // oflag debe ser igual que bflag al inicio de cada nivel
        int oflag = bflag;
        while (oflag < strlen(array)){

            if(bflag != oflag){
                if(array[bflag]==array[oflag]){
                    oflag++;
                    continue;
                }
            }


            // Se cambian los caracteres que señalan las banderas: bflag y oflag
            int temp = array[bflag];
            array[bflag] = array[oflag];
            array[oflag] = temp;

            /* Se ocupan calcular más permutaciones a partir de la permutacion actual.
            En el siguiente nivel, bflag se debe mover un espacio a la derecha.*/
            perm(bflag+1, array);

            // Se regresa al nivel anterior y lo restaura para crear la siguiente permutacion hija
            int reset = array[bflag];
            array[bflag] = array[oflag];
            array[oflag] = reset;

            // Se mueve el puntero naranja para crear la siguiente permutacion hija o para 
            oflag = oflag + 1;
        }

    
    }else{ 
        // Cuando el puntero azul llega a la ultima posicion del array, se debe imprimir.
        printf("%s\n",array);
        }
}



int main(int argc, char *argv[]){

    // Si se ingresan menos argumentos de la cuenta
    if(argc == 1){

        printf("Error: Menos argumentos de la cuenta.\n");
    // Si se ingresan más argumentos de la cuenta   
    }if(2 < argc){

        printf("Error: Más argumentos de la cuenta (sólo se puede recibir uno).\n");
    // Si se ingresa la cantidad de argumentos adecuada
    }if(argc == 2){
        printf("Las permutaciones son:\n\n");
        perm(0,argv[1]);   
        }
    return 0;
}