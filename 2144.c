int minimumCost(int* cost, int costSize)
{
  // This time Counting Sort comes again to save the day
  int final_price = 0;

  // Trivial case
  if (costSize == 1 || costSize == 2)
  {
    for (int i = 0; i < costSize; i++) final_price += cost[i];
    return final_price;
  }

  // find max
  int max = 0;
  for (int candy = 0; candy < costSize; candy++)
  {
    if (cost[candy] > max) max = cost[candy];
  }

  int* count = calloc(max + 1, sizeof(int));
  int* sorted_cost = calloc(costSize, sizeof(int));

  // count elements
  for (int candy = 0; candy < costSize; candy++)
  {
    count[cost[candy]]++;
  }

  // cumulative count
  for (int i = 1; i <= max; i++)
  {
    count[i] += count[i - 1];
  }

  // sort
  for (int i = 0; i < costSize; i++)
  {
    sorted_cost[count[cost[i]] - 1] = cost[i];
    count[cost[i]]--;
  }

  // Now with sorted list go in reverse
  int element = 1;
  for (int candy = costSize - 1; candy >= 0; candy--)
  {
    if (element == 1 || element == 2) 
    {
      final_price += sorted_cost[candy];
      element++;
    }
    else
    {
      element = 1;
    }
  }
  free(count);
  free(sorted_cost);
  return final_price;
}