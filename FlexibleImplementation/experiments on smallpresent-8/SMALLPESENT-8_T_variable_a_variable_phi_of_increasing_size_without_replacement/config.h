#ifndef CONFIGURATION
#define CONFIGURATION

#define n 8 //number of sBoxes
#define ROUND 31
#define KEYLENGTH 10 //is in byte
#define NOFIB 8 //No of Fixed input bits
#define NOFOB 8 //No of Fixed output bits

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

/*The following functions are basic ingredients of the cryptosystem. 
That is, the sbox and pbox. Thye are found in sboxpbox.c file */
unsigned char sBox(unsigned char input);

/*The following functions are for encryption and decryption. 
They are found in encryptionFunctions.c */
unsigned char **allocate_Memory_for_plaintext_or_ciphertext();
void printState(int r,unsigned char **states);
void encryption(unsigned char **plaintext_states,unsigned char **keys,unsigned long long int fixation, unsigned long long int ****fixations_vs_output_count,unsigned int **trails,unsigned int phi_size);
void addRoundKey(int r,unsigned char **plaintext_states,unsigned char **keys);
void applySBox(int r,unsigned char **plaintext_states);
void pbox(int r,unsigned char **plaintext_states);

//Memory releasing. These functions will be found in encryptionFunctions.c file
void releaseStateMemory(unsigned char **states);


//SSA related functions. These functions will be found in ssaPreparation.c file
void prepareplaintext(unsigned char **plaintext_states,unsigned int **trails,unsigned long long int fixation,unsigned long long int freebits);
unsigned int** preparingtheTrail();
void freeTrailMemory(unsigned int **trails);
void configureationConsistencyCheck();

//SSA experiment related functions. These functions will be found in ssaExperiment.c file
void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails);
unsigned long long int**** countFixationVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails,unsigned long long int *sample_plaintext_set);
void releasecountFixationVsOutputMemory(unsigned long long int ****fixations_a_vs_output_eta_count);
void postRoundSSABookKeping(int round,unsigned char **plaintext_states,unsigned long long int fixation,unsigned long long int ****fixations_vs_output_count,unsigned int **trails,unsigned int phi_size);
unsigned long long int evaluateOutputOfTrail(int i,unsigned char **plaintext_states,unsigned int **trails);
void initialize_fixations_vs_output_count(unsigned long long int ****fixations_vs_output_count);
void printFixationsVsOutputCount(unsigned long long int ****fixations_vs_output_count);
void print_time();
//long double*** prepareSSACapacities(unsigned long long int ***fixations_vs_output_count);
//void releaseSSACapacitiesMemory(long double ***ssa_capacities);
//long double computeExperimentalSSACapacity(int r,unsigned long long int a,unsigned long long int ***fixations_vs_output_count);
//long double*** computeMeanVariancePEta(unsigned long long int ***fixations_vs_output_count);
//void releasecomputeMeanVariancePEtaMemory(long double ***mean_variance_p_eta);
//long double** computeSSACapacityTable(long double ***ssa_capacities);
//void releasecomputeSSACapacityTableMemory(long double **ssa_capacities_mean_variance_table);
//long double* computeVarianceVariancePEta(long double ***mean_variance_p_eta);
//void releasecomputeVarianceVariancePEtaMemory(long double *varaince_variance_p_eta);
//void printSSACapacityDetailTable(long double **ssa_capacities_mean_variance_table,long double *variance_variance_p_eta);
long double computeTphia(int round, unsigned int phi_size, unsigned long long int fixation,unsigned long long int ****fixations_vs_output_count);
long double*** prepareTphia(unsigned long long int ****fixations_vs_output_count);
void releaseprepareTphiaMemory(long double ***T_varaible_phi_varaible_a);
void printT_variable_phi_variable_a(long double ***T_variable_phi_variable_a);
//long double **prepareTphiaTable(long double ***T_variable_phi_variable_a,long double **ssa_capacities_mean_variance_table);
//void releaseprepareTphiaTableMemory(long double **T_phi_a_mean_variance_table);
//void print_T_phi_a_DetailTable(long double **T_phi_a_mean_variance_table,long double *variance_variance_p_eta);
void preparePythonScriptForPlotting(long double ***T_variable_phi_variable_a);

//Genearate sample without replacement relation function. These functions will be found in generateSampleWithoutReplacement.c file
unsigned long long int* generateSampleWithoutreplacement();
void sort(unsigned long long int **sample_plaintext_set_local);
void partition(unsigned long long int **sample_plaintext_set_local,unsigned long long int low,unsigned long long int high,unsigned long long int **temp);
void mergeSort(unsigned long long int **sample_plaintext_set_local,unsigned long long int low,unsigned long long int mid,unsigned long long int high,unsigned long long int **temp);
unsigned int computePhiSize(unsigned long long int freebits);
