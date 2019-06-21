#include <iostream>
#include <fstream>
#include "../include/export.h"

Export::Export(std::string nameOfFile)
{
    this->fileName = nameOfFile;
}

void Export::writeToFile(const std::string data[], size_t dataLen)
{
    std::ofstream file (this->fileName+".txt");
    if(file.is_open()) {

        for(int i = 0; i < dataLen; i++) {
            file << data[i] << std::endl;
        }

        file.close();
        
    } else {
        //TODO: change for custom made error
        throw std::invalid_argument("File could not be opened");
    }
}