#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main () {

	int n;
	int m;
	string input1;

	getline(cin, input1);

	n = atoi(input1.c_str());
	m = atoi(input1.substr(input1.find(' ')).c_str());

	int city[n][m];
/*
	city[0][0] = 1;
	city[0][1] = 2;
	city[1][0] = 3;
	city[1][1] = 4;
*/

	string input2;

	for (int i = 0; i < n; i++) {

		getline(cin, input2);

		for (int j = 0; j < m; j++) {

			int pop = atoi(input2.c_str());
			city[i][m] = pop;

			input2 = input2.substr(find(' '));

		}

	}


	int bigcost = -1;

	for (int i = 0; i < n; i++) {

		//cout << "loop 1" << endl;

		for (int j = 0; j < m; j++) { //store location

		//cout << "loop 2" << endl;

			int tempbigcost = 0;

			for (int k = 0; k < n; k++) {

			//cout << "loop 3" << endl;

				for (int l = 0; l < m; l++) { //templocation

					//cout << "loop 4" << endl;

					tempbigcost += city[k][l] * (abs(i-k) + abs(j-l));

				}


			}

			if (tempbigcost < bigcost || bigcost < 0) {

				bigcost = tempbigcost;

			}

		}

	}

	cout << bigcost << endl;

	return (0);
}
