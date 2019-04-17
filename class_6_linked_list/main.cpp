#include <iostream>
#include "linked_list.cpp"
using namespace std;

int main()
{
    BSTree testTree;
    int inputKey; // 입력받을 키값
    char cmd; // 명령어 문자

    cout << endl << "Commands:" << endl;
    cout << "  +key : Insert element" << endl;
    cout << "  ?key : Retrieve element" << endl;
    cout << "  -key : Remove element" << endl;
    cout << "  Q    : Quit the test program" << endl;
    cout << endl;

    do
    {
        testTree.showStructure();

        cout << endl << "Command: ";
        cin >> cmd;
        if (cmd == '+' || cmd == '?' ||
            cmd == '-' || cmd == '<')
            cin >> inputKey;

        switch (cmd)
        {
            case '+':
                cout << "Insert : key = " << inputKey
                << endl;
                testTree.insert(inputKey);
                break;

            case '?':
                cout << "Retrieve : key = " << inputKey
                << endl;
                testTree.retrieve(inputKey);
                break;

            case '-':
                cout << "Remove : key = " << inputKey
                << endl;
                testTree.remove(inputKey);
                break;

            case 'Q': case 'q':
                break;

            default:
                cout << "Inactive or invalid command" << endl;
        }
    } while ((cmd != 'Q') && (cmd != 'q'));

}
