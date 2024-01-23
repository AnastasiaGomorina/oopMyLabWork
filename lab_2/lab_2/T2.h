#ifndef T2_H
#define T2_H

#include <string>
#include <iostream>

class T2 {
private:
    std::string identifier;
    int octalValue;

public:
    T2(const std::string& id, int val);
    void showValue() const;
    T2 operator-(const T2& other) const;
    friend std::ostream& operator<<(std::ostream& os, const T2& t2);
};

#endif // T2_H
