#ifndef FACTORY_H
#define FACTORY_H

#include "T1.h"
#include "T2.h"

class Factory {
public:
    static T1 createT1(const std::string& identifier, const std::string& value);
    static T2 createT2(const std::string& identifier, int octalValue);
    static void deleteObject(void* obj);
};

#endif // FACTORY_H
