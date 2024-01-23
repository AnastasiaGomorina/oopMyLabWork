#include "T2.h"
#include <iostream>
#include <iomanip>

T2::T2(const std::string& id, int val) : identifier(id), octalValue(val) {}

void T2::showValue() const {
    std::cout << "T2 " << identifier << ": " << std::oct << octalValue << std::dec << std::endl;
}

T2 T2::operator-(const T2& other) const {
    int resultValue = octalValue - other.octalValue;
    return T2(identifier, resultValue);
}

std::ostream& operator<<(std::ostream& os, const T2& t2) {
    os << "T2 " << t2.identifier << ": " << std::oct << t2.octalValue << std::dec;
    return os;
}
