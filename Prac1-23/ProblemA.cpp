
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<string> inFile ();
bool detect (string input);

int main () {

	vector<string> input = inFile();
	int ordinary = 0;
	int mirrored = 0;

	for (int i = 0; i < input.size(); i++) {

		if (detect(input[i])) {

			cout << "Mirrored pair" << endl;
			mirrored++;

		}

		else {

			cout << "Ordinary pair" << endl;
			ordinary++;

		}


	}	

	cout << "Summary: " << mirrored << " Mirrored pair";
	if (mirrored != 1)
		cout << 's';

	cout << ", " << ordinary << " ordinary pair";
	if (ordinary != 1)
		cout << 's';

	cout << endl;

	return (1);

}

vector<string> inFile () {

	vector<string> output;
	string input;
	ifstream in;
	in.open("problema.txt");

	while (getline(in, input)) {

		if (input[0] == ' ' && input[1] == ' ')
			break;

		output.push_back(input);

	}

	cout << "Ready!" << endl;
	in.close();

	return (output);

}

bool detect(string input) {

	if ((input[0] == 'p' && input[1] == 'q') || (input[0] == 'q' && input[1])) {

		return (true);

	}

	else if ((input[0] == 'b' && input[1] == 'd') || (input[0] == 'd' && input [1] == 'b')) {

		return (true);

	}

	else {

		return (false);

	}

}
