#include "Factory.h"

T1 Factory::createT1(const std::string& identifier, const std::string& value) {
    return T1(identifier, value);
}

T2 Factory::createT2(const std::string& identifier, int octalValue) {
    return T2(identifier, octalValue);
}

void Factory::deleteObject(void* obj) {
}