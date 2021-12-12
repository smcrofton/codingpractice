#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>

using namespace std;

class PracticeFunctions {
    public:
        //Classic FizzBuzz to get re-familiarized with some C++ basic syntax
        void fizzBuzz(int count){
            int i = 1;

            while (i <= count){
                string fizzBuzz = "";

                if (i % 3 == 0){ fizzBuzz += "Fizz"; }
                if (i % 5 == 0){ fizzBuzz += "Buzz"; }

                cout << fizzBuzz << endl;
                i++;
            }
        }

};

 
int main()
{
    PracticeFunctions Instance;
    Instance.fizzBuzz(15);

    return 0;
}