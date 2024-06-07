#!/bin/bash -i
conda deactivate
conda activate spider
cd /root/spider_jiaotong
/root/anaconda3/envs/spider/bin/python ./run.py 3
