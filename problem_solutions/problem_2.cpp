/* Even Fibonacci Numbers */
#include <iostream>

void updateElements(int &el1, int &el2) {
  int temp = el2;
  el2 = el2 + el1;
  el1 = temp;
}

int main (int argc, char *argv[]) {
  int firstElement = 1;
  int secondElement = 2;
  int sumOfEvenValuatedTerms = 2;
  while (secondElement < 4000000) {
    updateElements(firstElement, secondElement);
    if (secondElement % 2 == 0) sumOfEvenValuatedTerms += secondElement;
  }
  std::cout << sumOfEvenValuatedTerms << std::endl;
  return 0;
}
