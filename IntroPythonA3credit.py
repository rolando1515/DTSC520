#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1 = ["one", 1, 1.0]

q2 = ["two", 2, 2.0]
q2[1] = "dos"
Q2 = q2

q3 =["three", 3, 3.0]
q3.append("tres")
Q3 = q3

q4a = ["four", 4, 4.0]
q4b = ["eight", 8, 8.0, "ocho"]
q4a.extend(q4b)
Q4 = q4a

q5a = ["five", 5]
q5b = ["nine", 9, 9.0, "nueve"]
q5a.append(q5b)
Q5 = q5a

Q6 = len(q5b)

Q7 = q5b*3

I = len(Q5)
Q8 = Q5[I-1]

