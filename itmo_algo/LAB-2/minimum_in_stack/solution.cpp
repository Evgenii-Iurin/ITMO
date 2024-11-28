#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class MinStack {
public:
    void push(int x) {
        elements.push(x);
        if (min_elements.empty() || x <= min_elements.top()) {
            min_elements.push(x);
        }
    }
    
    void pop() {
        if (!elements.empty() && elements.top() == min_elements.top()) {
            min_elements.pop();
        }
        elements.pop();
    }
    
    int getMin() const {
        return min_elements.top();
    }

private:
    stack<int> elements;
    stack<int> min_elements;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    MinStack minStack;
    vector<int> results;
    
    for (int i = 0; i < n; ++i) {
        int operation;
        cin >> operation;
        
        if (operation == 1) {
            int x;
            cin >> x;
            minStack.push(x);
        } else if (operation == 2) {
            minStack.pop();
        } else if (operation == 3) {
            results.push_back(minStack.getMin());
        }
    }
    
    for (int result : results) {
        cout << result << '\n';
    }

    return 0;
}
