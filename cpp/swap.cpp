#include<iostream>
using namespace std;

int main(){

    int a=5;
    int b=7;


    // # using xor operation
    // a=a^b;
    // b=a^b;
    // a=a^b;

//     Step-by-step XOR operation (bitwise explanation)
// XOR (^) works as follows:

// 0 ^ 0 = 0
// 1 ^ 1 = 0
// 0 ^ 1 = 1
// 1 ^ 0 = 1
// Now, perform XOR on each bit from a = 5 (0101) and b = 3 (0011).

// Bit Position	a (0101)	b (0011)	XOR Result (a ^ b)
// Bit 3 (leftmost)	0	0	0
// Bit 2	1	0	1
// Bit 1	0	1	1
// Bit 0 (rightmost)	1	1	0


    //  using addition 
    a=a+b;
    b=a-b;
    a=a-b;

    cout<<a <<endl;
    cout<<b;

    return 0;
}