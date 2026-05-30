import pdfplumber, re
PDF="/sessions/sleepy-bold-wozniak/mnt/NFHS-6/Fact Sheets/National Family Health Survey (NFHS-6) 2023-2024 Fact Sheets.pdf"
numre=re.compile(r'^-?\d+(?:,\d{3})*(?:\.\d+)?\+?$')
startre=re.compile(r'^(\d{1,3})\.(.*)')
CENTERS=[424,460,495,535]
COLMIN=406
CANON_STATES={
 'india':'India','andhrapradesh':'Andhra Pradesh','arunachalpradesh':'Arunachal Pradesh',
 'assam':'Assam','bihar':'Bihar','chhattisgarh':'Chhattisgarh','goa':'Goa','gujarat':'Gujarat',
 'haryana':'Haryana','himachalpradesh':'Himachal Pradesh','jharkhand':'Jharkhand','karnataka':'Karnataka',
 'kerala':'Kerala','madhyapradesh':'Madhya Pradesh','maharashtra':'Maharashtra','meghalaya':'Meghalaya',
 'mizoram':'Mizoram','nagaland':'Nagaland','odisha':'Odisha','punjab':'Punjab','rajasthan':'Rajasthan',
 'sikkim':'Sikkim','tamilnadu':'Tamil Nadu','telangana':'Telangana','tripura':'Tripura',
 'uttarpradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand','westbengal':'West Bengal',
 'andamanandnicobarislands':'Andaman and Nicobar Islands','chandigarh':'Chandigarh',
 'dadra&nagarhavelianddaman&diu':'Dadra & Nagar Haveli and Daman & Diu',
 'jammuandkashmir':'Jammu and Kashmir','ladakh':'Ladakh','lakshadweep':'Lakshadweep',
 'nctofdelhi':'NCT of Delhi','puducherry':'Puducherry'}
def canon_state(raw):
    return CANON_STATES.get(re.sub(r'\s+','',raw).lower(), re.sub(r'\s+',' ',raw).strip())
def cluster_lines(words):
    ws=sorted(words,key=lambda w:(round(w['top']),w['x0']))
    lines=[]; cur=[]; curtop=None
    for w in ws:
        if curtop is None or abs(w['top']-curtop)<=3:
            cur.append(w); curtop=w['top'] if curtop is None else curtop
        else:
            lines.append(sorted(cur,key=lambda x:x['x0'])); cur=[w]; curtop=w['top']
    if cur: lines.append(sorted(cur,key=lambda x:x['x0']))
    return lines
def parse_page(page):
    words=page.extract_words()
    lines=cluster_lines(words)
    records=[]; buffer=[]; curnum=None; last=None
    for line in lines:
        texts=[]; vals={}
        for w in line:
            c=(w['x0']+w['x1'])/2
            if c>COLMIN and numre.match(w['text']):
                col=min(range(4),key=lambda i:abs(c-CENTERS[i])); vals[col]=w['text']
            else: texts.append(w['text'])
        for t in texts:
            m=startre.match(t)
            if m and len(m.group(1))<=3:
                curnum=int(m.group(1)); buffer=[t]; last='buf'
            else:
                if last=='emitted' and curnum is not None and records and records[-1][0]==curnum:
                    records[-1][1].append(t)
                else: buffer.append(t)
        if len(vals)>=3 and curnum is not None:
            records.append([curnum,list(buffer),[vals.get(0),vals.get(1),vals.get(2),vals.get(3)]])
            buffer=[]; last='emitted'
    out=[]
    for num,lab,vals in records:
        label=' '.join(lab); m=startre.match(label)
        if m: label=m.group(2).strip()
        out.append((num,re.sub(r'\s+',' ',label).strip(),vals))
    return out
def num_to_float(s):
    if s is None: return None
    s=s.replace(',','').rstrip('+')
    try: return float(s)
    except: return None
def main():
    with pdfplumber.open(PDF) as pdf:
        blocks=[]
        for p in range(len(pdf.pages)):
            t=pdf.pages[p].extract_text() or ""
            first=t.split("\n",1)[0]
            if first.replace(" ","").endswith("-KeyIndicators"):
                name=canon_state(first.rsplit("-",1)[0])
                if blocks and blocks[-1][0]==name: blocks[-1][1].append(p)
                else: blocks.append([name,[p]])
        data={}; canon_labels={}
        for name,ps in blocks:
            recs={}
            for p in ps:
                for num,label,vals in parse_page(pdf.pages[p]):
                    recs[num]=(label,vals)
                    if name=='India' and num not in canon_labels: canon_labels[num]=label
            data[name]=recs
    return data,canon_labels
if __name__=="__main__":
    data,canon=main()
    print("states:",len(data))
    print("India indicator count:",len(data['India']))
    for num in sorted(data['India']):
        lab,vals=data['India'][num]
        print(f"{num:>3} | {lab[:78]:78} | {vals}")
