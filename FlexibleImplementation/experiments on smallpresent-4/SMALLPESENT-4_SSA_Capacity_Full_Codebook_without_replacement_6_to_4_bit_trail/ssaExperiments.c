#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <time.h>
#include "config.h"


/*To compute SSA capacity of every round, we run this program for 31 rounds. After every round during an encryption, we do some bookkeeping
  To do the bookkeeping after every round, we are in need of some modification in the encryption function. We have sent the pointer of an array key_vs_output_count to the encryption function. As a result its prototype and definition is changed from the original implementation*/

void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{
	/* We will choose a large set of kyes. For each key of the set it will encrypt the full codebook and store the observed number of a specific input/output-bits
	   for a given round and key; in an array and returns the pointer to the array*/

	printf("All the masterkeys are chosen randomly with replacement. \n \n");
	unsigned long long int ***key_vs_output_count;
	key_vs_output_count = countKeyVsOutput(plaintext_states,keys,trails);


	/* Computing the experimental SSA capacities i.e. $C(a)$ for a given round and key $a$.
	   the result is stored in an array and the pointer of the array is returned*/
	long double ***ssa_capacities;
	ssa_capacities = prepareSSACapacities(key_vs_output_count);
	
	/* 1. Compute mean and variance of experimental SSA capacities over all the used keys for every round. */
	long double **ssa_capacities_mean_variance_table;
	ssa_capacities_mean_variance_table = computeSSACapacityTable(ssa_capacities);

	/*
	   The below function prints the result we are expecting from this SSA experiment
	   1. It prints the mean and variance of SSA capacity of every round computed over all the keys used 	   */
	printf("\n\nBelow, we print the result we are expecting from this SSA experiment \n 1. It prints the average SSA capacity of every round over the used keys\n 2. It prints the experimental variance of SSA capacities over all possible keys a for every round  \n ");
	printSSACapacityDetailTable(ssa_capacities_mean_variance_table);



	
	/*Releasing allocated memory*/
	releaseSSACapacitiesMemory(ssa_capacities);
	releasecountKeyVsOutputMemory(key_vs_output_count);
	releasecomputeSSACapacityTableMemory(ssa_capacities_mean_variance_table);
}



unsigned long long int ***countKeyVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{


	int i = 0;
	int j = 0;
	int total_keys = NOOFKEYS;
	int total_outputs = pow(2,NOFOB+NOFIB); /* this is the number of total possible output values for which we would like to compute the capacity. 
						   This is needed to create the array to keep the record –– how many times a specific output occured in the input/output trail */
	unsigned long long int freebits=0; // the variable freebits will be converted into the bits of plaintext that will be encrypted
	unsigned long long int total_freebit_plaintexts = pow(2,BLOCKLENGTH*8); // the number of plaintexts that will be encrypted. In this experiment, it is the full codebook
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

	/*Note that we have created a three dimensional array. 
	 > key_vs_output_count[i] represents a key.
	 > key_vs_output_count[i][j] represents a key and round j. */

	/*The container for counting is ready. Now, Let us encrypt the full codebook  –– all the possible plaintext (no fixed bits in the input trail)
	  for #NOOFKEYS many keys, for all the possible rounds and populate the array that we just have constructed above*/



	for(i = 0; i < NOOFKEYS; i++)
	{
		printf("Starting to encrypt using the %dth master key. ", i);
		 /*a masterkey will be generated with replacement i.e, it may generate a key which has been used before. 
						However, NOOFKYES is in the range of 2^8 to 2^16. The keyspace is as big as 2^80. 
						So it is almost guranteed that no keys will be repeated */
		chooseAndAssignithKey(keys,i);
		printMasterKey(keys); // prints the master key which just have been chosen in the previous step

		for(freebits =0; freebits < total_freebit_plaintexts; freebits++)
		{

			prepareplaintext(plaintext_states,trails,freebits); /* the bits of freebits variable are encoded as the bits of plaintext. 
										since no fixation is used in this experiment, the information 
										in the trail is not really used */
			encryption(plaintext_states,keys,i,key_vs_output_count,trails);	/* the bookkeeping function will be called from inside the encryption function. 
											   Informtion in the trail is not used for encryption but bookkeeping. */
		}

		printf("All encryptions for %dth key has been completed at: ",i); print_time();

	}

	return key_vs_output_count;

}



void initialize_key_vs_output_count(unsigned long long int ***key_vs_output_count)
{
unsigned long long int i=0;
unsigned long long int j=0;
unsigned long long int k=0;

unsigned long long int total_outputs = pow(2,NOFOB+NOFIB);

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


void postRoundSSABookKeping(int round,unsigned char **plaintext_states,int key_round_zero, unsigned long long int ***key_vs_output_count,unsigned int **trails)
{

	unsigned long long int value_at_output_of_trail = 0;
	unsigned long long int value_at_input_of_trail = 0;
	unsigned long long int value_at_input_output_of_trail = 0;
	value_at_output_of_trail = evaluateOutputOfTrail(round,plaintext_states,trails); //checking the value of eta;
	value_at_input_of_trail = evaluateInputOfTrail(0,plaintext_states,trails);
	value_at_input_output_of_trail = (value_at_input_of_trail << NOFOB) ^ value_at_output_of_trail; // leftshift the input bits so that the output bits have space to be xored
	/* because, in this experiment, the distribution for which we compute the capacity is : the distribution of the bits at the plaintext and chiphertext of the trail. 
	In the experiments of my masters thesis, we were interested in the distribution of the bits in ciphertext of the trail */
	key_vs_output_count[key_round_zero][round][value_at_input_output_of_trail] = key_vs_output_count[key_round_zero][round][value_at_input_output_of_trail] + 1;


	// following lines of code is used to test if extracting bits from the trail is working okay or not	
	//printf("ROUND: %d\n", round);
	//printf("Plaintext: %02X %02X ; value at input of trail: %llu \n", plaintext_states[0][0],plaintext_states[0][1], value_at_input_of_trail);
	//printf("Ciphertext: %02X %02X ; value at output of trail: %llu \n", plaintext_states[round][0],plaintext_states[round][1], value_at_output_of_trail);
	//printf("Value of the input output bits combined: %llu \n\n", value_at_input_output_of_trail);

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

	for(j = 0;j < NOFIB; j++)
	{
		target_input_byte = trails[0][j]/8;
		target_input_bit = trails[0][j]%8;
		x = 1 << target_input_bit;
		bit_value_at_input_bit_position = (plaintext_states[round][target_input_byte] & x) >> target_input_bit;
		value_at_input_of_trail = value_at_input_of_trail ^ (bit_value_at_input_bit_position << j);
	}
	
	return value_at_input_of_trail; 
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



long double computeExperimentalSSACapacity(int r,unsigned long long int a,unsigned long long int ***key_vs_output_count)
{

unsigned long long int eta = 0;
unsigned long long int total_outputs = pow(2,NOFOB+NOFIB);
unsigned long long int size_of_sample = pow(2,BLOCKLENGTH*8);
long double capacity_a = 0.0;

	for(eta = 0; eta < total_outputs; eta++)
	{
		capacity_a = capacity_a + pow(( (long double) (key_vs_output_count[a][r][eta]/(long double)size_of_sample) -  (long double)(1.0/total_outputs)),2);
	}
	
	capacity_a = capacity_a*total_outputs;
	
	return capacity_a;
}






long double** computeSSACapacityTable(long double ***ssa_capacities)
{
int i = 0;
int a = 0;
unsigned long long int total_keys = NOOFKEYS;
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

		experimental_variance = (long double)(sum/(long double)total_keys);
		ssa_capacities_mean_variance_table[i][1] = experimental_variance;
		
	}

	return ssa_capacities_mean_variance_table;
}


void printSSACapacityDetailTable(long double **ssa_capacities_mean_variance_table)
{
int i = 0;
long double mean = 0.0, variance = 0.0;

	/*Start: temporary code*/
	printf("SSA Capacity Detail Table:\nRound	Avg_C_a	(log_2)	Exp_Vari_C_a (log_2)\n");
	for(i = 0;i <= ROUND;i++)
	{
		mean = -1.0*log(ssa_capacities_mean_variance_table[i][0])*LOG2E;
		variance = -1.0*log(ssa_capacities_mean_variance_table[i][1])*LOG2E;
		printf("%d	%.8Lf	%.12Lf \n",i,mean,variance);
	}


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
