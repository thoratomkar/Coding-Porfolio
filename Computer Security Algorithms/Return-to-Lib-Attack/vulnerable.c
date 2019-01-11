#include<stdio.h>

#include<string.h>

void vuln(char *arg){
	char buf[7];
	strcpy(buf, arg);
	printf("You typed: %s\n", buf);
}
int main( int argc, char** argv ) {
	vuln(argv[1]);
	return 0;
}


