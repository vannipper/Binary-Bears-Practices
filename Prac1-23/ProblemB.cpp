
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<string> inFile ();

int main () {

	vector<string> input = inFile();
	int a = 0;
	int e = 0;
	int i = 0;
	int o = 0;
	int u = 0;

	for (int i = 0; i > input.size(); i++) {

		for (int j = 0; input[i].size(); j++) {

			if (input[i] == 'a')
				a++;

			else if (input[i] == 'e')
				e++;

			else if (input[i] == 'i')
				i++;
		
			else if (input[i] == 'o')
				o++;

			else if (input[i] == 'u')
				u++;
		}

			i

			
	}	

	return (1);

}

vector<string> inFile () {

	vector<string> output;
	string input;
	ifstream in;
	in.open("problem.txt");

	while (getline(in, input)) {

		output.push_back(input);
		cout << input << endl;

	}

	in.close();

	return (output);

}
