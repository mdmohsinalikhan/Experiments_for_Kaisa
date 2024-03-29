#ifndef CONFIGURATION
#define CONFIGURATION

#define n 4 //number of sBoxes
#define ROUND 31
#define MAXROUND 31 //this value is required to handle the size of the arrays during the SSA experiments.
#define KEYLENGTH 10 //is in byte
#define NOFIB 6 //No of Fixed input bits
#define NOFOB 6 //No of Fixed output bits
#define SAMPLESIZEINBIT 12 //it is set to 4*n - NOFIB when full code book is used. Otherwise it has to be set manually
#define NOOFKEYS pow(2,14)
#define LOG2E 1.44269504088896340736 // log2(e)

//defining the masterkey
#define KEYS00 0x00
#define KEYS01 0x00
#define KEYS02 0x00
#define KEYS03 0x00
#define KEYS04 0x00
#define KEYS05 0x00
#define KEYS06 0x00
#define KEYS07 0x00
#define KEYS08 0x00
#define KEYS09 0x00

//number of bytes or in other words, number of unsigned chars
#define BLOCKLENGTH ((n%2 == 0 ) ? (n/2):(n/2+1))

#endif

/*the followings functions are used for generating the round keys. 
This functions will be found in keyGenerationFunctions.c file */
unsigned char** generateRoundKeys();
void rotateKey61bitLeft(int r,unsigned char **keys);
void applySBoxOnKey(int r,unsigned char **keys);
void addRoundCounterOnKey(int r,unsigned char **keys);
void printRoundKeys(unsigned char **keys);
void releaseKeyMemory(unsigned char **states);
void printMasterKey(unsigned char **keys);
void chooseAndAssignithKey(unsigned char **keys,int ithkey);

/*The following functions are basic ingredients of the cryptosystem. 
That is, the sbox and pbox. Thye are found in sboxpbox.c file */
unsigned char sBox(unsigned char input);

/*The following functions are for encryption and decryption. 
They are found in encryptionFunctions.c */
unsigned char **allocate_Memory_for_plaintext_or_ciphertext();
void printState(int r,unsigned char **states);
void encryption(unsigned char **plaintext_states,unsigned char **keys, int ithkey, unsigned long long int ***key_vs_output_count,unsigned int **trails);
void addRoundKey(int r,unsigned char **plaintext_states,unsigned char **keys);
void applySBox(int r,unsigned char **plaintext_states);
void pbox(int r,unsigned char **plaintext_states);

//Memory releasing. These functions will be found in encryptionFunctions.c file
void releaseStateMemory(unsigned char **states);


//SSA related functions. These functions will be found in ssaPreparation.c file
void prepareplaintext(unsigned char **plaintext_states,unsigned int **trails,unsigned long long int freebits);
unsigned int** preparingtheTrail();
void freeTrailMemory(unsigned int **trails);
void configureationConsistencyCheck();

//SSA experiment related functions. These functions will be found in ssaExperiment.c file
void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails);
unsigned long long int*** countKeyVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails);
void releasecountKeyVsOutputMemory(unsigned long long int ***key_a_vs_output_eta_count);
void postRoundSSABookKeping(int round,unsigned char **plaintext_states,int key_round_zero, unsigned long long int ***key_vs_output_count,unsigned int **trails);
unsigned long long int evaluateOutputOfTrail(int i,unsigned char **plaintext_states,unsigned int **trails);
unsigned long long int evaluateInputOfTrail(int i,unsigned char **plaintext_states,unsigned int **trails);
void initialize_key_vs_output_count(unsigned long long int ***key_vs_output_count);
void print_time();
long double*** prepareSSACapacities(unsigned long long int ***key_vs_output_count);
void releaseSSACapacitiesMemory(long double ***ssa_capacities);
long double computeExperimentalSSACapacity(int r,unsigned long long int a,unsigned long long int ***key_vs_output_count);
long double** computeSSACapacityTable(long double ***ssa_capacities);
void releasecomputeSSACapacityTableMemory(long double **ssa_capacities_mean_variance_table);
void printSSACapacityDetailTable(long double **ssa_capacities_mean_variance_table);
void printSSASetup(unsigned char **keys,unsigned int **trails);
