# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.14.5/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.14.5/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/orlandoortega/Desktop/NotificationBot

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/orlandoortega/Desktop/NotificationBot

# Include any dependencies generated for this target.
include CMakeFiles/NotificationBot.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/NotificationBot.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/NotificationBot.dir/flags.make

CMakeFiles/NotificationBot.dir/src/main.cpp.o: CMakeFiles/NotificationBot.dir/flags.make
CMakeFiles/NotificationBot.dir/src/main.cpp.o: src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/orlandoortega/Desktop/NotificationBot/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/NotificationBot.dir/src/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/NotificationBot.dir/src/main.cpp.o -c /Users/orlandoortega/Desktop/NotificationBot/src/main.cpp

CMakeFiles/NotificationBot.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/NotificationBot.dir/src/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/orlandoortega/Desktop/NotificationBot/src/main.cpp > CMakeFiles/NotificationBot.dir/src/main.cpp.i

CMakeFiles/NotificationBot.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/NotificationBot.dir/src/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/orlandoortega/Desktop/NotificationBot/src/main.cpp -o CMakeFiles/NotificationBot.dir/src/main.cpp.s

CMakeFiles/NotificationBot.dir/src/weather.cpp.o: CMakeFiles/NotificationBot.dir/flags.make
CMakeFiles/NotificationBot.dir/src/weather.cpp.o: src/weather.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/orlandoortega/Desktop/NotificationBot/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/NotificationBot.dir/src/weather.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/NotificationBot.dir/src/weather.cpp.o -c /Users/orlandoortega/Desktop/NotificationBot/src/weather.cpp

CMakeFiles/NotificationBot.dir/src/weather.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/NotificationBot.dir/src/weather.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/orlandoortega/Desktop/NotificationBot/src/weather.cpp > CMakeFiles/NotificationBot.dir/src/weather.cpp.i

CMakeFiles/NotificationBot.dir/src/weather.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/NotificationBot.dir/src/weather.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/orlandoortega/Desktop/NotificationBot/src/weather.cpp -o CMakeFiles/NotificationBot.dir/src/weather.cpp.s

# Object files for target NotificationBot
NotificationBot_OBJECTS = \
"CMakeFiles/NotificationBot.dir/src/main.cpp.o" \
"CMakeFiles/NotificationBot.dir/src/weather.cpp.o"

# External object files for target NotificationBot
NotificationBot_EXTERNAL_OBJECTS =

NotificationBot: CMakeFiles/NotificationBot.dir/src/main.cpp.o
NotificationBot: CMakeFiles/NotificationBot.dir/src/weather.cpp.o
NotificationBot: CMakeFiles/NotificationBot.dir/build.make
NotificationBot: lib/libcpr.a
NotificationBot: lib/libcurl.dylib
NotificationBot: /usr/local/opt/openssl/lib/libssl.dylib
NotificationBot: /usr/local/opt/openssl/lib/libcrypto.dylib
NotificationBot: /usr/lib/libz.dylib
NotificationBot: CMakeFiles/NotificationBot.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/orlandoortega/Desktop/NotificationBot/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable NotificationBot"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/NotificationBot.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/NotificationBot.dir/build: NotificationBot

.PHONY : CMakeFiles/NotificationBot.dir/build

CMakeFiles/NotificationBot.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/NotificationBot.dir/cmake_clean.cmake
.PHONY : CMakeFiles/NotificationBot.dir/clean

CMakeFiles/NotificationBot.dir/depend:
	cd /Users/orlandoortega/Desktop/NotificationBot && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/orlandoortega/Desktop/NotificationBot /Users/orlandoortega/Desktop/NotificationBot /Users/orlandoortega/Desktop/NotificationBot /Users/orlandoortega/Desktop/NotificationBot /Users/orlandoortega/Desktop/NotificationBot/CMakeFiles/NotificationBot.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/NotificationBot.dir/depend
