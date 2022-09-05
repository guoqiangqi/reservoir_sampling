int main() {
  int[] reservoir = new int[m];

  // init
  for (int i = 0; i < reservoir.length; i++)
  {
      reservoir[i] = dataStream[i];
  }

  for (int i = m; i < dataStream.length; i++)
  {
      // 随机获得一个[0, i]内的随机整数
      int d = rand.nextInt(i + 1);
      // 如果随机整数落在[0, m-1]范围内，则替换蓄水池中的元素
      if (d < m)
      {
          reservoir[d] = dataStream[i];
      }
  }
}
