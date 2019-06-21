#include <string>
#pragma once
#ifndef EXPORT_H_
#define EXPORT_H_

class Export {

    public:
        Export(std::string nameOfFile);
        void writeToFile(const std::string data[], size_t dataLen);

    private:
        std::string fileName;
        
};

#endif 