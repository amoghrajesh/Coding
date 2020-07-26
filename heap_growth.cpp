#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    int *a = (int*)malloc(sizeof(int)*5);
    for(int i=0;i<5;i++){
       cin >> a[i];
    }
    for(int i=1;i<10;i++){
       cout << a[i] << "\n";
    }
    return 0;
}