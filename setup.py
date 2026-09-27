from pybind_setup_ext import cpp_ext, setup, update_submodule

update_submodule('headers', force=True, remote=True)

kw = {
    'include_dirs': ["headers"]
}

setup(

    cpp_ext("logger2/_log.cpp", **kw),

)

