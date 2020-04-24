/*
Студент: Якушенков Константин
Группа №407
Задание №3.3
*/
#include <stdio.h>;
#include <conio.h>;
#include "module.h"

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("ERROR! NOT ENOUGH ARGUMENTS\n");
        return 1;
    }
    else if (argc > 3)
    {
        printf("ERROR! TOO MANY ARGUMENTS\n");
        return 1;
    }

    char *name_input = argv[1];
    char *name_output = argv[2];
    
    double* arr;

    arr = from_file(name_input, arr);
    arr = norm(arr);
    into_file(name_output, arr);

    return 0;
}