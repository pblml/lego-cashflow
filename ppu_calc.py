import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PayPerUse():

    def __init__(self, acq_cost=288000, ref_quantity = 300, interest=0.025,  profit_pu=800, term=6, lower_bound=0.5):
        self.acq_cost = acq_cost
        self.term = term
        self.monthly_interest = (np.power(1+interest, (1/12))-1)
        self.ref_quantity = ref_quantity
        self.lower_bound = lower_bound*ref_quantity
        self.redemption_pa = self.acq_cost/term
        self.redemption_pu = (self.redemption_pa/12)/self.ref_quantity
        self.profit_pu = profit_pu

    def calc(self, log_file, fixed_rate=4000):
        df = pd.read_csv(log_file)
        valid_log = ["run", "counter"]
        if False:
            print(f"columns should be {valid_log}")
            return
        res_df = df[["run", "counter"]]
        res_df["redemption_pu"] = self.redemption_pu
        res_df["redemption_rate"] = [c*r if c>=self.lower_bound else self.lower_bound*r for c, r in zip(res_df["counter"], res_df["redemtion_pu"])]
        res_df["remaining_debt"] = [self.acq_cost - sum(res_df["redemtion_rate"][:i]) for i in range(len(res_df))]
        #!! FORMEL FÜR DIE ZINSBERECHNUNG FALSCH
        res_df["interest"] = res_df["remaining_debt"]*self.monthly_interest
        res_df["monthly_liability"] = res_df["redemtion_rate"]+res_df["interest"]
        res_df["turnover"] = self.profit_pu*res_df["counter"]
        res_df["profits"] = res_df["turnover"]-res_df["redemtion_rate"]
        res_df["profits_fixed_rate"] = res_df["turnover"]-fixed_rate
        self.df = res_df
        return self

    def plot(self, x="run", y1=["remaining_debt"], y2=["counter"]):
        ax1 = self.df.plot(x=x, y=y1)
        self.df.plot(x=x, y=y2, secondary_y=True, ax=ax1)
        plt.show()

    def save(self, filename="result.csv"):
        self.df.to_csv(filename)
    
    def __str__(self):
        return(str(self.df.append(self.df.sum(numeric_only=True), ignore_index=True)))

ppu = PayPerUse()
ppu.calc("log.csv").save("test_log_result.csv")
print(ppu)
ppu.df.plot(x="run", y=["profits", "profits_fixed_rate"], kind="bar")
plt.show()