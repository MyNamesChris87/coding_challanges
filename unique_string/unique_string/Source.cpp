#include <iostream>
#include <string>

using namespace std;

bool checkUniqueStr(string str) {
	for (int i = 0; i < str.size() - 1; i++) {
		for (int j = i + 1; j < str.size(); j++) {
			if (str[i] == str[j]) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	string str = "awndfjuvbhirag";

	bool sol = checkUniqueStr(str);

	if (sol) {
		cout << "pass" << endl;
	}
	else {
		cout << "fail" << endl;
	}

	return 0;
}