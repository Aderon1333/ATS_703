#include "module.h"
#include <stdio.h>
#include <malloc.h>
#include <math.h>

double* from_file(char *name, double *arr)
{
    FILE *input;

    if ((input = fopen(name, "r")) == NULL)
    {
        printf("ERROR OPENING INPUT FILE");
    }

    arr = (double*)malloc(3*sizeof(double));
    
    for(int loc_i = 0; loc_i < 3; loc_i++)
    {
        fscanf(input,"%lf", &arr[loc_i]);
    }

    fclose(input);

    return arr;
}

double *norm(double *arr)
{
    double mod = sqrt(pow(arr[0],2) + pow(arr[1],2) + pow(arr[2],2));
    
    for(int loc_i = 0; loc_i < 3;loc_i++)
    {
        arr[loc_i] = arr[loc_i] / mod;
    }
    return arr;
}

void into_file(char *name, double *arr)
{
    FILE *output;
    
    if ((output = fopen(name, "w")) == NULL)
    {
        printf("ERROR OPENING OUTPUT FILE");
    }
    else
    {
        /*NOTHING TO DO*/
    }
    
    for(int loc_i = 0; loc_i < 3; loc_i++)
    {
        fprintf(output, "%.4lf ", arr[loc_i]);
    }

    fclose(output);
}