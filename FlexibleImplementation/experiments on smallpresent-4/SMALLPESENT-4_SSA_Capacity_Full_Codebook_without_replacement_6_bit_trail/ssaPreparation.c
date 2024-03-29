#include<stdio.h>
#include<stdlib.h>
#include "config.h"

/* Note that this program can handle if 
   1. The no of fixed bits both in plaintext-ciphertext space have to be less or equal to 64
   2. And the number of free bits both in plaintext-ciphertext space also have to be less or equal to 64.
   If any of them is larger than 64, then those bits are always kept as zero	

   It takes the least signficant NOFIB number of bits from the integer fixation and set them as the fixation of the trail.
   Then it takes lest significant min(64,(BLOCKLENGTH*8-NOFIB)) number of bits from the integer freebits and set them as free bits of plaintext
   */

void prepareplaintext(unsigned char **plaintext_states,unsigned int **trails,unsigned long long int freebits)
{
int i =0;
int j = 0;
int target_byte_position = 0;
int target_bit_position = 0;
unsigned char ith_freebit_value_of_plaintext = 0x00;
int no_of_free_bits = BLOCKLENGTH*8; // in this case it is all the bits of the plaintext, because no fixation is used

	/*First initialize the plaintext_state to all zero*/

	for(i = 0; i <= ROUND; i++)
	{
		for(j = 0;j < BLOCKLENGTH; j++)
		{
			plaintext_states[i][j] = 0x00;
		}

	}


	for(i = 0;i < no_of_free_bits; i++)
	{

		/* There are BLOCKLENGTH*8-NOFIB number of free bits in the plaintext. However, since, we do not use any fixation in this experiment, 
		   the no of free bits is all the bits of the plaintext, i.e., BLOCKLENGTH*8 . The bits from the bitstring of the integer "freebits" 
		   will be set as the free bits in the plaintext.  The LSB and MSB of the integer "freebits" will become the first and last bits
		   of the input trail respectively. */
		ith_freebit_value_of_plaintext = (freebits >> i) & 0x0000000000000001;
		/* ith fixed bit of the input trail should be fixed at some target bit position of the plaintext. 
		   This target bit position is mentioned trails[0][i]. Now the task is to find this bit position in plaintext_states[0] array  */
		target_byte_position = i/8;
		target_bit_position = i%8;

		/* Fixing the bit value to the bit position of the plaintext*/
		plaintext_states[0][target_byte_position] = plaintext_states[0][target_byte_position] ^ (ith_freebit_value_of_plaintext << target_bit_position);

	}

}

unsigned int** preparingtheTrail()
{

	int i;
	unsigned int x = 0;
	unsigned int **trails;

	trails = (unsigned int **)malloc(sizeof(unsigned int*)*4);
	
	trails[0] = (unsigned int *)malloc(sizeof(unsigned int)*NOFIB);
	trails[1] = (unsigned int *)malloc(sizeof(unsigned int)*NOFOB);

	trails[2] = (unsigned int *)malloc(sizeof(unsigned int)*(BLOCKLENGTH*8-NOFIB)); //non trail at input
	trails[3] = (unsigned int *)malloc(sizeof(unsigned int)*(BLOCKLENGTH*8-NOFOB)); //non trail at output


	/*START: Hard coding the SSA trail inside the code. However, in below one can take it from user from standard input*/
	trails[0][0] = 9; 
	trails[0][1] = 10; 
	trails[0][2] = 11; 
	trails[0][3] = 13; 
	trails[0][4] = 14; 
	trails[0][5] = 15; 


	trails[1][0] = 9; 
	trails[1][1] = 10; 
	trails[1][2] = 11;
	trails[1][3] = 13; 
	trails[1][4] = 14; 
	trails[1][5] = 15; 

	/*End: Hard coding the SSA trail inside the code. However, in below one can take it from user from standard input*/
	
	/*
	Using this commented portion of the code, someone can take the ssa trail as input from the cryptanalyst

	printf("The program is configured in config.h file. It expects %d bits input and %d bits output trail.\n",NOFIB,NOFOB);
	printf("Please Enter bit positions of the input of the trail (starting from zero at right):");
	for(i = 0; i < NOFIB; i++)
	{
		scanf("%d",&x);
		trails[0][i] = x;
	}

	printf("Enter bit positions of the output of the trail (starting from zero at right):");
	for(i = 0; i < NOFOB; i++)
	{
		scanf("%d", &x);
		trails[1][i] = x;
	} */

	int in_trail = 0;
	int j = 0;
	int k = 0;
	int l = 0;

	/*Below commplex for loop is to generate the nontrails*/
	for(i = 0; i < BLOCKLENGTH*8; i++)
	{
		/*At first check if bit position i is in the trail or not. If it is in the trail, do nothing.
		  If it is not in the trail then add it in the non-trail*/
		in_trail = 0;
		for(j = 0;j < NOFIB; j++)
		{
			if(trails[0][j] == i)
			{	
				in_trail = 1; //will indicate that bit position i is in the trail
				break;
			}
		}

		if(in_trail == 0) 
		{
			trails[2][k] = i; //bit position i is not in the input trail. taking it in input nontrails
			k++;
		}


		in_trail = 0;
		for(j = 0;j < NOFOB; j++)
		{
			if(trails[1][j] == i)
			{	
				in_trail = 1; //will indicate that bit position i is in the trail
				break;
			}
		}

		if(in_trail == 0) 
		{
			trails[3][l] = i; //bit position i is not in the trail. taking it in nontrails
			l++;
		}

	}

return trails;

}

void freeTrailMemory(unsigned int **trails)
{

free(trails[0]);
free(trails[1]);
free(trails[2]);
free(trails[3]);

free(trails);

}

void configureationConsistencyCheck()
{
char x;
int i = 0;

if(NOFIB > 64 || NOFOB > 64 || (4*n)-NOFIB > 64 || (4*n)-NOFOB > 64)
{
	printf("Note that this program can handle if \n1. The no of fixed bits both in plaintext-ciphertext space is less or equal to 64 \n2. And the number of free bits is also less or equal to 64. \nIf one of them is larger than 64, then those bits are always kept as zero. \n Do you want to continue?");
	scanf("%c",&x);

}


}


void printSSASetup(unsigned char **keys,unsigned int **trails)
{
	int i = 0;


	printf("SMALLPRESENT-[%d]\n",n);
	printf("No of Rounds:%d\n",ROUND);
	printf("Block size: %d bits\n",4*n);
	//printMasterKey(keys);
	printf("Size of input trail:%d\n",NOFIB);
	printf("Size of output trail:%d\n",NOFIB);

	printf("Bit positions at the input of the trail (starting from zero from the right):");
	for(i = 0; i < NOFIB;i++)
	{
		printf("%d ", trails[0][i]);
	}
	printf("\n");
	/*printf("Bit positions at the input of the nontrail (starting from zero from the right):\n");
	for(i = 0; i < BLOCKLENGTH*8-NOFIB;i++)
	{
		printf("%d ", trails[2][i]);
	}
	printf("\n"); */
	printf("Bit positions at the output of the trail (starting from zero from the right):");
	for(i = 0; i < NOFOB;i++)
	{
		printf("%d ", trails[1][i]);
	}
	printf("\n");
	/*printf("Bit positions at the output of nontrail (starting from zero from the right):\n");
	for(i = 0; i < BLOCKLENGTH*8-NOFOB;i++)
	{
		printf("%d ", trails[3][i]);
	}
	printf("\n"); */
}
