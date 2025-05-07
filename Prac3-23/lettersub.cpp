#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

vector<vector<string> > fillBigVector ();

int main () {

	vector<vector<string> > bigVector = fillBigVector();

//////////////////////////////////////////////

	for (int i = 1; i < bigVector.size(); i++) {

		char characterArray[26];

		if ( (i%2 == 1) ) {

			if (bigVector[i].size() %2 == 1) {

				cout << "Wut" << endl;

			}

			else {

				for (int a = 0; a < 26; a++) {

					characterArray[a] = '0';

				}

				for (int b = 0; b < bigVector[i].size(); b += 2) {

					char tempChar = tolower(bigVector[i][0][b]);
					characterArray[tempChar-'a'] = tolower(bigVector[i][0][b+1]);

				}

			}

		}

	//////////////////// REPLACING

		for (int j = 0; j < bigVector[i-1].size(); j++) {

			for (int k = 0; k < bigVector[i-1][j].size(); k++) {

				if (characterArray[tolower(bigVector[i-1][j][k])-'a'] != '0') {

					bigVector[i][j][k] = characterArray[tolower(bigVector[i-1][j][k])-'a'];

				}
			}

			cout << bigVector[i][j] << ' ';

		}

	cout << endl;

}


	return (0);
}

vector<vector<string> > fillBigVector () {

	vector<vector<string> > bigVector;
	int numOfLines; //tweak
	char delimeter = ' '; //tweak

	string initializeInput = "";
	getline(cin, initializeInput);
	numOfLines = atoi(initializeInput.c_str());
	numOfLines *= 2;


	for (int i = numOfLines; i > 0; i--) {

		vector<string> smallVector;
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

			smallVector.push_back(tempInsert);

		}

		bigVector.push_back(smallVector);

	}

/*
	for (int i = 0; i < bigVector.size(); i++) {

		for (int j = 0; j < bigVector[i].size(); j++) {


			cout << bigVector[i][j] << ' ';

		}

	}
*/

	return (bigVector);

}
