def job_schedule(jobs):
  jobs.sort(key = lambda x:x[1], reverse = True)
  max_deadline = max(jobs, key = lambda x:x[2])[2]
  slot = [False] * max_deadline
  profit = 0
  n = len(jobs)

  for i in range(n):
    deadline = jobs[i][2] - 1
    
    while deadline>=0 and slot[deadline]:
      deadline = deadline - 1
      
    if deadline>=0:
      slot[deadline] = True
      profit += jobs[i][1]
    
  return profit

jobs = [(1, 50, 2), (2, 10, 1), (3, 20, 2), (4, 30, 1), (5, 40, 3)]
print(job_schedule(jobs))
