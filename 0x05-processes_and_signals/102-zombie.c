#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - function for infinite sleep loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * Description: create 5 zombie processes
 * Return: 0
 */
int main(void)
{
	unsigned int z;
	pid_t child_pid;

	for (z = 0; z < 5; z++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
