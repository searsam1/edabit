//
#include<cmath>

bool isNarcissistic(int n) {
  	int size = std::to_string(n).length(), res=0, temp=0;
  	int nCopy = n;
	  while (n > 0){
		temp = pow(n%10, size);
		res += temp;
		n /= 10;
	  }	
  	return res == nCopy;
}
//