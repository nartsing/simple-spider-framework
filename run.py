#!/root/anaconda3/envs/spider/bin/python
from spider_setting import SpiderCfg
from framework import main
import json
import sys

if __name__=="__main__":
    if len(sys.argv)>1:
        plan_ind=int(sys.argv[-1])
    else:
        plan_ind=-1
    cfg=SpiderCfg("./spider_cfg.json")

    days=[
        
    ]

    main(cfg, plan_ind)

