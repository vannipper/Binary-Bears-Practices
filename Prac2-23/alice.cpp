#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool hasBeenReached(int check, vector<bool> num);

int main () {

	string win = "";
	getline(cin, win);

	vector<bool> num;
	int A = 0;
	int B = 0;

	for (int i = 0; i < win.size(); i++) {

		num.push_back(false);

	}


	for (int i = 0; i < win.size(); i++) {

		if (win[i] == 'A') {

			A++;

			if (hasBeenReached(A, num)) {

				num[A-1] = true;
				cout << A + ' ';

			}

		}

		else {

			B++;

			if (hasBeenReached(B, num)) {

				num[B-1] = true;

			}
		}

	}

	cout << endl;

	return (0);
}

bool hasBeenReached (int check, vector<bool> num) {

	if (num[check-1] == false)
		return (true);

}
