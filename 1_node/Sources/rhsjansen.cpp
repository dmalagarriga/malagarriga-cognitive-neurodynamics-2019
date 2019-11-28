#include "../Headers/rhsjansen.h"
#include "../Headers/Parameters.h"
#include "../Headers/voxel.h"
#include <math.h>


float S(voxel *V, float nu){
	
	float value;
	value=2.0*V->e0/(1.0+exp(V->r*(V->nu0 - nu)));
        return value;
}

float S_coupling(voxel *V, float nu){
	
	float value;
	value=(2.0/(1.0+exp(-V->r*nu))-1);
        return value;
}
		

void rhsjansen (Parameters *P){

		
for (int i=0; i < P->nNodes; i++){
	
	
		
P->V[i].f[0] = P->V[i].y[3];
P->V[i].f[3] = (P->V[i].A)*(P->V[i].a)*S(&P->V[i], P->V[i].y[1] - P->V[i].y[2]) - 2*(P->V[i].a)*P->V[i].y[3] - (P->V[i].a)*(P->V[i].a)*P->V[i].y[0];

P->V[i].f[1] = P->V[i].y[4] ;
P->V[i].f[4] = (P->V[i].A)*(P->V[i].a)*(P->V[i].p+P->V[i].amp*sin(2*M_PI*P->V[i].freq*P->t+P->V[i].phase/2*M_PI)+ P->V[i].c2*S(&P->V[i], (P->V[i].c1*P->V[i].y[0]))) - 2*(P->V[i].a)*P->V[i].y[4] - (P->V[i].a)*(P->V[i].a)*P->V[i].y[1];

P->V[i].f[2] = P->V[i].y[5]; 
P->V[i].f[5] = (P->V[i].B)*(P->V[i].b)*(P->V[i].c4)*S(&P->V[i], P->V[i].c3*P->V[i].y[0]) - 2*(P->V[i].b)*P->V[i].y[5] - (P->V[i].b)*(P->V[i].b)*P->V[i].y[2];
/*
for (int o=0;o<P->count;o++){
if(P->t+10*P->dt>= P->Time_Occ[o] && P->Time_Occ[o] > P->t-10*P->dt){
				//P->V[i].f[4] += Pulsed_Input(&P->V[i],P->Time_Occ[o]-P->t);
				P->V[i].f[4] +=(P->V[i].A)*(P->V[i].a)*1000.0*exp(-((P->Time_Occ[o]-P->t)/2*500)*((P->Time_Occ[o]-P->t)/2*500));
				//P->V[i].f[4] +=(P->V[i].A)*(P->V[i].a)*1000.0*exp(-((10.94-P->t)/2*500)*((10.94-P->t)/2*500));
				
				}
				}
*/
for (int l=0; l < P->nNodes; l++){
		
	if(P->Kex[i][l]!=0.0){
	//P->V[i].f[4] += (P->V[i].A)*(P->V[i].a)*(P->Kex[i][l]/P->nNodes)*P->V[i].alpha*S(&P->V[l], P->V[l].y[1]-P->V[l].y[2]);
	P->V[i].f[4] += (P->V[i].A)*(P->V[i].a)*(P->Kex[i][l])*P->V[i].alpha*S(&P->V[l], P->V[l].y[1]-P->V[l].y[2]); 
		
										}
						
					
						}

for (int j=0;j<P->nNodes;j++){
	if(P->Kin[i][j]!=0.0){
		
	//	P->V[i].f[5] += (P->V[i].B)*(P->V[i].b)*(P->Kin[i][j]/P->nNodes)*P->V[i].beta*S(&P->V[j], P->V[j].y[1]-P->V[j].y[2]);
	//	P->V[i].f[5] += (P->V[i].B)*(P->V[i].b)*(P->Kin[i][j])*P->V[i].beta*S(&P->V[j], P->V[j].y[1]-P->V[j].y[2]);
		P->V[i].f[5] += (P->V[i].B)*(P->V[i].b)*(P->Kin[i][j])*P->V[i].beta*S(&P->V[j], P->V[j].c3*P->V[j].y[0]); //Short range 'à la' Pons et al.
						}
	}

}


cout << P->Time_Occ[P->count-2]/P->nNodes << endl;

int m = 0;

while ( m < P->nNodes)
{
for (int o=0;o<P->count-2;o++){
if(P->Time_Occ[o]>=m*P->Time_Occ[P->count-2]/P->nNodes && P->Time_Occ[o]<=(m+1)*P->Time_Occ[P->count-2]/P->nNodes){if(P->t+10*P->dt>= P->Time_Occ[o]-(m*P->Time_Occ[P->count-2]/P->nNodes) && P->Time_Occ[o]-(m*P->Time_Occ[P->count-2]/P->nNodes) > P->t-10*P->dt){

					P->V[m].f[4] +=P->V[m].Decide_input*(P->V[m].A)*(P->V[m].a)*1000.0*exp(-((P->Time_Occ[o]-(m*P->Time_Occ[P->count-2]/P->nNodes)-P->t)/2*500)*((P->Time_Occ[o]-(m*P->Time_Occ[P->count-2]/P->nNodes)-P->t)/2*500));
				
				}
				}


}
m++;
}

/*
for (int o=0;o<P->count;o++){
if(P->Time_Occ[o]<=2300){if(P->t+10*P->dt>= P->Time_Occ[o] && P->Time_Occ[o] > P->t-10*P->dt){

				P->V[0].f[4] +=P->V[0].Decide_input*(P->V[0].A)*(P->V[0].a)*1000.0*exp(-((P->Time_Occ[o]-P->t)/2*500)*((P->Time_Occ[o]-P->t)/2*500));
				
				}
				}
if(P->Time_Occ[o]>=2300 && P->Time_Occ[o]<=4600){if(P->t+10*P->dt>= P->Time_Occ[o]-(2300) && P->Time_Occ[o]-(2300) > P->t-10*P->dt){
				
				P->V[1].f[4] +=P->V[1].Decide_input*(P->V[1].A)*(P->V[1].a)*1000.0*exp(-((P->Time_Occ[o]-(2300)-P->t)/2*500)*((P->Time_Occ[o]-(2300)-P->t)/2*500));
				
				
				}
				}
if(P->Time_Occ[o]>=4600){if(P->t+10*P->dt>= P->Time_Occ[o]-4600 && P->Time_Occ[o]-4600 > P->t-10*P->dt){
				
				P->V[2].f[4] +=P->V[2].Decide_input*(P->V[2].A)*(P->V[2].a)*1000.0*exp(-((P->Time_Occ[o]-4600-P->t)/2*500)*((P->Time_Occ[o]-4600-P->t)/2*500));
				
				
				}
				}				
}
				         
				         
*/				                 


}
