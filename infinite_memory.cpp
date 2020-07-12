// File: HeapFunOOM-AllocationWithoutFree.cc


#include <iostream>
#include <vector>
using namespace std;


int main() {

  cout << endl << "Let's Learn by Doing!" << endl;


  int *ptr_heap = NULL;  // sizeof(int) = 4

  // Allocate roughly 4GB of integers.

  int count_to_allocate = 1000000000;

  unsigned long total_allocation = 0;
  vector<int*> v;
  

  char user_choice;


  while (user_choice != 'N') {

    // TODO(1): Allocate without handling allocation failure.

    ptr_heap = new int[count_to_allocate];
    v.push_back(ptr_heap);

    total_allocation += count_to_allocate * sizeof(int);


    // TODO(2): Uncomment code to allocate by handling failure.

    // You might have to comment above code.

    try {

      ptr_heap = new int[count_to_allocate];

      total_allocation += count_to_allocate * sizeof(int);

    } catch (const bad_alloc& e) {      

      cout << "Allocation failed: " << e.what() << endl;
      int i = 10;
      while(i){
          v.pop_back();
          i--;
      }
      

    }


    cout << "Allocated 4GB at " << ptr_heap

	 << "; Total allocation : " << total_allocation/1000000000 << " GB"

	 << "; Allocate more heap space? Y/N" << endl;


    // TODO: Uncomment to stop/observe heap growth of the program in procfs.

    cin >> user_choice;

  }

}