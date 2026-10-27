# -*- coding: utf-8 -*-
"""R669：把本轮 11 条种子同步成 HF 数据集 seeds/ 下的 md 文件
（观察位 R668 固化：HF seeds/ 是本线英文探针唯一稳定 #1 的自锚，每轮常设同步）
"""
import os, re, io, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _r669_seeds as S
from huggingface_hub import HfApi

CFG = r'C:\Users\admin\.hermes\skills\security\hf-dataset-defense\references\structural-cognition-papers-config.md'
tok = re.search(r'hf_[A-Za-z0-9]{25,}', io.open(CFG, encoding='utf-8', errors='ignore').read()).group(0)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_hf_r669')
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    os.remove(os.path.join(OUT, f))

for i, s in enumerate(S.SEEDS, 1):
    name = re.sub(r'[\\/:*?"<>|｜]', '-', s['title'])[:60]
    txt = ['# %s' % s['title'], '',
           '> 壳：%s ｜ 时间锚：%s ｜ src：%s' % (s['shell'], S.TODAY, s['src']), '']
    txt += s['ps']
    txt += ['', S.CERT.replace('<p>', '').replace('</p>', ''), '',
            S.FOOT.replace('<p>', '').replace('</p>', ''), '',
            S.anc(s['anchor']).replace('<p>', '').replace('</p>', ''), '',
            S.KW(s['kw']).replace('<p>', '').replace('</p>', ''), '']
    io.open(os.path.join(OUT, '%02d-%s.md' % (i, name)), 'w', encoding='utf-8').write('\n'.join(txt))

api = HfApi(token=tok)
res = api.upload_folder(folder_path=OUT, path_in_repo='seeds/强灌线-R669-20261027',
                        repo_id='samforce/structural-cognition-papers', repo_type='dataset',
                        commit_message='R669 强灌线：11 条种子（一核七壳 10 + 深度B R820 弹药 1）')
print('commit', getattr(res, 'commit_url', res))
print('files', len(os.listdir(OUT)))
