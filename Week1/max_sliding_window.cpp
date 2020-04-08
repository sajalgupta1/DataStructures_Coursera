#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void max_sliding_window_naive(vector<int> const & arr, int k) {
    // Create a Double Ended Queue, Qi that will store indexes of array elements 
    // The queue will store indexes of useful elements in every window and it will 
    // maintain decreasing order of values from front to rear in Qi, i.e., 
    // arr[Qi.front[]] to arr[Qi.rear()] are sorted in decreasing order 
    std::deque<int> Qi(k); 
    int n = arr.size();
    /* Process first k (or first window) elements of array */
    int i; 
    for (i = 0; i < k; ++i) { 
        // For every element, the previous smaller elements are useless so 
        // remove them from Qi 
        while ((!Qi.empty()) && arr[i] >= arr[Qi.back()]) 
            Qi.pop_back(); // Remove from rear 
  
        // Add new element at rear of queue 
        Qi.push_back(i); 
    } 
  
    // Process rest of the elements, i.e., from arr[k] to arr[n-1] 
    for (; i < n; ++i) { 
        // The element at the front of the queue is the largest element of 
        // previous window, so print it 
        cout << arr[Qi.front()] << " "; 
  
        // Remove the elements which are out of this window 
        while ((!Qi.empty()) && Qi.front() <= i - k) 
            Qi.pop_front(); // Remove from front of queue 
  
        // Remove all elements smaller than the currently 
        // being added element (remove useless elements) 
        while ((!Qi.empty()) && arr[i] >= arr[Qi.back()]) 
            Qi.pop_back(); 
  
        // Add current element at the rear of Qi 
        Qi.push_back(i); 
    } 
  
    // Print the maximum element of last window 
    cout << arr[Qi.front()]; 
    /*int m = A[0];
    vector<int> arr;
    for(int i = 0;i<w;i++)
        arr.push_back(A[i]);
    make_heap(arr.begin(),arr.end());
    cout<<arr.front()<<" ";
    for(int i=w;i<A.size();i++)
    {
        auto it = find(arr.begin(),arr.end(),A[i-w]);
        arr.erase(it);
        arr.push_back(A[i]);
        make_heap(arr.begin(),arr.end());
        cout<<arr.front()<<" ";
    }*/
    /*priority_queue <int> window;
    for (int i = 0;i<w;i++)
    {
        window.push(A[i]);
    }
        cout << window.top() << " ";
    window.remove();
    for(int i = w;i<A.size();i++)
    {
        window.push(A[i]);
        cout<<window.top()<<" ";
        window.remove();
    }*/
    return;
}


int main() {
    int n = 0;
    cin >> n;

    vector<int> A(n);
    for (int i = 0; i < n; ++i)
        cin >> A.at(i);

    int w = 0;
    cin >> w;

    max_sliding_window_naive(A, w);

    return 0;
}
