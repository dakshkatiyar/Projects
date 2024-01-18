#include <iostream>
using namespace std;

class person
{
public:
    string name;
    int numPayments;
    int pays[20];
    int totalDone;
    int ledger[10][10]; //[2,4] means 2 dega 4 ko
};

int main()
{
    cout<< "*********************\n";
    int n; // no. of people
    cout << "Enter the number of people\n";
    cin >> n;

    person p[n + 1];

    for (int i = 1; i <= n; i++)
    {

        cout << "Enter name of person " << i << endl;
        cin >> p[i].name;
    }

    for (int i = 1; i <= n; i++) // each person paying
    {
        cout << "Enter no. of payment done by " << p[i].name << endl;
        cin >> p[i].numPayments;

        p[i].totalDone = 0;

        for (int j = 1; j <= p[i].numPayments; j++) // num of payments by a person
        {
            cout << "Enter payment " << j << endl;
            cin >> p[i].pays[j];
            p[i].totalDone += p[i].pays[j];
        }
        cout << "Total payment " << i << " is " << p[i].totalDone << endl;
    }

    for (int i = 1; i <= n; i++)
    {
        int perPerson = p[i].totalDone / n; // division of money per person by 1 person
        for (int j = 1; j <= n; j++)
        {
            if (i != j)
            {
                p[j].ledger[j][i] = perPerson;
            }
        }
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (i != j)
            {
                int net = p[i].ledger[i][j] - p[j].ledger[j][i];
                if (net > 0)
                {
                    cout << p[i].name << " will give " << p[j].name << " " << net << endl;
                }

                else
                {
                    cout << p[j].name << " will give " << p[i].name << " " << -net << endl;
                }
            }
        }
    }

    return 0;
}