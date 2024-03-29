#include<stdio.h>
#include<stdlib.h>
#include "config.h"

int main()
{
	int i=0;
	unsigned char **keys;
	unsigned char **plaintext_states;
	unsigned char **ciphertext_states;
	unsigned int **trails;

	configureationConsistencyCheck();

	/* generate the round keys. Block length, Number of rounds, and Master 
	key are configured in config.h file using macros */
	keys = generateRoundKeys();

	/* allocating memory for the plaintext_states. It generates a two dimensional array. 
	Each row is represents the state of that round */
	plaintext_states = allocate_Memory_for_plaintext_or_ciphertext();
	trails = preparingtheTrail();
	printSSASetup(keys,trails);

	/* Start: An example, how plaintext is prepared and encrypted 
		  To test, uncomment the lines with three slashes */
		///prepareplaintext(plaintext_states,trails,0);

		/* actual encryption is happening. Ciphertext is found in the plaintext 
		state after the last round */
		///unsigned long long int ***key_vs_output_counts;
		
		///encryption(plaintext_states,keys,key_vs_output_counts,trails);	
	/* End: An example, how plaintext is prepared and encrypted */

	SSA(plaintext_states,keys,trails);

	//releasing memories which were allocated in different places of the code
	releaseKeyMemory(keys);
	releaseStateMemory(plaintext_states);
	freeTrailMemory(trails);

return 0;
}
