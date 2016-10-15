#include <stdio.h>
#include <stdlib.h>

#define BASE 2

int main( int argc, char const *argv[] ) {

	FILE *pFile;
	long int *number;
	char *numberInBinary;
	int nBits, nNumeros;

	pFile = fopen( argv[1], "r" );

	fscanf( pFile, "%d%d\n", &nBits, &nNumeros );

	printf( "Running for %d bits and %d numbers\n", nBits, nNumeros );

	number = ( long int* )malloc( nNumeros * sizeof( long int ) );
	numberInBinary = ( char* )malloc( ( nBits + 1 ) * sizeof( char ) );

	for ( int i = 0; i < nNumeros; ++i ) {
		fscanf( pFile, " %[^\n]", numberInBinary );
		numberInBinary[nBits] = '\0';
		// printf( "%s\n", numberInBinary );
		number[i] = strtol( numberInBinary, NULL, BASE );
		// printf( "%d\n", number[i] );
	}