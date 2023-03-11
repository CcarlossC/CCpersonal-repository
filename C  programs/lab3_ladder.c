

// -------------------------------------------#
// _____Universidad de Costa Rica______#
// ___Escuela de Ingenieria Electrica___#
// ____Laboratorio3: Formas de subir una escalera_______#

// Autor: Carlos Andres Cordero Retana B92317

// Descripcion del programa:
  
  /*
  El siguiente programa calcula e imprime todas las posibles formas
  de subir una escalera compuesta por 1 o 2 o 3 .. o 11 escalones en pasos 
  de 1,2,3 y 4. Para ello, se crean dos funciones: combi y perm. La primera 
  calcula algun combinacion con repeticion que sume N, y la segunda, genera 
  todas las permutaciones posibles de la combinacion calculada por combi.
*/


# include <stdio.h>
# include <string.h>
# include <stdlib.h>

/* La funcion perm trabaja con los siguientes parametros de entrada:

- bflag: puntero que fija un elemento del array en un momento determinado.
- array: contiene los elementos que se van a permutar
- count: cuenta el numero de permutaciones generadas
- permutations: almacena todas las permutaciones generadas

Funcion que calcula e imprime todas las permutaciones posibles
en base a una combinacion de entrada dada.
*/

void perm(int bflag, char array[100], int *count, char **permutations) {
 
    
    if (bflag < strlen(array)) {       
        int oflag = bflag;

        // El puntero oflag se posiciona en cada elemento del array                 
        while (oflag < strlen(array)) {     
            
            // Se optimiza para no crear combinaciones innecesarias
            if (bflag != oflag) {
                if (array[bflag] == array[oflag]) {
                    oflag++;
                    continue;
                }
            }
            // Se cambian los caracteres que señalan las banderas: bflag y oflag
            int temp = array[bflag];
            array[bflag] = array[oflag];
            array[oflag] = temp;

             
            // Se crean mas permutaciones hijas
            perm(bflag+1, array, count, permutations);
            
            // Se regresa al nivel anterior y lo restaura para crear la siguiente permutacion hija
            int reset = array[bflag];
            array[bflag] = array[oflag];
            array[oflag] = reset;

            // Se mueve el puntero naranja para crear la siguiente permutacion hija
            oflag = oflag + 1;
        }

    // Cuando bflag apunta al ultimo elemento
    } else {            
        int j;  

       
        int is_new_permutation = 1;    
        // Se verifica si la permutacion ya existe
        for (j = 0; j < *count; j++) {           
            if (strcmp(array, permutations[j]) == 0) {  
                is_new_permutation = 0;  
                break;
            }
        }// La permutacion se copia a la memoria reservada
        if (is_new_permutation) {  
            permutations[*count] = malloc(strlen(array) + 1); 
            strcpy(permutations[*count], array);  
            (*count)++;  
         
            // Se imprime la permutacion
            for (j = 0; j < strlen(array); j++) {
                if (j == (strlen(array)-1)) {
                    printf("%c ", array[j]);
                } else {
                    printf("%c, ", array[j]);
                }    
            }
            printf("\n");
        }
    }
}



/* La funcion combi trabaja con los siguientes parametros de entrada:

- len: numero de elementos de cvector
- cvector: vector que contiene la combinacion actual.
- Ns: Cantidad de escalones dada por el usuario.
- validcombis: bandera que guarda la cantidad de iteraciones en las cuales el array suma Ns.
- iters: iteraciones que deben hacerse para disminuir el calculo de combinaciones innecesarias.

Funcion que calcula alguna combinacion con repeticion que sume Ns, de modo que se la pueda brindar 
a la funcion permu para que esta pueda calcular todas las permutaciones de la combinacion dada.
*/

void combi(int len, int cvector[50], int Ns, int validcombis, int iters ){


    int i;
    int mul = 1;
    int new;
    int sum=0;

    for(i=(len-1); 0<=i; i-- ){

        // Si es 4, entonces se pueden tener los siguientes escenarios en cvector[i-1]
        if(cvector[i]==4){

            // Primer escenario
            if(cvector[i-1]==1){
                cvector[i-1] = 2;
                int y;
                for(y=0; y<len; y++){
                    if (cvector[y]==1){
                        continue;
                        }
                    cvector[y] = 2;
                    }
                break;
                }
            
            //Segundo escenario
            if(cvector[i-1]==2){
                cvector[i-1]=3;
                int limite = i-1;
                int v;
                for(v=0; v<len; v++){
                    if (limite<=v){
                        cvector[v] = 3;
                    }   
                }
                break;

                
                break;
            }
            
            // Tercer escenario
            if(cvector[i-1]==3){
                cvector[i-1] = 4;
                break;
            }
            
            // Cuarto escenario
            if(cvector[i-1]==4){
                continue;
            }


        // Si cvector[i] no es 4, entonces sume 1 a la combi actual
        }else{
            new = cvector[i]*mul;
			sum = sum + new;
			mul = mul*10;
                if(i==0){
                    int e;
                    int nw;
                    sum = sum + 1;
                    char strr[50];
  			        sprintf(strr, "%d", sum);

                    int sav = len;
                    for(e=(strlen(strr)-1); 0<=e ; e--){
                        int
                        nw = (int)(strr[e]) -48;
                        cvector[sav-1] = nw;
                        sav--;
                    }

                }
        }

    }


    int sumaaa = 0;
    int q;

    // Se suma los numeros del array
    for(q=0; q<len; q++){
            sumaaa=cvector[q]+sumaaa;
        }
    
    // Si la combinacion actual suma 4, entonces mandela a la funcion permu
    if(sumaaa==Ns){
        validcombis++;
        int a;
        int multi =1;
        int plus = 0;
        int newe;
        for(int a = len-1; 0 <= a; a--){
            newe= cvector[a]*multi;
            plus = plus + newe;
            multi = multi*10;
            }
        char strre[50];
        sprintf(strre, "%d", plus); 
        int count =0;
        char *permutations[200]; 

        
        // Aqui se tiene el array listo para permutar
        perm(0,strre, &count, permutations);
    
    }

    // Si ya no existen mas combinaciones que sumen 4, pare el ciclo.
    if(validcombis == iters){
            cvector[0]=4;
        }

    // Se utiliza recursion para calcular la siguiente combinacion   
    if(cvector[0]!=4){
        combi(len, cvector,Ns,validcombis,iters);
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
        int N=atoi(argv[1]);
        int x;
        int NN;
        int listaq[50];
        int ii;

        // Se genera la primera combinacion
        for(ii=0; ii<N; ii++){
                if(ii==(N-1)){
                    printf("1");
                    break;
                }
                printf("1, ");
            }
            printf("\n");

        for(NN=(N-1); 0<NN; NN--){

            // Se crea una lista de NN unos
            for(x=0; x<NN; x++){
            listaq[x] = 1;
            }
            int iters = N- NN;
    
            // Se llama a la funcion por primera vez con una condicion inicial
            combi(NN,listaq,N, 0, iters);

        }
    
    }

    return 0;

}
