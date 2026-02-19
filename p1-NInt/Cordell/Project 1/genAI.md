i. I used chatGPT. <br>
ii. Prompt:
<br>
 Will this make an array [2, 4, 8, 16, ...]:
```python
N_array=[0]
for k in range(2**10):
    N_array.append(2**k)
```
iii. Response: <br>
Not quite — it will start with **0**, then **1**, then powers of 2:

* `N_array` begins as `[0]`
* the loop appends `2**k` for `k = 0, 1, 2, ..., 1023`
* so you get: `[0, 1, 2, 4, 8, 16, ...]`

If you want `[2, 4, 8, 16, ...]`, do either:

```python
N_array = []
for k in range(1, 11):   # 1..10
    N_array.append(2**k)
```

or more compact:

```python
N_array = [2**k for k in range(1, 11)]
```

(Those examples give the first 10 terms: 2 through 1024.)
<br>
iv. I used the more compact form. <br>
v. There is nothing wrong with the generated code. There also wasn't much of anything with my code either, it just included 0 and 1. <br>
That is pretty much all I used AI for that I think you care about (its the only time I asked it about code aside from markdown syntax), but I also asked it a bunch of random stuff like how to install LaTeX, how to format a table in markdown, copy paste em dash, and what's another word for "software." So, I'll email you the chat history. 