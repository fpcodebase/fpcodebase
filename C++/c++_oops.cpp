#include <iostream>
using namespace std;

class Base {
public:
    virtual void print() { cout << "Base" << endl; }
};

class Derived : public Base {
public:
    void print() override { cout << "Derived" << endl; }
};
int main() {
    Derived d;
    Base &b = d;
    b.print();
    return 0;
}