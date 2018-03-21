# - Try to find TinyXML2
# This module finds TinyXML2 if it is installed and determines where
# the library and header files are. This code sets the following variables:
#
#  TINYXML2_FOUND - System has TinyXML2
#  TINYXML2_INCLUDE_DIRS - The TinyXML2 include directories
#  TINYXML2_LIBRARIES - The libraries needed to use TinyXML2
#  TINYXML2_DEFINITIONS - Compiler switches required for using TinyXML2
#
# Based on http://www.cmake.org/Wiki/CMake:How_To_Find_Libraries#Writing_find_modules

find_package(PkgConfig)
pkg_check_modules(PC_TINYXML2 tinyxml2)

find_path(TINYXML2_INCLUDE_DIR tinyxml2.h
          HINTS ${PC_TINYXML2_INCLUDEDIR}
          PATH_SUFFIXES include
          PATHS /usr /usr/local)

find_library(TINYXML2_LIBRARY tinyxml2
             HINTS ${PC_TINYXML2_LIBDIR}
             PATH_SUFFIXES lib64 lib
             PATHS /usr /usr/local)

set(TINYXML2_LIBRARIES ${TINYXML2_LIBRARY})
set(TINYXML2_INCLUDE_DIRS ${TINYXML2_INCLUDE_DIR})

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(TinyXML2 DEFAULT_MSG
                                  TINYXML2_LIBRARY TINYXML2_INCLUDE_DIR)
mark_as_advanced(TINYXML2_INCLUDE_DIR TINYXML2_LIBRARY)
