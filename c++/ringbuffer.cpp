#include <iostream>
#include "ringbuffer.h"
using namespace std;

int main() {
    RingBuffer<string> textring(6);
    textring.add("one");
    textring.add("two");
    textring.add("three");
    textring.add("four");
    textring.add("five");
    textring.add("six");
    textring.add("seven");
    textring.add("eight");
    textring.add("nine");

    for (int i = 0; i < textring.size(); i++) {
        cout << textring.get(i) <<endl;
    }
    
    return 0;
    
}