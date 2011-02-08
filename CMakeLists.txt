project(books NONE)
cmake_minimum_required(VERSION 2.4)

include(UseLATEX.cmake)
set(PDFLATEX_COMPILER xelatex)

add_subdirectory(bely)
