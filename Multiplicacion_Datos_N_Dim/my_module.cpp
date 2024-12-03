#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <Eigen/Dense>

namespace p = boost::python;
namespace np = boost::python::numpy;

np::ndarray matrix_multiply(const np::ndarray& A, const np::ndarray& B) {
    int rowsA = A.shape(0);
    int colsA = A.shape(1);
    int colsB = B.shape(1);

    Eigen::MatrixXd matA(rowsA, colsA);
    Eigen::MatrixXd matB(colsA, colsB);

    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsA; ++j) {
            matA(i, j) = p::extract<double>(A[i][j]);
        }
    }

    for (int i = 0; i < colsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            matB(i, j) = p::extract<double>(B[i][j]);
        }
    }

    Eigen::MatrixXd result = matA * matB;
    p::tuple shape = p::make_tuple(result.rows(), result.cols());
    np::dtype dtype = np::dtype::get_builtin<double>();
    np::ndarray result_np = np::zeros(shape, dtype);
    for (int i = 0; i < result.rows(); ++i) {
        for (int j = 0; j < result.cols(); ++j) {
            result_np[i][j] = result(i, j);
        }
    }
    return result_np;
}

BOOST_PYTHON_MODULE(my_module) {
    np::initialize();
    p::def("matrix_multiply", matrix_multiply);
}
