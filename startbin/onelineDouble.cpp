#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

double stringToDouble (string input);
vector<vector<double> > fillBigVector ();

int main () {

	vector<vector<double> > bigVector = fillBigVector();

///////////////////////////////////////





	return (0);
}

vector<vector<double> > fillBigVector () {

	vector<vector<double> > bigVector = fillBigVector();
	int numOfLines = 1; //tweak
	char delimeter = ' '; //tweak

	for (int i = numOfLines; i > 0; i--) {

		vector<double> smallVector;
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

			double doubleInsert = stringToDouble(tempInsert);
			smallVector.push_back(doubleInsert);

		}

		bigVector.push_back(smallVector);

	}

	for (int i = 0; i < bigVector.size(); i++) {

		for (int j = 0; j < bigVector[i].size(); j++) {

			cout << bigVector[i][j] << ' ';

		}

	}

}

double stringToDouble(string input) {

	int decimalIndex = input.find('.');

	for (int i = decimalIndex; i >= 0; i==) {

		if (decimalIndex ==

	}


	return (doubleOut);

}

