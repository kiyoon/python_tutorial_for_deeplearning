# cProfile

```python
python -m cProfile [-s tottime] myscript.py
```

# line_profiler

```bash
pip install line_profiler
```

Add `@profile` decorator to Python functions.

```bash
kernprof -l -v myscript.py
```

In order to view it again,  
```bash
python -m line_profiler myscript.py.lprof
```
