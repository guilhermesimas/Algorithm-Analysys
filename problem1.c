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



	fclose( pFile );
	return 0;
}

int degrau_2_frascos ( long int x, int n ) {
	int raiz_n = ( int )sqrt( n );
	for ( int i = 0; i < n; i += raiz_n ) {
		/* code */
		if ( i >= x ) {
			for ( int j = i - raiz_n; j < i; j++ ) {
				/* code */
				if ( j == x ) {
					return j;
				}
			}
		}
	}
}

degrau_k_frascos( long int x, int n, int k ) {
	int raiz_kesima = ( int )pow( n, 1.0f / k );
	int inicio = 0;
	int fim = n;
	int incremento = ( int ) pow( raiz_kesima, k - 1 );
	for ( int i = 0; i < k; i++ ) {
		for ( int j = inicio; j < fim; j += incremento ) {
			if ( j >= x ) {
				if ( incremento == 1 ) {
					return j;
				}
				inicio = j - incremento;
				fim = j;
				incremento = incremento / raiz_kesima;
				break;
			}
		}
	}
}
