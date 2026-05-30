import pandas as pd, numpy as np, re
m=pd.read_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/master_long.csv")

# ---- canonical state names ----
SMAP={
 "Andaman & Nicobar Islands":"Andaman and Nicobar Islands",
 "Maharastra":"Maharashtra","Chattisgarh":"Chhattisgarh",
 "Jammu & Kashmir":"Jammu and Kashmir","Delhi":"NCT of Delhi",
 "Dadra and Nagar Haveli & Daman and Diu":"Dadra & Nagar Haveli and Daman & Diu",
}
m["state_std"]=m["state"].replace(SMAP)

# ---- indicator normalization ----
def norm(t):
    if not isinstance(t,str): return ""
    s=t.lower().strip()
    s=s.replace("≥",">=").replace("≤","<=").replace("–","-").replace("—","-").replace("’","'")
    s=re.sub(r"(\d),(\d{3})",r"\1\2",s)              # 1,000 -> 1000
    s=re.sub(r"([a-z\)])\d{1,2}(?:,\s*\d{1,2})*\b",r"\1",s)  # strip footnote superscripts
    s=s.replace("(%)","").replace("( %)","")
    s=re.sub(r"\bwomen age 15-49 years\b","women",s)
    s=re.sub(r"\bmen age 15-49 years\b","men",s)
    s=re.sub(r"\(age 15-49 years\)","",s)
    s=re.sub(r"\(currently married women age 15-49 years\)","",s)
    s=re.sub(r"\bfamily planning\b","fp",s)
    s=re.sub(r"[^a-z0-9><=./-]+"," ",s)
    s=re.sub(r"\s+"," ",s).strip()
    return s
# key uses section(Women/Men hint) + indicator for blood sugar/hypertension disambiguation
def sexhint(sec,ind):
    blob=(str(sec)+" "+str(ind)).lower()
    if "blood sugar" in blob or "elevated blood pressure" in blob or "hypertension" in blob or "mm of hg" in blob:
        if re.search(r"\bmen\b",blob) and "women" not in re.sub(r"\bmen\b","",blob): pass
    return ""
def mkkey(row):
    k=norm(row["indicator"])
    sec=str(row["section"]).lower()
    # add women/men prefix for BP/sugar where label omits it
    if ("blood sugar" in sec or "hypertension" in sec) and not re.match(r"(wo)?men",k):
        if "women" in sec or sec.endswith("- women"): k="women "+k
        elif " men" in sec or sec.endswith("- men"): k="men "+k
    return k
m["nkey"]=m.apply(mkkey,axis=1)

# ---- harmonized id per nkey ----
keys=sorted(m["nkey"].unique())
hid={k:f"H{n+1:03d}" for n,k in enumerate(keys)}
m["harmonized_id"]=m["nkey"].map(hid)

m.to_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/master_long2.csv",index=False)

# ---- coverage matrix ----
rep=(m.groupby("nkey").agg(harmonized_id=("harmonized_id","first")).reset_index())
def rep_label(k):
    sub=m[m["nkey"]==k]
    for r in ["NFHS-6","NFHS-5","NFHS-4","NFHS-3"]:
        s=sub[sub["round"]==r]
        if len(s): return s["indicator"].iloc[0], s["section"].iloc[0]
    return "",""
cov_rows=[]
for k in keys:
    sub=m[m["nkey"]==k]
    lbl,sec=rep_label(k)
    d=dict(harmonized_id=hid[k], section=sec, indicator=lbl)
    for r,short in [("NFHS-3","N3"),("NFHS-4","N4"),("NFHS-5","N5"),("NFHS-6","N6")]:
        sr=sub[sub["round"]==r]
        has = (sr["value"].notna().any())
        d[r]="Y" if has else ("·" if len(sr) else "")
    d["rounds_covered"]=sum(1 for r in ["NFHS-3","NFHS-4","NFHS-5","NFHS-6"] if d[r]=="Y")
    cov_rows.append(d)
cov=pd.DataFrame(cov_rows).sort_values(["rounds_covered","harmonized_id"],ascending=[False,True])
cov.to_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/coverage.csv",index=False)

print("total harmonized indicators:",len(keys))
print("covered in all 4 rounds:", (cov["rounds_covered"]==4).sum())
print("in 3 rounds:", (cov["rounds_covered"]==3).sum())
print("in 2 rounds:", (cov["rounds_covered"]==2).sum())
print("in 1 round:", (cov["rounds_covered"]==1).sum())
print("\nSample 4-round indicators:")
for _,r in cov[cov.rounds_covered==4].head(20).iterrows():
    print(" ",r["harmonized_id"],"|",r["indicator"][:70])
