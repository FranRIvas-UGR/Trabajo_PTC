#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <cmath>
#include <stdexcept>

namespace py = boost::python;
namespace np = boost::python::numpy;

double calcular_promedio(np::ndarray arr) {
    // Verificar que el array tiene solo una dimensión
    if (arr.get_nd() != 1) {
        PyErr_SetString(PyExc_ValueError, "El array debe ser unidimensional");
        py::throw_error_already_set();
    }

    int longitud = arr.shape(0);
    if (longitud == 0) {
        PyErr_SetString(PyExc_ValueError, "El array no puede estar vacío");
        py::throw_error_already_set();
    }

    // Asegurarse de que el array tiene el tipo correcto (double)
    if (arr.get_dtype() != np::dtype::get_builtin<double>()) {
        PyErr_SetString(PyExc_TypeError, "El array debe contener números de tipo float");
        py::throw_error_already_set();
    }

    // Accede a los datos directamente en la memoria
    double* data = reinterpret_cast<double*>(arr.get_data());

    double suma = 0.0;
    for (int i = 0; i < longitud; ++i) {
        suma += data[i];
    }

    return suma / longitud;
}

BOOST_PYTHON_MODULE(calcular_promedio_boost_module) {
    Py_Initialize();
    np::initialize();
    py::def("calcular_promedio", calcular_promedio);
}
