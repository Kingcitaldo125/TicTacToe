// Inspired by: https://edabit.com/challenge/rscwis53jKokoKRYo
#include <iostream>
#include <string>
#include <vector>


namespace TTT {
	enum class WIN_COND
	{
		TIE = 0, O, X
	};
}


using std::cout;

using TTT::WIN_COND;


template <typename T, typename V>
WIN_COND constexpr check_rows(const T& results)
{
	int O = 0;
	int X = 0;
	typename T::const_iterator it;
	for (it = results.begin(); it != results.end(); ++it)
	{
		const auto& sub_arr = *it;
		typename V::const_iterator itt;
		int nx = 0;
		int no = 0;
		int c = 0;
		for (itt = sub_arr.begin(); itt != sub_arr.end(); ++itt)
		{
			const char& chr = *itt;
			if (c == 0 && chr == 'O')
				++O;
			if (c == 0 && chr == 'X')
				++X;

			if (chr == 'O')
				++no;
			if (chr == 'X')
				++nx;

			if (nx >= 3)
			{
				return WIN_COND::X;
			}
			if (no >= 3)
			{
				return WIN_COND::O;
			}
			++c;
		}
		if (X >= 3)
		{
			return WIN_COND::X;
		}
		if (O >= 3)
		{
			return WIN_COND::O;
		}
	}

	return WIN_COND::TIE;
}


template <typename T>
WIN_COND constexpr check_cols(const T& results)
{
	for (int i = 0; i < results.size(); ++i)
	{
		typename T::const_iterator it;
		int nx = 0;
		int no = 0;
		for (it = results.begin(); it != results.end(); ++it)
		{
			auto row = *it;
			const char& chr = row.at(i);

			if (chr == 'O')
				++no;
			if (chr == 'X')
				++nx;
		}
		if (nx >= 3)
		{
			return WIN_COND::X;
		}
		if (no >= 3)
		{
			return WIN_COND::O;
		}
	}

	return WIN_COND::TIE;
}


template <typename T>
WIN_COND constexpr check_diagonals(const T& results)
{
	int i,j;
	int X = 0;
	int O = 0;
	std::string res;
	for (i = 0; i < 3; ++i)
	{
		auto val = results.at(i).at(i);
		if (val == 'X')
			++X;
		if (val == 'O')
			++O;
	}

	if (X >= 3)
		return WIN_COND::X;
	if (O >= 3)
		return WIN_COND::O;

	X = 0;
	O = 0;
	for (i = 2; i >= 0; --i)
	{
		for (j = 0; j < 3; ++j)
		{
			auto val = results.at(i).at(j);
			if (val == 'X')
				++X;
			if (val == 'O')
				++O;
		}
	}

	if (X >= 3)
		return WIN_COND::X;
	if (O >= 3)
		return WIN_COND::O;

	return WIN_COND::TIE;
}


template <typename T, typename V>
constexpr WIN_COND evaluate(const T& results)
{
	WIN_COND x = check_rows<T, V>(results);
	WIN_COND y = check_cols<T>(results);

	if (x == WIN_COND::TIE && y == WIN_COND::TIE)
		return check_diagonals<T>(results);
	else if(x == WIN_COND::TIE && y != WIN_COND::TIE)
		return y;
	else if(y == WIN_COND::TIE && x != WIN_COND::TIE)
		return x;

	return WIN_COND::TIE;
}


template <typename T, typename V>
constexpr std::string TicTacToe(const T& x)
{
	auto res = evaluate<T,V>(x);
	switch (res)
	{
	case WIN_COND::TIE:
		return "It's a tie";
	case WIN_COND::X:
		return "Player 1 wins";
	case WIN_COND::O:
		return "Player 2 wins";
	default:
		return "";
	}
}


int main(int argc, char** argv)
{
	// Player 1 X
	// Player 2 O

	using vecchar = std::vector<char>;
	using vecvecchar = std::vector<vecchar>;

	vecvecchar x =
	{
	{'X','O','X'},
	{'O','O','X'},
	{'O','X','X'}
	};

	// Print result of game
	cout << TicTacToe<vecvecchar, vecchar>(x) << '\n';

	return 0;
}
