#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list that we will check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		if (list->next == NULL)
			return (0);
		if (list->next == temp)
			return (1);
		list = list->next;
	}
	return(0);
}
