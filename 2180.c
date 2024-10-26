int countEven(int num)
{
    int quantity = 0;
    for (int countdown = num; countdown > 0; countdown--)
    {
        if (sumDigits(countdown) % 2 == 0) quantity++;
    }
    return quantity;
}

int sumDigits(int number)
{
    int sum = 0;
    while (number != 0)
    {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}