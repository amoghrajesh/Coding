import sys

stats = {}

for line in sys.stdin:
    fields = line.strip().split(',')
    name, runs_on_ball = fields
    try:
        runs_on_ball = int(runs_on_ball)
    except ValueError:
        continue

    if name not in stats:
        stats[name] = {'runs': 0, 'balls': 0}

    stats[name]['runs'] += runs_on_ball
    stats[name]['balls'] += 1

for batsman in stats:
    st = stats[batsman]
    runs = st['runs']
    balls = st['balls']
    strike_rate = (runs / balls) * 100 if balls > 0 else 0
    print(f'{batsman}\t{strike_rate:.2f}')
