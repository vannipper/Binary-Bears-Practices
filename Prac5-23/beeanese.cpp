#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;

vector<vector<string> > fillBigVector ();

int main () {

	vector<vector<string> > bigVector = fillBigVector();

//////////////////////////////////////////////

	for (int i = 0; i < bigVector.size(); i++) {

		int zcounter = 0;
		string buzzbuild = "";

		for (int j = 0; j < bigVector[i].size(); j++) {

			for (int k = 0; k < bigVector[i][j].size(); k++) {

				bool lastz = true;

				switch (bigVector[i][j][k]) {

					case 'a':

					case 'A':

					case 'e':

					case 'E':

					case 'i':

					case 'I':

					case 'o':

					case 'O':

					case 'u':

					case 'U':

						buzzbuild += "Buzz!Buzz!";
						break;

					case 'z':

					case 'Z':

						zcounter++;
						buzzbuild += "bzz";

						for (int a = k+1; a < bigVector[i][j].size(); a++) {

							if (bigVector[i][j][a] == 'z') {

								lastz = false;
								break;

							}

						}

						if (lastz) {

							for (zcounter; zcounter > 0; zcounter--) {

								buzzbuild += "Buzz!";

							}

						}
						break;

					default:

						buzzbuild += "Buzz!";
						break;
						


				}

			}

		}

	cout << buzzbuild << endl;
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

	return (bigVector);

}
