/* Multiples of 3 or 5 */
#include <iostream>

int main (int argc, char *argv[]) {
  int sumOfMultiples = 0;
  for (int i = 1; i < 1000; i++) {
    if (i % 3 == 0 || i % 5 == 0) sumOfMultiples += i;
  }
  std::cout << sumOfMultiples << std::endl;
  return 0;
}
