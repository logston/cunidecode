#include <stdio.h>
#include <string.h>
#include <Python.h>
#include "data.h"


static int get_string_size(char *string) {
    int size = 0;
    while (string[size] != '\0') {
        size++;
    }
    return size;
}


static char *append(char *str_head, char *str_tail) { 
    int head_size = get_string_size(str_head);
    int tail_size = get_string_size(str_tail);
    int total_size = head_size + tail_size;

    char *ret_string = (char *)malloc(sizeof(char) * (total_size + 1));

    strncpy(ret_string, str_head, head_size);
    strncpy((ret_string + head_size), str_tail, tail_size);
    ret_string[total_size] = '\0';

    free(str_head);

    return ret_string;
}


static PyObject *cunidecode_unidecode( PyObject *self, PyObject *args ) {
    Py_UNICODE *string;
    int string_size;
    if (!PyArg_ParseTuple(args, "u#", &string, &string_size)) {
      return NULL;
    } 

    char *temp_string;
    // Build an initial buffer the size of the unicode string.
    char *ret_string = (char *)malloc(sizeof(char));
    if (ret_string == 0) {
      EXIT_FAILURE;
    }
      
    ret_string[0] = '\0';

    int i, unichar, section, position;
    for (i = 0; i < string_size; i++) {
        unichar = string[i];

        // Only support the Basic Multilingual Plane
        if (unichar < 65536) {
            section = unichar >> 8;
            position = unichar % 256;
            temp_string = data[section][position];
        } else {
            temp_string = "";
        }

        ret_string = append(ret_string, temp_string);
    }

    PyObject* ret_val = Py_BuildValue("s", ret_string);

    free(ret_string);

    return ret_val;
}


static PyMethodDef cunidecode_methods[] = {
    { "unidecode", (PyCFunction)cunidecode_unidecode, METH_VARARGS,
      "Transliterate an Unicode object into an ASCII string" },
    { NULL, NULL, 0, NULL }
};


char* module_doc = "\
Transliterate Unicode text into plain 7-bit ASCII.\
\
Example usage:\
>>> from cunidecode import unidecode:\
>>> unidecode(u'\u5317\u4EB0')\
'Bei Jing'\
\
The transliteration uses a straightforward map, and doesn't have alternatives\
for the same character based on language, position, or anything else.\
";

PyMODINIT_FUNC initcunidecode() {
    Py_InitModule3("cunidecode", cunidecode_methods, module_doc);
}

