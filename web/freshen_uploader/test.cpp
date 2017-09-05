#include <bits/stdc++.h>

using namespace std;

int main() {
  int n; cin >> n;
  vector<int> A(n);
  for(auto &a:A) cin >> a;
  sort(A.begin(), A.end());
  for(auto a:A) cout << a << endl;
}
