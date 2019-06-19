# Minimum version of CMake required to build this project
cmake_minimum_required(VERSION 3.0)

#language standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Name of the project
project(NotificationBot)

# Create a few variables for the folder names
# set(HELPERS_DIR src/helpers)
# set(MODELS_DIR src/models)

add_executable(
  NotificationBot
  src/main.cpp
  src/weather.cpp
#   ${HELPERS_DIR}/AwesomeHelper.cpp
#   ${HELPERS_DIR}/OkHelper.cpp
#   ${MODELS_DIR}/Person.cpp
)

#find libraries
add_subdirectory(libraries/cpr)

# Add all the source files needed to build the executable

target_link_libraries (NotificationBot cpr)



