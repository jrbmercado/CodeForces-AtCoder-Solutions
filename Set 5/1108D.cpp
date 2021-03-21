#include <string>
#include <iostream>
using namespace std;
int main() {
  int length;
  string myString;
  cin >> length;
  cin >> myString; //RBGRRBRGG
  int counter = 0;
  for(int i=0; i<length; i++){
    // If the current letter is the same as the letter behind me
    if(myString[i]==myString[i-1]){
        counter ++;
        // Change to R
        myString[i]='R';
        if(myString[i] != myString[i+1] && myString[i] != myString[i-1]){
            continue;
        }
        // Change to G
        myString[i]='G';
        if(myString[i] != myString[i+1] && myString[i] != myString[i-1]){
            continue;
        }
        // Change to B
        myString[i]='B';
        if(myString[i] != myString[i+1] && myString[i] != myString[i-1]){
            continue;
        }
    }
  }
  cout << counter << endl;
  cout << myString;
  return 0;
}