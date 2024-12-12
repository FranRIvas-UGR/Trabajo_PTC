#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <cmath>
#include <limits>
#include <numpy/ndarrayobject.h>

namespace py = boost::python;
namespace np = boost::python::numpy;

np::ndarray nearest_neighbor_search_boost_np(np::ndarray data, np::ndarray point) {
    if (data.get_nd() != 2 || point.get_nd() != 1) {
        PyErr_SetString(PyExc_ValueError, "Invalid dimensions for data or point");
        py::throw_error_already_set();
    }

    auto shape = data.get_shape();
    npy_intp num_points = shape[0];
    npy_intp dimensions = shape[1];

    if (point.shape(0) != dimensions) {
        PyErr_SetString(PyExc_ValueError, "Dimension mismatch between data and point");
        py::throw_error_already_set();
    }

    const double* data_ptr = reinterpret_cast<const double*>(data.get_data());
    const double* point_ptr = reinterpret_cast<const double*>(point.get_data());

    double min_distance = std::numeric_limits<double>::max();
    npy_intp nearest_index = -1;

    for (npy_intp i = 0; i < num_points; ++i) {
        double distance = 0.0;
        for (npy_intp j = 0; j < dimensions; ++j) {
            double diff = data_ptr[i * dimensions + j] - point_ptr[j];
            distance += diff * diff;
        }
        distance = std::sqrt(distance);

        if (distance < min_distance) {
            min_distance = distance;
            nearest_index = i;
        }
    }

    return np::from_data(&data_ptr[nearest_index * dimensions],
                         np::dtype::get_builtin<double>(),
                         py::make_tuple(dimensions),
                         py::make_tuple(sizeof(double)),
                         py::object());
}

BOOST_PYTHON_MODULE(nearest_neighbor_boost_np) {
    np::initialize();
    py::def("nearest_neighbor_search_boost_np", nearest_neighbor_search_boost_np);
}
