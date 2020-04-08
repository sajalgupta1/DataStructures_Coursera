#include<bits/stdc++.h>
using namespace std;


int main()
{
    int q;
    cin>>q;
    stack<int> maxst;
    // stack<int> st;
    int maxi = INT_MIN;
    while(q--)
    {
        string s;
        cin>>s;
        if(s=="push")
        {
            string val;
            cin>>val;
            int val_int = stoi(val);
            if(maxi<val_int)
            {
                maxst.push(val_int);
                maxi = val_int;
            }
            else{
                maxst.push(maxi);
            }

        }
        else if(s=="pop")
        {
            maxst.pop();

        }
        else if(s=="max"){
            if(maxst.size()!=0)
            {
                cout<<maxst.top()<<endl;
            }

        }   
    }
    return 0;
}