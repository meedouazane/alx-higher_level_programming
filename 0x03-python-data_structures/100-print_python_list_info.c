#include <Python.h>
/**
 * print_python_list - prints some basic info about Python lists
 * @p: python object
 * Return: Always 0
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, size, allo;
	PyObject *obj;

	size = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allo);

	while (i < size)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
