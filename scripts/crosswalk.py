import pandas as pd, numpy as np, re
m=pd.read_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/master_long2.csv")

def L(row):  # normalized text incl section for sex disambiguation
    return (str(row["section"])+" || "+str(row["indicator"])).lower()
m["_L"]=m.apply(L,axis=1)

# canonical crosswalk: name -> (must_have[list], must_not[list])
CW = [
 ("Female population age 6+ who ever attended school (%)", ["age 6 years and above who ever attended school"], []),
 ("Population below age 15 years (%)", ["population below age 15 years"], []),
 ("Sex ratio of total population (f per 1000 males)", ["sex ratio of the total population"], []),
 ("Sex ratio at birth, last 5 years (f per 1000 males)", ["sex ratio at birth"], []),
 ("Households with electricity (%)", ["households with electricity"], []),
 ("Households with electricity (%)", ["living in households with electricity"], []),
 ("Households with improved drinking-water source (%)", ["improved drinking-water source"], []),
 ("Households using improved sanitation facility (%)", ["improved sanitation facility"], []),
 ("Households using clean fuel for cooking (%)", ["clean fuel for cooking"], []),
 ("Households using iodized salt (%)", ["iodized salt"], []),
 ("HH member covered by health insurance/scheme (%)", ["health insurance","scheme"], []),
 ("HH member covered by health insurance/scheme (%)", ["health scheme or health insurance"], []),
 ("Women (15-49) who are literate (%)", ["women","literate"], ["10 or more"]),
 ("Men (15-49) who are literate (%)", ["men","literate"], ["women","10 or more"]),
 ("Women (15-49) with 10+ years schooling (%)", ["women","10 or more years of schooling"], []),
 ("Men (15-49) with 10+ years schooling (%)", ["men","10 or more years of schooling"], ["women"]),
 ("Women who ever used the internet (%)", ["women","ever used the internet"], []),
 ("Men who ever used the internet (%)", ["men","ever used the internet"], ["women"]),
 ("Women 20-24 married before age 18 (%)", ["women age 20-24 years married before age 18"], []),
 ("Men 25-29 married before age 21 (%)", ["men age 25-29 years married before age 21"], []),
 ("Total fertility rate (children per woman)", ["total fertility rate"], []),
 ("Women 15-19 already mothers/pregnant (%)", ["age 15-19 years who were already mothers or pregnant"], []),
 ("Infant mortality rate (per 1000)", ["infant mortality rate"], ["neonatal"]),
 ("Under-five mortality rate (per 1000)", ["under-five mortality rate"], []),
 ("FP: Any method (%)", ["|| any method"], []),
 ("FP: Any modern method (%)", ["any modern method"], []),
 ("FP: Female sterilization (%)", ["female sterilization"], []),
 ("FP: Male sterilization (%)", ["male sterilization"], []),
 ("FP: IUD/PPIUD (%)", ["iud/ppiud"], []),
 ("FP: Pill (%)", ["|| pill"], []),
 ("FP: Condom (%)", ["|| condom"], []),
 ("Total unmet need for FP (%)", ["total unmet need"], []),
 ("Unmet need for spacing (%)", ["unmet need for spacing"], []),
 ("ANC visit in first trimester (%)", ["antenatal check-up in the first trimester"], []),
 ("ANC: 4+ visits (%)", ["at least 4 antenatal care visits"], []),
 ("Last birth protected vs neonatal tetanus (%)", ["protected against neonatal tetanus"], []),
 ("Mother took IFA 100+ days (%)", ["iron folic acid for 100 days"], []),
 ("Mother received MCP card (%)", ["mother and child protection"], []),
 ("Institutional births (%)", ["institutional births"], ["public"]),
 ("Institutional births in public facility (%)", ["institutional births in public facility"], []),
 ("Births delivered by caesarean section (%)", ["births delivered by caesarean section"], ["private","public"]),
 ("C-section in private facility (%)", ["private health facility","caesarean"], []),
 ("C-section in public facility (%)", ["public health facility","caesarean"], []),
 ("PNC for mother within 2 days (%)", ["mothers who received postnatal care"], []),
 ("Child fully immunized/vaccinated (%)", ["fully immunized"], []),
 ("Child fully vaccinated (card or recall) (%)", ["fully vaccinated based on information from either"], []),
 ("Child received BCG (%)", ["received bcg"], []),
 ("Child received 3 doses polio (%)", ["3 doses of polio"], []),
 ("Child received measles/MCV 1st dose (%)", ["measles"], ["second","24-35","fully","any vaccine"]),
 ("Child received vitamin A dose (%)", ["vitamin a dose"], []),
 ("Prevalence of diarrhoea, last 2 weeks (%)", ["prevalence of diarrhoea"], ["severe"]),
 ("Child w/ diarrhoea given ORS (%)", ["diarrhoea","oral rehydration salts"], []),
 ("Child w/ diarrhoea given zinc (%)", ["diarrhoea","received zinc"], []),
 ("Prevalence of ARI symptoms (%)", ["prevalence of symptoms of acute respiratory"], []),
 ("Child ARI/fever taken to facility (%)", ["fever or symptoms of ari","taken to a health"], []),
 ("Child breastfed within 1 hour of birth (%)", ["breastfed within one hour of birth"], []),
 ("Child <6m exclusively breastfed (%)", ["exclusively breastfed"], ["or breastfeeding"]),
 ("Child 6-8m solid/semi-solid + breastmilk (%)", ["6-8 months receiving solid"], []),
 ("Breastfed child 6-23m adequate diet (%)", ["breastfeeding children age 6-23 months receiving an adequate"], ["non-"]),
 ("Total child 6-23m adequate diet (%)", ["total children age 6-23 months receiving an adequate"], []),
 ("Children under 5 stunted (%)", ["stunted"], []),
 ("Children under 5 wasted (%)", ["wasted (weight-for-height)"], ["severely"]),
 ("Children under 5 severely wasted (%)", ["severely wasted"], []),
 ("Children under 5 underweight (%)", ["underweight (weight-for-age)"], []),
 ("Women BMI below normal (%)", ["women","below normal"], ["men"]),
 ("Men BMI below normal (%)", ["men","below normal"], ["women"]),
 ("Women overweight/obese (%)", ["women","overweight or obese"], ["men"]),
 ("Men overweight/obese (%)", ["men","overweight or obese"], ["women"]),
 ("Children 6-59m anaemic (%)", ["children age 6-59 months who are anaemic"], []),
 ("Non-pregnant women anaemic (%)", ["non-pregnant women","anaemic"], []),
 ("Pregnant women anaemic (%)", ["pregnant women","anaemic"], ["non-pregnant"]),
 ("All women 15-49 anaemic (%)", ["all women age 15-49 years who are anaemic"], []),
 ("Men 15-49 anaemic (%)", ["men age 15-49 years who are anaemic"], []),
 ("Women comprehensive knowledge HIV/AIDS (%)", ["women","comprehensive knowledge"], ["men"]),
 ("Men comprehensive knowledge HIV/AIDS (%)", ["men","comprehensive knowledge"], ["women"]),
 ("Married women participate in HH decisions (%)", ["participate in"], []),
 ("Women paid in cash for work (%)", ["worked in the last 12 months","paid in cash"], []),
 ("Women owning house/land (%)", ["owning a house and/or land"], ["households"]),
 ("Women with own bank/savings account (%)", ["bank or savings account that they themselves"], []),
 ("Women with own mobile phone (%)", ["mobile phone that they themselves"], []),
 ("Women 15-24 hygienic menstrual protection (%)", ["hygienic methods of protection"], []),
 ("Ever-married women experienced spousal violence (%)", ["experienced spousal violence"], []),
 ("Women who use any tobacco (%)", ["women","any kind of tobacco"], ["men"]),
 ("Men who use any tobacco (%)", ["men","any kind of tobacco"], ["women"]),
 ("Women who consume alcohol (%)", ["women","consume alcohol"], ["men"]),
 ("Men who consume alcohol (%)", ["men","consume alcohol"], ["women"]),
]

def has(t,sub):
    return re.search(r'(?<![a-z])'+re.escape(sub)+r'(?![a-z])', t) is not None
def match_canon(text):
    hits=[]
    for name,must,mustnot in CW:
        if all(has(text,x) for x in must) and not any(has(text,x) for x in mustnot):
            if name not in hits: hits.append(name)
    return hits

# assign: for each row, find canonical (first unique match)
def assign(text):
    h=match_canon(text)
    if not h: return None
    return h[0]
m["canonical"]=m["_L"].map(assign)

# diagnostics: ambiguous (multiple matches) per round
amb=0
for t in m["_L"].unique():
    if len(match_canon(t))>1:
        amb+=1
print("distinct texts with >1 canonical match (ambiguous):",amb)

# coverage of canonical across rounds
cov=[]
for name,_,_ in CW:
    sub=m[m["canonical"]==name]
    d={"canonical":name}
    for r in ["NFHS-3","NFHS-4","NFHS-5","NFHS-6"]:
        d[r]="Y" if (sub[sub["round"]==r]["value"].notna().any()) else ""
    d["rounds"]=sum(1 for r in ["NFHS-3","NFHS-4","NFHS-5","NFHS-6"] if d[r]=="Y")
    cov.append(d)
covdf=pd.DataFrame(cov).drop_duplicates("canonical")
print("\ncanonical indicators:",covdf.canonical.nunique())
print(covdf["rounds"].value_counts().sort_index())
print("\nmapped rows:", m["canonical"].notna().sum(),"of",len(m))
covdf.to_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/canon_coverage.csv",index=False)
m.to_csv("/sessions/sleepy-bold-wozniak/mnt/outputs/master_long3.csv",index=False)
# show any canonical with 0 rounds (bad signature)
print("\nZERO-match canonicals:")
print(covdf[covdf["rounds"]==0]["canonical"].tolist())
