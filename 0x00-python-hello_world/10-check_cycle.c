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
	while (head && head->next)
	{
		temp = temp->next;
		head = head->next->next;
		if (head == temp)
			return (1);
	}
	return(0);
}
