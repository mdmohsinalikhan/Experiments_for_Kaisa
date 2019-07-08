#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <time.h>
#include "config.h"


/*To compute SSA capacity of every round, we run this program for 31 rounds. After every round during an encryption, we do some bookkeeping
  To do the bookkeeping after every round, we are in need of some modification in the encryption function. We have send the pointer of array fixations_vs_output_count to the encryption function. As a result its prototype and definition is changed from the original implementation*/

void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{
	/* For all possible keys, it will encrypt all possible plaintexts and store the observed number of a specific output
	   for a given round and key in an array and returns the pointer to the array*/


	unsigned long long int ***key_vs_output_count;
	key_vs_output_count = countKeyVsOutput(plaintext_states,keys,trails);

//	for(int i = 0; i < NOOFKEYS; i++)
//	{
		
//		for(int j = 0; j <= ROUND; j++)
//		{
//			printf("key: %d and round: %d \n", i, j);
			
//			for(int k = 0; k < pow(2,NOFOB); k++)
//			{
//				printf("%d occurs at out put %llu many times \n",k, key_vs_output_count[i][j][k]);		
//			}

//			printf("\n");

//		}

//	}


	/* Compute the mean and variance of $p_{\eta}(a)$ over all possible key for a given round
	   The result is stored in an array and the pointer to the array is returned */
	///long double ***mean_variance_p_eta;
	///mean_variance_p_eta = computeMeanVariancePEta(key_vs_output_count);

	/* Compute the variance of "variance of $p_{\eta}(a)$ over all possible fixation for a given round"
		over all possible $\eta$. The result is stored in an array and the pointer to the array is returned */
	///long double *variance_variance_p_eta;
	///variance_variance_p_eta = computeVarianceVariancePEta(mean_variance_p_eta);

		
	/* Computing the experimental SSA capacities i.e. $C(a)$ for a given round and fixation $a$.
	   the result is stored in an array and the pointer of the array is returned*/
	long double ***ssa_capacities;
	ssa_capacities = prepareSSACapacities(key_vs_output_count);
	
	/* 1. Compute mean and variance of experimental SSA capacities over all the fixations for every round. 
	   2. Then compute the theoretical variance of the SSA capacities over all the fixations for every round
	   3. And also compute the distance between the theoretical and experimental values of the variances of 
		SSA capacities over all fixations for every round
	   The results are stored in an array and the pointer to that array is returned*/
	long double **ssa_capacities_mean_variance_table;
	ssa_capacities_mean_variance_table = computeSSACapacityTable(ssa_capacities);

	/*
	   The below function prints the result we are expecting from this SSA experiment
	   1. It prints the average SSA capacity of every round
	   2. It prints the experimental variance of SSA capacities over all possible fixations a for every round
	   3. It prints the theoretical variance of SSA capacities over all possible fixations a for every round
	   4. It prints the distance between theoretical and experimental variance
	   5. It also prints the variance of "variance of $p_{\eta}(a)$ over all possible fixation for a given round"
		over all possible $\eta$
	   */
	printf("\n\nBelow, we print the result we are expecting from this SSA experiment \n 1. It prints the average SSA capacity of every round\n 2. It prints the experimental variance of SSA capacities over all possible keys a for every round  \n ");
	printSSACapacityDetailTable(ssa_capacities_mean_variance_table);



	
	/*Releasing allocated memory*/
	releaseSSACapacitiesMemory(ssa_capacities);
	releasecountKeyVsOutputMemory(key_vs_output_count);
	///releasecomputeMeanVariancePEtaMemory(mean_variance_p_eta);
	releasecomputeSSACapacityTableMemory(ssa_capacities_mean_variance_table);
	///releasecomputeVarianceVariancePEtaMemory(variance_variance_p_eta);
}



unsigned long long int ***countKeyVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{


	int i = 0;
	int j = 0;
	int total_keys = NOOFKEYS;
	int total_fixations = pow(2,NOFIB);
	int total_outputs = pow(2,NOFOB+NOFIB);
	unsigned long long int fixation=0;
	unsigned long long int freebits=0;
	unsigned long long int total_freebit_plaintexts = pow(2,BLOCKLENGTH*8);
	//unsigned long long int total_freebit_plaintexts = 2048;
	unsigned long long int	***key_vs_output_count = (unsigned long long int***)malloc(sizeof(unsigned long long int**)*NOOFKEYS);

	for(i = 0;i < NOOFKEYS; i++)
	{
		key_vs_output_count[i] = (unsigned long long int**)malloc(sizeof(unsigned long long int*)*(ROUND+1));

		for(j=0; j <= ROUND; j++)
		{
			key_vs_output_count[i][j] = (unsigned long long int *)malloc(sizeof(unsigned long long int)*total_outputs);			
		}
	}

	initialize_key_vs_output_count(key_vs_output_count); 

	/*Note that we have created a two dimensional array. 
	 > key_vs_output_count[i] represents a key.
	 > key_vs_output_count[i][j] represents a key and round j. */

	/*The container for counting is ready. Now, Let us encrypt all the possible plaintexts 
	  for all the possible keys, for all the possible rounds and populate the array that we just have constructed above*/


	//unsigned long long int x = 2;
	for(i = 0; i < NOOFKEYS; i++)
	{
		printf("Starting to encrypt using the %dth master key. ", i);
		chooseAndAssignithKey(keys,i); //keys are generated with replacement
		printMasterKey(keys);
		for(freebits =0; freebits < total_freebit_plaintexts; freebits++)
		{

			prepareplaintext(plaintext_states,trails,freebits);	
			encryption(plaintext_states,keys,i,key_vs_output_count,trails);	
		}

		printf("All encryptions for %dth key has been completed at: ",i); print_time();

	}

	return key_vs_output_count;

}


void releasecountKeyVsOutputMemory(unsigned long long int ***key_vs_output_count)
{
	int i = 0;
	int j = 0;
	int total_keys = NOOFKEYS;

	for(i = 0; i<total_keys; i++)
	{	
		for(j=0; j <= ROUND; j++)
		{
			free(key_vs_output_count[i][j]);
		}
		free(key_vs_output_count[i]);
	}
	
	free(key_vs_output_count);
}

void postRoundSSABookKeping(int round,unsigned char **plaintext_states,int key_round_zero, unsigned long long int ***key_vs_output_count,unsigned int **trails)
{

	unsigned long long int value_at_output_of_trail = 0;
	unsigned long long int value_at_input_of_trail = 0;
	unsigned long long int value_at_input_output_of_trail = 0;
	value_at_output_of_trail = evaluateOutputOfTrail(round,plaintext_states,trails);//checking the value of eta;
	value_at_input_of_trail = evaluateInputOfTrail(0,plaintext_states,trails);
	value_at_input_output_of_trail = (value_at_input_of_trail << NOFOB) ^ value_at_output_of_trail;
	//printf("Value of input output of the trail is: %llu",value_at_input_output_of_trail);
	key_vs_output_count[key_round_zero][round][value_at_input_output_of_trail] = key_vs_output_count[key_round_zero][round][value_at_input_output_of_trail] + 1;
}

unsigned long long int evaluateOutputOfTrail(int round,unsigned char **plaintext_states,unsigned int **trails)
{
int j = 0;
unsigned long long int value_at_output_of_trail=0;
unsigned int target_output_byte = 0;
unsigned int target_output_bit = 0;
unsigned long long int bit_value_at_outputput_bit_position = 0x00;
unsigned long long int x = 0;

	for(j = 0;j < NOFOB; j++)
	{
		target_output_byte = trails[1][j]/8;
		target_output_bit = trails[1][j]%8;
		x = 1 << target_output_bit;
		bit_value_at_outputput_bit_position = (plaintext_states[round][target_output_byte] & x) >> target_output_bit;
		value_at_output_of_trail = value_at_output_of_trail ^ (bit_value_at_outputput_bit_position << j);
	}
	
	/* for dummy purpose it is always returning 0 now. Soon this function will be properly implemented */
	return value_at_output_of_trail; 
}


unsigned long long int evaluateInputOfTrail(int round,unsigned char **plaintext_states,unsigned int **trails)
{
int j = 0;
unsigned long long int value_at_input_of_trail=0;
unsigned int target_input_byte = 0;
unsigned int target_input_bit = 0;
unsigned long long int bit_value_at_input_bit_position = 0x00;
unsigned long long int x = 0;

	for(j = 0;j < NOFOB; j++)
	{
		target_input_byte = trails[0][j]/8;
		target_input_bit = trails[0][j]%8;
		x = 1 << target_input_bit;
		bit_value_at_input_bit_position = (plaintext_states[round][target_input_byte] & x) >> target_input_bit;
		value_at_input_of_trail = value_at_input_of_trail ^ (bit_value_at_input_bit_position << j);
	}
	
	/* for dummy purpose it is always returning 0 now. Soon this function will be properly implemented */
	return value_at_input_of_trail; 
}

void initialize_key_vs_output_count(unsigned long long int ***key_vs_output_count)
{
unsigned long long int i=0;
unsigned long long int j=0;
unsigned long long int k=0;

unsigned long long int total_fixations = pow(2,NOFIB);
unsigned long long int total_outputs = pow(2,NOFOB);

	for(i = 0;i < NOOFKEYS; i++)
	{
		for(j=0; j <= ROUND; j++)
		{
			for(k=0; k < total_outputs; k++ )
			{
				key_vs_output_count[i][j][k] = 0;
			}
		}
	}	
}


/*The following function is found online. I am just using it.*/
void print_time()
{
    time_t timer;
    char buffer[26];
    struct tm* tm_info;

    time(&timer);
    tm_info = localtime(&timer);

    strftime(buffer, 26, "%Y:%m:%d %H:%M:%S", tm_info);
    puts(buffer);
}


long double*** prepareSSACapacities(unsigned long long int ***key_vs_output_count)
{
int i = 0;
unsigned long long int j = 0;
unsigned long long int total_keys = NOOFKEYS;

	long double ***ssa_capacities = (long double ***)malloc(sizeof(long double*)*(ROUND+1));

	for(i = 0; i <= ROUND;i++)
	{
		ssa_capacities[i] = (long double **)malloc(sizeof(long double*)*total_keys);
		for(j = 0; j < total_keys; j++)
		{
			ssa_capacities[i][j] = (long double *)malloc(sizeof(long double)*2);

			//and initialize
			ssa_capacities[i][j][0] = -1; //we will store the experimental capacity here for round i and fixation j
			ssa_capacities[i][j][1] = -1; //we will store the theoretical capacity here for round i and fixation j
			ssa_capacities[i][j][0] = computeExperimentalSSACapacity(i,j,key_vs_output_count);
		}
	}

return ssa_capacities;
}

void releaseSSACapacitiesMemory(long double ***ssa_capacities)
{

	int i = 0;
	unsigned long long int j = 0;
	unsigned long long int total_keys = NOOFKEYS;

	for(i = 0; i<=ROUND; i++)
	{	
		for(j=0; j < total_keys; j++)
		{
			free(ssa_capacities[i][j]);
		}
		free(ssa_capacities[i]);
	}
	
	free(ssa_capacities);

}


long double computeExperimentalSSACapacity(int r,unsigned long long int a,unsigned long long int ***key_vs_output_count)
{

unsigned long long int eta = 0;
unsigned long long int total_outputs = pow(2,NOFOB+NOFIB);
unsigned long long int size_of_sample = pow(2,BLOCKLENGTH*8);
long double capacity_a = 0;

	for(eta = 0; eta < total_outputs; eta++)
	{
		capacity_a = capacity_a + pow((key_vs_output_count[a][r][eta]/(long double)size_of_sample - 1.0/total_outputs),2);
	}
	
	capacity_a = capacity_a*total_outputs;
	
	return capacity_a;
}



/*The data type casting used while calculating the mean and variance needs to be checked closely. Could the be overflowed or truncated?*/
long double*** computeMeanVariancePEta(unsigned long long int ***key_vs_output_count)
{
int r = 0;
unsigned long long a = 0; //key.
unsigned long long eta = 0; //$\eta$.  Output bits of the trail

unsigned long long int total_outputs = pow(2,NOFOB);
unsigned long long int total_keys = NOOFKEYS;
long double mean = 0;
long double variance = 0;
unsigned long long int sum = 0;
unsigned long long int samplesize = pow(2,4*n);

	long double ***mean_variance_p_eta = (long double ***)malloc(sizeof(long double**)*(ROUND+1));

	for(r = 0; r <= ROUND; r++)
	{
		mean_variance_p_eta[r] = (long double **)malloc(sizeof(long double*)*total_outputs);
		for(eta = 0;eta < total_outputs;eta++)
		{
			mean_variance_p_eta[r][eta] = (long double *)malloc(sizeof(long double)*2);
		}
	}


	/* computing mean of $p_{\eta}(a)$ over all keys a */
	for(r = 1; r<= ROUND; r++)
	{
		for(eta = 0;eta < total_outputs; eta++)
		{
			sum = 0;
			for(a = 0; a < total_keys; a++)
			{
				sum = sum + key_vs_output_count[a][r][eta];
			}
			mean = ((long double)sum/(long double)samplesize)/(long double)total_keys;
			mean_variance_p_eta[r][eta][0] = mean;
		}
	}

	long double diff = 0;
	long double sum_for_variance = 0.0;
	/* computing varaince of $p_{\eta}(a)$ over all keys a */
	for(r = 1; r<= ROUND; r++)
	{
		for(eta = 0;eta < total_outputs; eta++)
		{
			sum_for_variance = 0;
			for(a = 0; a < total_keys; a++)
			{

				diff = (long double)key_vs_output_count[r][a][eta]/(long double)samplesize - mean_variance_p_eta[r][eta][0];
				sum_for_variance = sum_for_variance + pow(diff,2);
			}
			variance = sum_for_variance/total_keys;
			mean_variance_p_eta[r][eta][1] = variance;
		}
	}

	return mean_variance_p_eta;
}


void releasecomputeMeanVariancePEtaMemory(long double ***mean_variance_p_eta)
{
	int i = 0;
	int j = 0;
	int total_outputs = pow(2,NOFOB);

	for(i = 0; i<=ROUND; i++)
	{	
		for(j=0; j < total_outputs; j++)
		{
			free(mean_variance_p_eta[i][j]);
		}
		free(mean_variance_p_eta[i]);
	}
	
	free(mean_variance_p_eta);
}



long double** computeSSACapacityTable(long double ***ssa_capacities)
{
int i = 0;
int a = 0;
unsigned long long int total_keys = NOOFKEYS;
unsigned long long int total_outputs = pow(2,4*n);
long double **ssa_capacities_mean_variance_table = (long double **)malloc(sizeof(long double)*(ROUND+1));
long double sum = 0.0;
long double mean = 0.0;
long double experimental_variance = 0.0;

	for(i = 0;i <= ROUND; i++)
	{
		ssa_capacities_mean_variance_table[i] = (long double *)malloc(sizeof(long double)*2);

	}

	/*computing average of $C(a)$ over all possible keys a*/
	for(i = 0;i <= ROUND; i++)
	{
		sum = 0.0;
		for(a = 0; a < total_keys; a++)
		{
			sum = sum + ssa_capacities[i][a][0];
		}

		mean = sum/(long double)total_keys;
		ssa_capacities_mean_variance_table[i][0] = mean;
	}

	/*computing varaince of $C(a)$ over all possible keys a*/
	for(i = 0;i <= ROUND; i++)
	{
		sum = 0.0;
		for(a = 0; a < total_keys; a++)
		{
			sum = sum + pow((ssa_capacities[i][a][0] - ssa_capacities_mean_variance_table[i][0]),2);
		}

		experimental_variance = sum/(long double)total_keys;
		ssa_capacities_mean_variance_table[i][1] = experimental_variance;
		
	}

	return ssa_capacities_mean_variance_table;
}


void releasecomputeSSACapacityTableMemory(long double **ssa_capacities_mean_variance_table)
{

	int i =0;
	for(i = 0;i<=ROUND;i++)
	{
		free(ssa_capacities_mean_variance_table[i]);
	}

	free(ssa_capacities_mean_variance_table);

}


long double* computeVarianceVariancePEta(long double ***mean_variance_p_eta)
{
int i =0;
unsigned long int eta = 0;
unsigned long int total_outputs = pow(2,NOFOB);
long double sum = 0.0;
long double mean = 0.0;
long double variance = 0.0;

	long double *variance_variance_p_eta = (long double *)malloc(sizeof(long double)*(ROUND+1));
	
	for(i = 1; i <= ROUND; i++)
	{
		sum = 0;
		for(eta = 0; eta < total_outputs; eta++)
		{
			sum = sum + mean_variance_p_eta[i][eta][1];
		}
		mean = sum/(long double)total_outputs;

		sum = 0;
		for(eta = 0; eta < total_outputs; eta++)
		{
			sum = sum + pow((mean_variance_p_eta[i][eta][1] - mean),2);
		}
		variance = sum/(long double)total_outputs;
		variance_variance_p_eta[i] = variance;
	}
	
	return variance_variance_p_eta;
}

void releasecomputeVarianceVariancePEtaMemory(long double *variance_variance_p_eta)
{

	free(variance_variance_p_eta);
}


void printSSACapacityDetailTable(long double **ssa_capacities_mean_variance_table)
{
int i = 0;
long double distance = 0.0;
	/*Start: temporary code*/
	printf("SSA Capacity Detail Table:\nRound	Avg_C_a	Exp_Vari_C_a\n");
	for(i = 0;i <= ROUND;i++)
	{
		printf("%d	%.8Lf	%.12Lf \n",i,ssa_capacities_mean_variance_table[i][0],ssa_capacities_mean_variance_table[i][1]);
	}


}

