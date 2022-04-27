x = """
- English
This is typewriter effect in cmd

- Indonesia
Ini adalah efek typewriter di cmd


                        -- Juan --
"""
import time
for i in x:
    print(i, end="", flush=True)
    time.sleep(0.05)
