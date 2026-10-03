#include <pybind11/pybind11.h>

#include "remap.h"

#include "Formatter.hpp"
#include "MutState.hpp"

PYBIND11_MODULE(_log, m) {

    py::class_<Formatter>(m, "Formatter")
        .def(py::init<>())
        .def("format", &Formatter::format);

    py::class_<MutInt>(m, "MutInt")
        .def(py::init<int>())
        .def_readwrite("value", &MutInt::value)
        .def("__bool__", &MutInt::__bool__)
        .def("__int__", &MutInt::__int__)
        .def("__index__", &MutInt::__int__)
        .def("__str__", &MutInt::__str__)
        .def("__repr__", &MutInt::__str__)
        .def("__iadd__", &MutInt::__iadd__, py::is_operator())
        .def("__isub__", &MutInt::__isub__, py::is_operator())
        .def("__add__", &MutInt::__add__, py::is_operator())
        .def("__sub__", &MutInt::__sub__, py::is_operator());

    py::class_<MutState, MutInt>(m, "MutState")
        .def_readwrite("lvalue", &MutState::lvalue)
        .def("set", &MutState::set)
        .def("pause", &MutState::pause)
        .def("resume", &MutState::resume)
        .def("enable", &MutState::enable)
        .def("disable", &MutState::disable);
    
    m.attr("VERBOSE") = py::cast(&VERBOSE);
    m.attr("HELP") = py::cast(&HELP);

}
