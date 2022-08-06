import math
from fractions import Fraction
import sys
import subprocess
from pyfiglet import Figlet
from termcolor import colored


def ar_pr():
	subprocess.call("clear", shell=True)
	f = Figlet()
	print(f.renderText('arpr_seeker'))
	print(colored('1)Find the term', 'green'))
	print(colored('2)Find the common difference', 'green'))
	print(colored('3)Find the sum of the terms', 'green'))
	print(colored('99)EXIT', 'red'))
	option = input(colored('Choose an option: ', 'green'))

	if option == '1':
		a1 = input(colored('Input term of arithmetic progression: ', 'green'))
		d = input(colored('Input the common difference: ', 'green'))
		an = input(colored('Input the index of the term to be found: ', 'green'))
		res = int(a1) + int(d) * (int(an) - 1)
		print(colored(str(a1) + ' + ' + str(d) + '*' + '( ' + str(an) + ' - 1) = ' + str(res), 'yellow'))

		answer = input(colored('Continue?(y/n)', 'green'))
		if answer == 'y':
			ar_pr()
		if answer == 'n':
			subprocess.call('clear', shell=True)
			sys.exit(0)

	if option == '2':
		an = input(colored('Input a term of arithmetic progression: ', 'green'))
		ak = input(colored('Input a term of arithmetic progression: ', 'green'))
		n = input(colored('Input a index of ' + an + ': ', 'green'))
		k = input(colored('Input a index of ' + ak + ': ', 'green'))
		s = Fraction(int(an) - int(ak),  int(n) - int(k))
		math.exp(s)
		print(colored('(' + str(an) + ' - ' + str(ak) + ') / (' + str(n) + ' - ' + str(k) + ') ' + ' = ' + str(s), 'yellow'))

		answer = input(colored('Continue?(y/n)', 'green'))
		if answer == 'y':
			ar_pr()
		if answer == 'n':
			subprocess.call('clear', shell=True)
			sys.exit(0)

	if option == '3':
		n = int(input(colored('Input a index of S(sum): ', 'green')))
		a1 = int(input(colored('Input a first term of a progression: ', 'green')))
		d = int(input(colored('Input a common difference of progression: ', 'green')))
		x = Fraction(2 * a1 + d * (n - 1), 2)
		math.exp(x)
		res = x * n
		print(colored(res, 'yellow'))

		answer = input(colored('Continue?(y/n)', 'green'))
		if answer == 'y':
			ar_pr()
		if answer == 'n':
			subprocess.call('clear', shell=True)
			sys.exit(0)

try:

	ar_pr()

except OverflowError and ValueError:
	print("Something went wrong...")
