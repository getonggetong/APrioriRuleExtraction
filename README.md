A-Priori Association Rule Extraction
=====================

Tong Ge (tg2473)

Yi Wang (yw2580)

##Files Hierachy
![Files](img/FILES.png)


####(a) Which NYC Open Data data set(s) you used to generate the INTEGRATED-DATASET file; 
NYC City Hall Library Publications
"Official publications submitted by city agencies in electronic format to the City Hall Library, also available at http://nyc.gov/html/records/html/govpub/home.shtml "


Row number: 4929

URL:
https://data.cityofnewyork.us/Recreation/NYC-City-Hall-Library-Publications/ei8e-zggc

####(b) What (high- level) procedure you used to map the original NYC Open Data data set(s) into your INTEGRATED-DATASET file. The explanation should be detailed enough to allow us to recreate your INTEGRATED-DATASET file exactly from scratch from the NYC Open Data site.

Nothing

####(c) What makes your choice of INTEGRATED-DATASET file interesting (in other words, justify your choice of NYC Open Data data set(s)).


###How to run

```
> cd src
> ./run.sh -o output -s min_sup -c min_conf -d dataset 

usage: Main.py [-h] [-S MIN_SUP] [-C MIN_CONF] [-D CSVDATA] [-O OUTPUT]

<Usage> 

optional arguments:
  -h, --help            show this help message and exit
  -S MIN_SUP, -s MIN_SUP
                        <min_support>
  -C MIN_CONF, -c MIN_CONF
                        <min_confidence>
  -D CSVDATA, -d CSVDATA
                        <dataset file name>
  -O OUTPUT, -o OUTPUT  <stdout or file>
```
e.g., 
![example](img/example.png)

In default, the program will execute our INTEGRATED-DATASET.csv with min_support=0.2, min_confidence=0.8 and the result will be list in the terminal.


###Internal Design
You must explain in the README file precisely what variation(s)you have implemented and why

Internally, we implemented the algorithm desribed in Section 2.1 of the Agrawal and Srikant paper in VLDB 1994 with minor modications. Our pseudocode, similar to section 2.1.1 are given below, here we omit the internal function of ```apriori-gen``` and ```FILTER```.

**Pseudocode**
```
L1 = {large 1-itemsets};
Answer[0] = L1
k=2;
while(Answer.length >= k-1)
{
	Lk_1 = Answer[k-2]; 
	Ck = apriori-gen(L);
	Lk = FILTER(Ck);
	if(Lk!=NULL)
	{
		Answer.append(Lk);
	}
}
```
In particular, instead of scanning transcations over and over again in ```apriori-gen``` procedure. We always maintain inverse words list data structure, in which we place the words or words sequences as key, their corresponding apperance transcations as value. So that we only have to compare, intersect, merge the **transaction lists** to performance certain operations. e.g., the sample inverse words list:

![sample](img/sample.png)


