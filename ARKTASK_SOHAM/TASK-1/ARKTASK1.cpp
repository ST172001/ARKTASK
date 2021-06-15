#include <bits/stdc++.h>

#include <iostream>

#include <thread>

#include <chrono>
using namespace std::chrono;

using namespace std;
const int sizen = 1000;
long long costMatrixA[sizen][sizen];
long long costMatrixB[sizen][sizen];
long long productMat[sizen][sizen];

//Simple recursion which returns the minimum cost of going from i,j to n,n
long long minA[sizen][sizen] = {0};
long long maxB[sizen][sizen] = {0};
int n = sizen - 1; /* reduce cal in loop */
void cal_min_A()

{
/* cal for row n-1 and col n-1 to reduce condition checking */
int i, j, x, y;
minA[n][n] = costMatrixA[n][n];
for (i = n - 1; i >= 0; i--)
{
minA[n][i] = costMatrixA[n][i] + minA[n][i + 1];
minA[i][n] = costMatrixA[i][n] + minA[i + 1][n];
}
/* cal for all the rest cell */
int cnt = 1;
for (i = n - 1; i >= 0; i--)
{
x = n - 1;
y = i;
for (j = 0; j < cnt; j++)
{
minA[x][y] = costMatrixA[x][y] + min(minA[x + 1][y], minA[x][y + 1]);
x--;
y++;
}
cnt++;
}
cnt = n - 1;
for (i = n - 2; i >= 0; i--)
{
x = i;
y = 0;
for (j = 0; j < cnt; j++)
{
minA[x][y] = costMatrixA[x][y] + min(minA[x + 1][y], minA[x][y + 1]);
x--;
y++;
}
cnt--;
}
}
void cal_max_B()
{
/* cal for row n-1 and col n-1 to reduce condition checking */
int i, j, x, y;
maxB[n][n] = costMatrixB[n][n];
for (i = n - 1; i >= 0; i--)
{
maxB[n][i] = costMatrixB[n][i] + maxB[n][i + 1];
maxB[i][n] = costMatrixB[i][n] + maxB[i + 1][n];
}
/* cal for all the rest cell */
int cnt = 1;
for (i = n - 1; i >= 0; i--)
{
x = n - 1;
y = i;
for (j = 0; j < cnt; j++)
{
maxB[x][y] = costMatrixB[x][y] + max(maxB[x + 1][y], maxB[x][y + 1]);
x--;
y++;
}
cnt++;
}
cnt = n - 1;

for (i = n - 2; i >= 0; i--)
{
x = i;
y = 0;
for (j = 0; j < cnt; j++)
{
maxB[x][y] = costMatrixB[x][y] + max(maxB[x + 1][y], maxB[x][y + 1]);
x--;
y++;
}
cnt--;
}
}
// void cal_four_col(int row, int col)
// {
// for (int i = 0; i < 4; i++)
// {
// for (int k = 0; k < sizen; k++)
// productMat[row][col + i] += minA[row][k] * maxB[k][col + i];
// }
// }
void cal_product_mat_row(int row)
{
for (int i = 0; i < sizen; i++)
{
for (int k = 0; k < sizen; k++)
{
productMat[row][i] += minA[row][k] * maxB[k][i];
}
}
}
int main()
{
srand(time(0));
// freopen("testcase.txt", "r", stdin);
// freopen("result.txt", "w", stdout);
int i, j, k;
// initialisation
for (i = 0; i < sizen; i++)
{
for (j = 0; j < sizen; j++)
{

costMatrixA[i][j] = 1 + rand() % 1000;
costMatrixB[i][j] = 1 + rand() % 1000;
productMat[i][j] = 0;
}
}
auto start = high_resolution_clock::now();
cal_min_A();
cal_max_B();
for (i = 0; i < sizen; i++)
{
// for (j = 0; j < sizen; j++)
// {
// thread t(cal_four_col, i, j);
// t.join();
// }
thread t(cal_product_mat_row, i);
t.join();
}
//filter of size 4 x n

printf("Minimun cost from (0, 0) to (X, Y) is %ld\n", minA[n][n]);
printf("Maximun cost from (0, 0) to (X, Y) is %ld\n", maxB[0][0]);
auto stop = high_resolution_clock::now();
auto duration = duration_cast<microseconds>(stop - start);
cout << "Calculate time is "<< duration.count() << "ms\n";
return 0;}
