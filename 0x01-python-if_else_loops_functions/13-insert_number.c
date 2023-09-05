#include "lists.h"
/**
 * insert_node - insert a new node at giving position of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current == NULL || number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (number > current->n)
	{
		previous = current;
		current = current->next;
		if (current->next == NULL)
		{
			current->next = new;
			return (new);
		}
	}
	previous->next = new;
	new->next = current;

	return (new);
}
