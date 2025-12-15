#ifndef RINGBUFFER_H_
#define RINGBUFFER_H_

#include <iostream>
using namespace std;

template<class T>

class RingBuffer {
    private:
        int m_pos;
        int m_size;
        T *m_values;

    public:
        class Iterator;

    public:
        RingBuffer(int size): m_pos(0), m_size(size), m_values(NULL) {
            m_values = new T[size];
        }

        ~RingBuffer() {
            delete [] m_values;
        }

        int size() {
            return m_size;
        }

        void add(T value) {
            m_values[m_pos++] = value;

            if(m_pos == m_size) {
                m_pos = 0;
            }
        }

        T &get(int pos) {
            return m_values[pos];
        }
};

#endif
