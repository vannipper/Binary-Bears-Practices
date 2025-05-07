#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

vector<vector<int> > fillBigVector();

int main () {

	vector<vector<int> > bigVector = fillBigVector();

///////////////////////////////////////////////////

	for (int i = 0; i < bigVector.size(); i++) {

		int j = bigVector[i][2] / 100;	// century
		int k = bigVector[i][2] % 100;	// year within century
		int m = bigVector[i][0];	// month
		int q = bigVector[i][1];	// day

		int h = (q + ((26*(m + 1)) / 10) + k + (k/4) + (j/4) + (5*j)) % 7; // day of week
		string dayOfWeek;

		if (h == 0)

			dayOfWeek = "Saturday";

		else if (h == 1)

			dayOfWeek = "Sunday";

		else if (h == 2)

			dayOfWeek = "Monday";

		else if (h == 3)

			dayOfWeek = "Tuesday";

		else if (h == 4)

			dayOfWeek = "Wednesday";

		else if (h == 5)

			dayOfWeek = "Thursday";

		else

			dayOfWeek = "Friday";


		int dayOfYear = 0;
		bool nextMonth = true;

		if (m == 1) {

			dayOfYear += q;
			nextMonth = false;

		}

		else

			dayOfYear += 31;

		if (m == 2 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (k % 4 == 0 && nextMonth)

			dayOfYear += 29;

		else if (nextMonth)

			dayOfYear += 28;

		if (m == 3 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 31;

		if (m == 4 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 30;

		if (m == 5 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 31;
	
		if (m == 6 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 30;

		if (m == 7 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 31;

		if (m == 8 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 31;

		if (m == 9 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 30;

		if (m == 10 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 31;

		if (m == 11 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}

		else if (nextMonth)

			dayOfYear += 30

;
		if (m == 12 && nextMonth) {

			dayOfYear += q;
			nextMonth = false;

		}


		cout << m << '/' << q << '/' << j << k << " is a " << dayOfWeek << " and the " << dayOfYear;

		if (dayOfYear % 10 == 1)

			cout << "st";

		else if (dayOfYear % 10 == 2)

			cout << "nd";

		else if (dayOfYear % 10 == 3)

			cout << "rd";

		else

			cout << "th";

		cout << " day of the year." << endl;

		

	}


	return (0);
}

vector<vector<int> > fillBigVector() {

	vector<vector<int> > bigVector;
	int numOfLines; //tweak
	char delimeter = '/'; //tweak


	string initializeInput = "";
	getline(cin, initializeInput);
	numOfLines = atoi(initializeInput.c_str());


	for (int i = numOfLines; i > 0; i--) {

		vector<int> smallVector;
		string tempInput = "";
		getline (cin, tempInput);

		while (!tempInput.empty()) {

			string tempInsert;

			if (tempInput.find(delimeter) == -1) { // if on the last rotation of inner while loop

				tempInsert = tempInput;
				tempInput.clear();

			}

			else {

				tempInsert = tempInput.substr(0, tempInput.find(delimeter));
				tempInput = tempInput.substr(tempInput.find(delimeter) + 1);

			}

			int integerInsert = atoi(tempInsert.c_str());
			smallVector.push_back(integerInsert);

		}

		bigVector.push_back(smallVector);

	}

/*
	for (int i = 0; i < bigVector.size(); i++) {

		for (int j = 0; j < bigVector[i].size(); j++) {

			cout << bigVector[i][j] << ' ';

		}

		cout << endl;

	}
*/

	return(bigVector);

}
