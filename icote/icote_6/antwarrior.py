a = [1,3,1,5,4]
cache = [0] * len(a)
def antwarrior(array, N):
  global cache
  if cache[N] != 0: return cache[N]
  if N == 0:
    cache[0] = array[0]
    return cache[0]
  if N == 1:
    cache[1] = max(array[0], array[1])
    return cache[1]
  cache[N] = max(antwarrior(array,N - 1), antwarrior(array,N - 2) + array[N])
  return cache[N]

print(antwarrior(a, len(a) - 1 ))
print(cache)
