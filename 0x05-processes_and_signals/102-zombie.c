#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (true)
		sleep(1);

	return (0);
}

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();

		if (pid == -1)
		{
			perror("fork Error");
			exit(EXIT_FAILURE);
		}

		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(EXIT_SUCCESS);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
