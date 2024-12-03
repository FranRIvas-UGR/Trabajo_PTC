#include <boost/python.hpp>
#include <boost/multiprecision/cpp_int.hpp>
#include <stdexcept>
#include <boost/python/to_python_converter.hpp>

using namespace boost::multiprecision;
using namespace boost::python;

// Conversor personalizado de cpp_int a Python int
struct cpp_int_to_python {
    static PyObject* convert(const cpp_int& val) {
        return PyLong_FromString(val.str().c_str(), nullptr, 10);  // Convertir directamente a Python int
    }
};

cpp_int factorial(int n) {
    if (n < 0) {
        throw std::invalid_argument("Negative input not allowed");
    } else if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Registrar el conversor
BOOST_PYTHON_MODULE(my_module) {
    // Registro del conversor
    to_python_converter<cpp_int, cpp_int_to_python>();

    def("factorial", factorial);
}


