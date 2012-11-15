#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

int main(int argc, char *argv[]) 
{
	if (argc <= 1)
	{
		fprintf(stderr, "No filename given.");
		return 0;
	}

	FILE *file;
	float lat;
	float lng;
	bool b = 1;

	while(1)
	{
		if (b)
		{
			lat = 47.814019;
			lng = 9.652841;
		}
		else
		{
			lat = 47.813745;
			lng = 9.652176;
		}

		b = !b;
		

		file = fopen(argv[1], "w+");
		fprintf(file,"{\"latitude\": %f, \"longitude\": %f}", lat, lng);
		fclose(file);
		fprintf(stderr, "{\"latitude\": %f, \"longitude\": %f}\n", lat, lng);
		sleep(1);
	}

	return 0; 
}