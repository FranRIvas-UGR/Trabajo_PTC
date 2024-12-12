#include <boost/python.hpp>

long long sum_numbers(int n) {
    long long total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
    return total;
}

BOOST_PYTHON_MODULE(my_module) {
    using namespace boost::python;
    def("sum_numbers", sum_numbers);
}

