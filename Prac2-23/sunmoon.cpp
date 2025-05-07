#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

int main () {

	vector<vector<int> > bigVector;
	// vector<vector<string> > bigVector;
	int numOfLines = 2; //tweak
	char delimeter = ' '; //tweak

/*
	string initializeInput = "";
	getline(cin, initializeInput);
	numOfLines = atoi(initializeInput.c_str());
*/

	for (int i = numOfLines; i > 0; i--) {

		vector<int> smallVector;
		// vector<string> smallVector;
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
			// smallVector.push_back(tempInsert);

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

/////////////////////////////////////////////////////////////////////////

	int sunstart, sunmod;
	int moonstart, moonmod;

	sunstart = bigVector[0][0];
	sunmod = bigVector[0][1];
	moonstart = bigVector[1][0];
	moonmod = bigVector[1][1];

 	bool ecl = false;
	int years = -1;

	while (!ecl) {

		if ( (sunstart % sunmod == 0) && (moonstart % moonmod == 0)) {

			ecl = true;

		}

		sunstart++;
		moonstart++;
		years++;

	}

	cout << years << endl;

	return (0);
}
