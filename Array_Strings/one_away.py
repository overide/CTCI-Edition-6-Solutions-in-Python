# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

def isOneAway(string1,string2):
	str1_len = len(string1)
	str2_len = len(string2)
	if abs(str1_len-str2_len) <= 1:
		if str1_len > str2_len:
			string1,string2 = string2,string1

		if str1_len != str2_len:
			difference = 0;i=0;j=0
			min_len = min(str1_len,str2_len)
			while(i <= min_len-1):
				if string1[i] != string2[j]:
					difference += 1
					j += 1
				else:
					i += 1; j += 1

				if difference > 1:
					return False
		else:
			difference = 0
			for i, ch in enumerate(string1):
				if string2[i] != ch:
					difference += 1

				if difference > 1:
					return False

	return True

def main():
	str1,str2 = input().strip(' ').split(' ')
	print(isOneAway(str1,str2))

main()