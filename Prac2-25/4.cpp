#include <iostream>
using namespace std;

int main()
{
    int n; 
    cin >>n; 
    for(int i=1; i<=n; i++)
    {
        int y;
        cin >> y;
        int num = 0;
        if (y%4 == 0 && y%100 != 0 || y%400 == 0)
            num = 1;
        else
            num = 0;

        if (num == 0)
        {
            if (y%4 ==0 || (y-1)%4 ==0)
                cout << "Calendar for " << y << " can next be reused in " << y+6 << "." << endl;
            else
                cout << "Calendar for " << y << " can next be reused in " << y+11 << "." << endl;
        }
            
        else
            cout << "Calendar for " << y << " can next be reused in " << y+28 << "." << endl;
    }
    return 0;
}