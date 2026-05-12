
#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
using namespace std;

struct Simplex {
	int m, n; // m constraints, n original variables
	vector<vector<double>> T; // tableau (m+1) x (n+m+1) last col is RHS
	double eps = 1e-9;

	Simplex(const vector<vector<double>>& A, const vector<double>& b, const vector<double>& c) {
		m = (int)A.size();
		n = (int)c.size();
		int cols = n + m; // original vars + slack vars
		T.assign(m + 1, vector<double>(cols + 1, 0.0));

		// Fill constraint rows
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) T[i][j] = A[i][j];
			T[i][n + i] = 1.0; // slack variable
			T[i][cols] = b[i]; // RHS
		}

		// Objective row: maximize c^T x -> put -c in objective row for simplex
		for (int j = 0; j < n; ++j) T[m][j] = -c[j];
		T[m][cols] = 0.0;
	}

	int pivotCol() {
		int cols = (int)T[0].size() - 1;
		int best = -1;
		double mostNeg = -eps;
		for (int j = 0; j < cols; ++j) {
			if (T[m][j] < mostNeg) {
				mostNeg = T[m][j];
				best = j;
			}
		}
		return best;
	}

	int pivotRow(int col) {
		int best = -1;
		double minRatio = 1e300;
		for (int i = 0; i < m; ++i) {
			double a = T[i][col];
			if (a > eps) {
				double ratio = T[i].back() / a;
				if (ratio < minRatio - eps || (abs(ratio - minRatio) < eps && a > 0)) {
					minRatio = ratio;
					best = i;
				}
			}
		}
		return best;
	}

	void doPivot(int row, int col) {
		double pivot = T[row][col];
		int cols = (int)T[0].size();
		for (int j = 0; j < cols; ++j) T[row][j] /= pivot;
		for (int i = 0; i <= m; ++i) if (i != row) {
			double factor = T[i][col];
			for (int j = 0; j < cols; ++j) T[i][j] -= factor * T[row][j];
		}
	}

	pair<vector<double>, bool> solve() {
		int cols = (int)T[0].size() - 1;
		while (true) {
			int col = pivotCol();
			if (col == -1) break; // optimal
			int row = pivotRow(col);
			if (row == -1) return {{}, false}; // unbounded
			doPivot(row, col);
		}

		// Extract solution for original variables (first n columns)
		vector<double> x(n, 0.0);
		for (int j = 0; j < n; ++j) {
			int oneRow = -1;
			for (int i = 0; i < m; ++i) {
				if (abs(T[i][j] - 1.0) < eps) {
					bool isUnit = true;
					for (int k = 0; k < m; ++k) if (k != i && abs(T[k][j]) > eps) { isUnit = false; break; }
					if (isUnit) { oneRow = i; break; }
				}
			}
			if (oneRow != -1) x[j] = T[oneRow].back();
			else x[j] = 0.0;
		}

		return {x, true};
	}
};

int main() {
	// Maximizar z = 3 x1 + 2 x2
	vector<vector<double>> A = {{1,1}, {2,1}};
	vector<double> b = {4, 5};
	vector<double> c = {3, 2};

	Simplex solver(A, b, c);
	auto res = solver.solve();
	vector<double> x = res.first;
	bool ok = res.second;
	if (!ok) {
		cout << "Problema sin acotación o sin solución óptima.\n";
		return 1;
	}

	double z = 0.0;
	for (size_t i = 0; i < x.size(); ++i) z += x[i] * c[i];

	cout << "Estado: Solución óptima encontrada\n";
	for (size_t i = 0; i < x.size(); ++i) cout << "x" << (i+1) << " = " << x[i] << "\n";
	cout << "Valor máximo de Z = " << z << "\n";
	return 0;
}
