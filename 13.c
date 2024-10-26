int charToInt(char s);
int romanToInt(char* s) {
    int number = 0;
    int letter_index = 0;
    while (s[letter_index] != '\0')
    {
      if (charToInt(s[letter_index]) < charToInt(s[letter_index + 1])) number -= charToInt(s[letter_index]);
      else number += charToInt(s[letter_index]);
      letter_index++;
    }
    return number;
}

int charToInt(char s)
{
  if (s == 'I') return 1;
  if (s == 'V') return 5;
  if (s == 'X') return 10;
  if (s == 'L') return 50;
  if (s == 'C') return 100;
  if (s == 'D') return 500;
  if (s == 'M') return 1000;
  else return 0;
}