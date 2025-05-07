#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;


vector<vector<string> > fillBigVector ();

int main () {

	vector<vector<string> > bigVector = fillBigVector();

//////////////////////////////////////////////


	string kanye[] = {"me", "you", "she", "her", "he", "him"};
	string kanyes[] = {"my", "mine", "your", "yours", "hers", "his"};

	for (int i = 0; i < bigVector.size(); i++) {

		for (int j = 0; j < bigVector[i].size(); j++) {

			bool kanyefound = false;
			string copy = bigVector[i][j];
			tolower(copy[0]);

			for (int k = 0; k < 6; k++) {

				if (copy == kanye[k]) {

					cout << "Kanye ";
					kanyefound = true;

				}

			}

			for (int k = 0; k < 6; k++) {

				if (copy == kanyes[k]) {

					cout << "Kanye's ";
					kanyefound = true;

				} 

			}

			if (!kanyefound) {

				cout << bigVector[i][j] << ' ';

			}

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

	return(bigVector);
}
