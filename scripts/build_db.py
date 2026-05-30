import re, json, pandas as pd, numpy as np
import sys
sys.path.insert(0,'/sessions/sleepy-bold-wozniak/mnt/outputs')
from parse_nfhs6 import main as parse6, num_to_float

FS="/sessions/sleepy-bold-wozniak/mnt/NFHS-6/Fact Sheets/"

# ---------- NFHS-6 section map by indicator number ----------
SEC6=[(1,11,"Population and Household Profile"),
(12,15,"Characteristics of Adults (age 15-49 years)"),
(16,19,"Marriage and Fertility"),
(20,24,"Current Use of Family Planning Methods (currently married women age 15-49 years)"),
(25,27,"Unmet Need for Family Planning (currently married women age 15-49 years)"),
(28,34,"Maternal and Child Health - Antenatal Care"),
(35,40,"Maternal and Child Health - Delivery Care"),
(41,43,"Maternal and Child Health - Postnatal Care"),
(44,56,"Child Vaccinations and Vitamin A Supplementation"),
(57,60,"Treatment of Childhood Diseases (children under age 5 years)"),
(61,73,"Child Feeding Practices and Nutritional Status of Children"),
(74,77,"Nutritional Status of Adults (age 15-49 years)"),
(78,80,"Blood Sugar Level among Adults (age 15+) - Women"),
(81,83,"Blood Sugar Level among Adults (age 15+) - Men"),
(84,86,"Hypertension among Adults (age 15+) - Women"),
(87,89,"Hypertension among Adults (age 15+) - Men"),
(90,94,"Women's Empowerment (women age 15-49 years)"),
(95,97,"Gender Based Violence (age 18-49 years)"),
(98,101,"Tobacco Use and Alcohol Consumption among Adults (age 15+)")]
def sec6(n):
    for a,b,s in SEC6:
        if a<=n<=b: return s
    return ""

UNIT_CUT=re.compile(r'(.*?\((?:%|children per woman|number of children per woman|per 1,?000 live births|Rs\.?)\))')
def clean6(lbl):
    m=UNIT_CUT.match(lbl)
    if m: return m.group(1).strip()
    return lbl.strip()

# ---------- parse NFHS-6 ----------
data6,canon=parse6()
rows=[]
canon_clean={n:clean6(l) for n,l in canon.items()}
for state,recs in data6.items():
    for num,(lbl,vals) in recs.items():
        clbl=canon_clean.get(num, clean6(lbl))
        for area,raw in zip(["Urban","Rural","Total"],vals[:3]):
            rows.append(dict(state=state,round="NFHS-6",year="2023-24",area=area,
                             section=sec6(num),indicator=clbl,ind_no=num,
                             value_raw=raw,value=num_to_float(raw),source="NFHS-6 PDF"))
df6=pd.DataFrame(rows)
print("NFHS-6 rows:",len(df6),"states:",df6.state.nunique(),"indicators:",df6.indicator.nunique())

# ---------- NFHS-5 xls ----------
x5=pd.read_excel(FS+"NFHS_5_Factsheets_Data.xls")
idcols=["States/UTs","Area"]
indcols=[c for c in x5.columns if c not in idcols]
m5=x5.melt(id_vars=idcols,value_vars=indcols,var_name="indicator",value_name="value")
m5=m5.rename(columns={"States/UTs":"state"})
m5["round"]="NFHS-5"; m5["year"]="2019-21"; m5["source"]="NFHS-5 xls"
m5["indicator"]=m5["indicator"].str.strip().str.replace(r"\s+"," ",regex=True)
def tofloat(v):
    if pd.isna(v): return None
    if isinstance(v,(int,float)): return float(v)
    s=str(v).replace(",","").replace("(","").replace(")","").strip()
    if s.upper() in ("NA","","*","-"): return None
    try: return float(s)
    except: return None
m5["value_num"]=m5["value"].map(tofloat)
m5["section"]=""
df5=m5[["state","round","year","area","section","indicator","value","value_num","source"]].copy() if "area" in m5 else None
m5=m5.rename(columns={"Area":"area"})
df5=pd.DataFrame(dict(state=m5["state"],round=m5["round"],year=m5["year"],area=m5["area"],
                      section="",indicator=m5["indicator"],ind_no=np.nan,
                      value_raw=m5["value"].astype(str),value=m5["value_num"],source=m5["source"]))
print("NFHS-5 rows:",len(df5),"states:",df5.state.nunique(),"indicators:",df5.indicator.nunique())

# ---------- NFHS-4 & 3 sparse xlsx ----------
x43=pd.read_excel(FS+"NFHS-4 and 3 Fact Sheets Sparse.xlsx")
x43=x43.rename(columns={"India/States/UTs":"state","Survey":"round","Area":"area"})
indcols43=[c for c in x43.columns if c not in ("state","round","area") and not str(c).startswith("Note of")]
m43=x43.melt(id_vars=["state","round","area"],value_vars=indcols43,var_name="indfull",value_name="value")
def split_sec(s):
    if " - " in s:
        a,b=s.split(" - ",1); return a.strip(),b.strip()
    return "",s.strip()
secind=m43["indfull"].map(split_sec)
m43["section"]=[a for a,b in secind]; m43["indicator"]=[b for a,b in secind]
m43["value_num"]=m43["value"].map(tofloat)
m43["year"]=m43["round"].map({"NFHS-4":"2015-16","NFHS-3":"2005-06"})
m43["source"]="NFHS-4/3 sparse xlsx"
df43=pd.DataFrame(dict(state=m43["state"],round=m43["round"],year=m43["year"],area=m43["area"],
                       section=m43["section"],indicator=m43["indicator"],ind_no=np.nan,
                       value_raw=m43["value"].astype(str),value=m43["value_num"],source=m43["source"]))
print("NFHS-4/3 rows:",len(df43),"states:",df43.state.nunique(),
      "indicators:",df43.indicator.nunique(),"rounds:",sorted(df43["round"].unique()))

# ---------- combine ----------
master=pd.concat([df6,df5,df43],ignore_index=True)
# drop rows that are entirely empty value AND came from sparse NA? keep all (blanks meaningful) but drop where value_raw nan-ish for sparse
master["value_raw"]=master["value_raw"].replace({"nan":None,"None":None})
master.to_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/master_long.csv",index=False)
print("\nMASTER rows:",len(master))
print(master.groupby("round").agg(rows=("value","size"),nonnull=("value","count"),
      states=("state","nunique"),inds=("indicator","nunique")))
