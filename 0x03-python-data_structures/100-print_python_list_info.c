#include <Python.h>
/**
 * print_python_list - prints some basic info about Python lists
 * @p: python object
 * Return: Always 0
 */
void print_python_list_info(PyObject *p)
{
	int n, allocate, i = 0;
	PyObject *obj;

	n = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (;i < n; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
