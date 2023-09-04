#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list that we will check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *head;

	temp = list;
	head = list;
	if (!list)
		return (0);
	while (head->next != NULL)
	{
		head = head->next;
		if (head == temp)
			return (1);
	}
	return(0);
}
