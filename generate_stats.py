import datetime
# generate_stats.py
svg = f'''
<svg width="300" height="100">
  <text x="20" y="30" font-family="Arial" font-size="16" fill="#000">
    Последний коммит: aboba
  </text>
</svg>
'''
with open("stats.svg", "w") as f:
    f.write(svg)
