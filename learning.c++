#include <iostream>

using namespace std;

class Employee {

public:
    string Name;
    string Company;
    int Age;

    void introduction() {

        cout<<"Name - " << Name <<endl;
        cout<<"Age - " << Age <<endl;
        cout<<"Company - " << Company <<endl;

    }
};

int main() {
    int value = 12;
    // cout <<value;
    
    Employee employeeOne;
    employeeOne.Name = 'Rahul';
    employeeOne.Company = 'SIG';
    employeeOne.Age = 32;

    // cout<<"\nAge of Employee is: "<< employeeOne.Age << endl;

    employeeOne.introduction();
}