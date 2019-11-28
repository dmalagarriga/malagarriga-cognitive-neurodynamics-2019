#include <iostream>
#include <cstdlib>
#include "../Headers/Parameters.h"
#include "../Headers/Heun.h"
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"


using namespace std;

Parameters * P;
const gsl_rng_type * T;
unsigned long int seed=atoi(getenv("SEED"));
gsl_rng * r;
float FREQ=strtod(getenv("Frequencia"),NULL);
float AMP=strtod(getenv("Amplitud"),NULL);
float SEC=strtod(getenv("Section"),NULL);




int main (int argc, char **argv){

    
    P=new Parameters;

    gsl_rng_env_setup();
    
   
    T = gsl_rng_default;
    r = gsl_rng_alloc (T);

    gsl_rng_set(r,seed);
	//P->nt = P->Time_Occ[P->count-8000]/(P->nNodes*P->dt); // Total number of steps, given by the length of Time_Occurrences
	P->nt = P->Time_Occ[P->count-2]/(P->nNodes*P->dt);
//Initial conditions 

	for (int i=0; i<P->nNodes; i++){
		
		for (int j=0; j<6; j++){
		
			P->V[i].y[j] = 1*gsl_ran_gaussian(r,10.0);
			
				
					}
			//P->V[i].phase=1*gsl_ran_gaussian(r,10.0);
			P->V[i].phase=gsl_ran_flat(r,0.0,6.28);
					}
	
	P->WriteInitialConditions(seed);
	
	for (int i=0;i<P->nNodes;i++){
		
		P->V[i].amp=AMP;
		P->V[i].freq=FREQ;
		
						     }
	
	
	for (P->it=0; (P->it) < (P->nt); P->it++){	

	        Heun(P); 
          	P->RefreshDelay();	
		    P->t+=P->dt;
	//cout << P->V[0].y[0] << endl;
	//if(0.1 <P->V[0].y[0] && P->V[0].y[0]<0.108){cout<<P->t << " " << P->V[0].y[1] << " " << P->V[0].y[2] << endl;}
	if(SEC < P->V[0].y1y2[10] && P->V[0].y1y2[10]<SEC+0.5){P->WritePoincare();}
	
	
        if (P->it % P->ntout ==0)
		{	
		P->WriteData();
		  	
		}
	    
						}	
	
	
	gsl_rng_free (r);
	delete P;

return EXIT_SUCCESS;

}
