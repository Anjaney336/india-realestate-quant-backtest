from pathlib import Path
import csv,collections,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).parent;out=root/'results/risk';groups=collections.defaultdict(list)
for x in csv.DictReader((root/'results/historical/ledger.csv').open()):groups[x['date'][:4]].append(float(x['net_return']))
rows=[{'year':y,'observations':len(r),'zero_return_days':sum(v==0 for v in r),'compounded_return':math.prod(1+v for v in r)-1} for y,r in sorted(groups.items())]
with (out/'annual_diagnostics.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
fig,axs=plt.subplots(1,2,figsize=(11,4));axs[0].bar([x['year'] for x in rows],[100*x['compounded_return'] for x in rows]);axs[0].set(title='Historical baseline: annual net return',ylabel='Return (%)');axs[1].bar([x['year'] for x in rows],[x['zero_return_days']/x['observations']*100 for x in rows]);axs[1].set(title='Zero-return concentration',ylabel='Zero-return observations (%)');fig.tight_layout();fig.savefig(out/'annual_diagnostics.svg');print('Published year-by-year returns and cash-period concentration; no new model tuning')

