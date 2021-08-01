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
using std::endl;

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


template <typename T, typename V>
WIN_COND constexpr check_diagonals(const T& results)
{
	int i;
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

	return WIN_COND::TIE;
}


template <typename T, typename V>
inline constexpr WIN_COND evaluate(const T& results)
{
	WIN_COND x = check_rows<T, V>(results);
	return x == WIN_COND::TIE ? check_diagonals<T, V>(results) : x;
}


template <typename T, typename V>
inline constexpr std::string TicTacToe(const T& x)
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

	std::vector<std::vector<char>> x =
	{
	{'X','O','O'},
	{'O','O','X'},
	{'X','O','X'}
	};

	// Print result of game
	cout << TicTacToe<std::vector<std::vector<char>>, std::vector<char>>(x) << endl;

	return 0;
}

