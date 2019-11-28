#include "../Headers/Heun.h"
#include "../Headers/rhsjansen.h"
#include "../Headers/voxel.h"
#include "../Headers/Parameters.h"
#include <math.h>
#include "gsl/gsl_rng.h"
#include "gsl/gsl_randist.h"

void Heun (Parameters *P){
		
	rhsjansen(P);	
	
	for (int iV=0; iV < P->nNodes; iV++){
		P->V[iV].X=sqrt(2*P->V[iV].epsilon*P->dt)*gsl_ran_gaussian(r,1.0);
		
 		for (int iEq=0; iEq < 6; iEq++){
                       
			P->V[iV].yold[iEq] = P->V[iV].y[iEq];
			
			P->V[iV].f_old[iEq] = P->V[iV].f[iEq];
			
			P->V[iV].y[iEq] += (P->V[iV].f[iEq])*(P->dt); // This is y_tild

			 
                       		       }				 
			P->V[iV].y[4]+=P->V[iV].X;	
			//for (int o=0;o<P->count;o++){
				//if(P->t-10*P->dt< P->Time_Occ[o] < P->t+10*P->dt){
				//if(P->t+10*P->dt>= 10.94 && 10.94 > P->t-10*P->dt){
				//P->V[i].f[4] += Pulsed_Input(&P->V[i],P->Time_Occ[o]-P->t);
				//P->V[iV].f[4] +=10.0*exp(-((P->Time_Occ[o]-P->t)/2*500)*((P->Time_Occ[o]-P->t)/2*500));
				//P->V[iV].f[4] +=(P->V[iV].A)*(P->V[iV].a)*1000.0*exp(-((10.94-P->t)/2*500)*((10.94-P->t)/2*500));
				
	
				//}
	
				//}

					     }
				


	rhsjansen(P);	// This is f_tild
	for (int iV=0; iV<P->nNodes; iV++){
		for (int iEq=0; iEq < 6; iEq++){
			P->V[iV].y[iEq]=P->V[iV].yold[iEq]+0.5*(P->V[iV].f[iEq]+P->V[iV].f_old[iEq])*(P->dt);	
     }

			   P->V[iV].y[4]+=P->V[iV].X;	
	 			//if(P->t+10*P->dt>= 10.94 && 10.94 > P->t-10*P->dt){
				//P->V[i].f[4] += Pulsed_Input(&P->V[i],P->Time_Occ[o]-P->t);
				//P->V[iV].f[4] +=10.0*exp(-((P->Time_Occ[o]-P->t)/2*500)*((P->Time_Occ[o]-P->t)/2*500));
				//P->V[iV].f[4] +=(P->V[iV].A)*(P->V[iV].a)*1000.0*exp(-((10.94-P->t)/2*500)*((10.94-P->t)/2*500));
				
	
				//}

		
} 

};
