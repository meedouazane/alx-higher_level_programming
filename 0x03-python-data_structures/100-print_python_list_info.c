#include <Python.h>
/**
 * print_python_list - prints some basic info about Python lists
 * @p: python object
 * Return: Always 0
 */
void print_python_list(PyObject *p)
{
	int n, i = 0, a;
	PyObject *o;

	n = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", n);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < n; i++)
	{
		printf("Element %d: ", i);
		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
