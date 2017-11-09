import csv 

# Identify Med Orders that string match to a list of anticancer drugs, grouped by presense or absense of RxNorm codes.


# Function: getMedWhiteListSet
# Description: Returns a unique, lowercase list of medications
# Arguments: 
#       - medList : List of medications

def getMedWhiteListSet(medList):
    fooMedWhiteList = []
    for drug in medList:
        n = str(drug).lower()
        fooMedWhiteList.append(n)

    medWhiteList = set(fooMedWhiteList)
    return medWhiteList


# Function: stringMatchDrug
# Description: Returns a list where the first item is the total number of med orders.  The second item in the list is a dictionary of medication orders from drugList and respective count of those med orders. 
# Arguments: 
#       - drugList : List of medications created from getMedWhiteListSet
#       - description : List of medication orders

def stringMatchDrug(drugList,description):
    matches_dic = {}
    match_list = []
    medOrderCount = 0
    for drug in drugList:
        for medOrder in description:
            medOrderLower = medOrder.lower()
            if drug in medOrderLower:
                match_list.append(medOrderLower)
                medOrderCount += 1
    matches_dic = {x:match_list.count(x) for x in match_list}
    return [medOrderCount, matches_dic]

# Function: parseStringMatchList
# Description: Parses the output from stringMatchDrug
# Arguments: 
#       - stringMatchList : List of medications
#       - num : Number in the list to parse.  
#               * If num = 0, then the Med Order Count of the dictionary is returned.
#               * If num = 0, then the dictionary will print a pipe delimited list of med order description and respective count

def parseStringMatchList(stringMatchList,num):
    if num == 0:
        return stringMatchList[0]
    if num == 1:
        for k,v in sorted(stringMatchList[1].items()):
            print k,"|",v
        return
    else:
        pass

# Parse the CSV file into two lists:
# 1. Med Orders that have RxNorm codes
# 2. Med Orders that do not have RxNorm codes - includes drugs that do not med link in Syapse

File_Name = raw_input("CSV File Name: ")
RXNORM_CODE_Row = input("RXNORM_CODE Column: ")
DESCRIPTION_Row = input("DESCRIPTION Column: ")

medDescription_dic = {}
none_descriptions = []
has_description = []
row_count = -1
count = 0

with open(File_Name, 'rU') as fin:
    reader = csv.reader(fin)
    for row in reader:
        row_count += 1
        RXNORM_CODE = row[RXNORM_CODE_Row]
        DESCRIPTION = row[DESCRIPTION_Row]
        if RXNORM_CODE == "None" or RXNORM_CODE == "":
            none_descriptions.append(DESCRIPTION) # List of med orders that do not have RxNorm codes
            count += 1
        else:
            has_description.append(DESCRIPTION) # List of med orders names that have RxNorm codes


# ATC drug list is from Syapse Medications where ATC = L
atcListInitial = [
    "abarelix",
    "abatacept",
    "abetimus",
    "abiraterone",
    "Aclarubicin",
    "adalimumab",
    "ado-trastuzumab emtansine",
    "Afatinib",
    "afelimomab",
    "aflibercept",
    "albinterferon alfa-2b",
    "Aldesleukin",
    "alefacept",
    "alemtuzumab",
    "alitretinoin",
    "Altretamine",
    "Aminoglutethimide",
    "Aminolevulinic Acid",
    "amrubicin",
    "Amsacrine",
    "anagrelide",
    "anakinra",
    "anastrozole",
    "ancestim",
    "antilymphocyte immunoglobulin (horse)",
    "antithymocyte immunoglobulin (rabbit)",
    "apremilast",
    "arsenic trioxide",
    "ASPARAGINASE",
    "axitinib",
    "Azacitidine",
    "Azathioprine",
    "balugrastim",
    "basiliximab",
    "BCG Vaccine",
    "begelomab",
    "belatacept",
    "belimumab",
    "belinostat",
    "bendamustine",
    "bevacizumab",
    "bexarotene",
    "bicalutamide",
    "Bleomycin",
    "blinatumomab",
    "bortezomib",
    "bosutinib",
    "brentuximab vedotin",
    "briakinumab",
    "brodalumab",
    "Buserelin",
    "Busulfan",
    "cabazitaxel",
    "cabozantinib",
    "canakinumab",
    "capecitabine",
    "Carboplatin",
    "carboquone",
    "carfilzomib",
    "carmofur",
    "Carmustine",
    "catumaxomab",
    "cediranib",
    "cepeginterferon alfa-2b",
    "ceritinib",
    "certolizumab pegol",
    "cetuximab",
    "Chlorambucil",
    "Cisplatin",
    "Cladribine",
    "clofarabine",
    "cridanimod",
    "crizotinib",
    "Cyclophosphamide",
    "Cytarabine",
    "dabrafenib",
    "Dacarbazine",
    "Daclizumab",
    "Dactinomycin",
    "dasatinib",
    "dasiprotimut-T",
    "Daunorubicin",
    "decitabine",
    "degarelix",
    "demecolcine",
    "denileukin diftitox",
    "Diethylstilbestrol",
    "dinutuximab",
    "docetaxel",
    "Doxorubicin",
    "eculizumab",
    "Edrecolomab",
    "efalizumab",
    "efaproxiral",
    "enzalutamide",
    "Epirubicin",
    "eribulin",
    "erlotinib",
    "Estramustine",
    "Etanercept",
    "Ethinyl Estradiol",
    "Ethoglucid",
    "Etoposide",
    "everolimus",
    "exemestane",
    "Filgrastim",
    "fingolimod",
    "fludarabine",
    "Fluorouracil",
    "fluorouracil, combinations",
    "Flutamide",
    "formestane",
    "fosfestrol",
    "fotemustine",
    "fulvestrant",
    "gefitinib",
    "gemcitabine",
    "gemtuzumab",
    "gestonorone",
    "glatiramer acetate",
    "golimumab",
    "Goserelin",
    "gusperimus",
    "histamine dihydrochloride",
    "histrelin",
    "hydroxyurea",
    "Ibrutinib",
    "Idarubicin",
    "idelalisib",
    "Ifosfamide",
    "imatinib",
    "immunocyanin",
    "infliximab",
    "interferon alfa natural",
    "Interferon Alfa-2a",
    "Interferon Alfa-2b",
    "Interferon Alfa-n1",
    "interferon alfacon-1",
    "Interferon beta-1a",
    "interferon beta-1b",
    "Interferon Type II",
    "Interferon-beta",
    "ipilimumab",
    "irinotecan",
    "ixabepilone",
    "ixazomib",
    "lapatinib",
    "leflunomide",
    "lenalidomide",
    "lenograstim",
    "lentinan",
    "lenvatinib",
    "letrozole",
    "Leuprolide",
    "lipegfilgrastim",
    "Lomustine",
    "lonidamine",
    "mannosulfan",
    "masitinib",
    "Masoprocol",
    "Mechlorethamine",
    "Medroxyprogesterone",
    "Megestrol",
    "melanoma vaccine",
    "Melphalan",
    "mepolizumab",
    "mercaptopurine",
    "Methotrexate",
    "methyl 5-aminolevulinate",
    "mifamurtide",
    "miltefosine",
    "Mitobronitol",
    "mitoguazone",
    "Mitomycin",
    "Mitotane",
    "Mitoxantrone",
    "molgramostim",
    "Muromonab-CD3",
    "Mycophenolic Acid",
    "natalizumab",
    "necitumumab",
    "nelarabine",
    "nilotinib",
    "nilutamide",
    "nimustine",
    "nintedanib",
    "nivolumab",
    "obinutuzumab",
    "oblimersen",
    "ofatumumab",
    "olaparib",
    "omacetaxine mepesuccinate",
    "Oprelvekin",
    "oxaliplatin",
    "Paclitaxel",
    "paclitaxel poliglumex",
    "palbociclib",
    "panitumumab",
    "panobinostat",
    "pazopanib",
    "pegademase bovine",
    "pegaspargase",
    "pegfilgrastim",
    "peginterferon alfa-2a",
    "peginterferon alfa-2a, combinations",
    "peginterferon alfa-2b",
    "peginterferon alfa-2b, combinations",
    "peginterferon beta-1a",
    "pembrolizumab",
    "pemetrexed",
    "Pentostatin",
    "pertuzumab",
    "pidotimod",
    "Pipobroman",
    "Pirarubicin",
    "pirfenidone",
    "pixantrone",
    "Plerixafor",
    "Plicamycin",
    "poly I:C",
    "poly ICLC",
    "polyestradiol phosphate",
    "polyplatillen",
    "pomalidomide",
    "ponatinib",
    "porfimer sodium",
    "Pralatrexate",
    "Prednimustine",
    "Procarbazine",
    "raltitrexed",
    "ramucirumab",
    "ranimustine",
    "regorafenib",
    "ridaforolimus",
    "rilonacept",
    "rituximab",
    "romidepsin",
    "roquinimex",
    "ruxolitinib",
    "sargramostim",
    "satraplatin",
    "secukinumab",
    "semustine",
    "siltuximab",
    "sipuleucel-T",
    "sitimagene ceradenovec",
    "sonidegib",
    "sorafenib",
    "Streptozocin",
    "sunitinib",
    "Tacrolimus",
    "Tamoxifen",
    "TASONERMIN",
    "Tegafur",
    "tegafur, combinations",
    "temoporfin",
    "temozolomide",
    "temsirolimus",
    "Teniposide",
    "teriflunomide",
    "Thalidomide",
    "Thioguanine",
    "Thiotepa",
    "Thymopentin",
    "tiazofurine",
    "tivozanib",
    "tocilizumab",
    "tofacitinib",
    "Topotecan",
    "Toremifene",
    "trabectedin",
    "trametinib",
    "trastuzumab",
    "treosulfan",
    "Tretinoin",
    "triaziquone",
    "trifluridine, combinations",
    "Triptorelin",
    "trofosfamide",
    "ustekinumab",
    "valrubicin",
    "Vandetanib",
    "vedolizumab",
    "Vemurafenib",
    "Vinblastine",
    "Vincristine",
    "Vindesine",
    "vinflunine",
    "vinorelbine",
    "vintafolide",
    "vismodegib",
    "voclosporin",
    "Vorinostat",
    "vorozole",
    "zorubicin"]
atcListSet = getMedWhiteListSet(atcListInitial)

# Jon's list is a list of drugs of interest supplied by Jon.
jonListInitial = [
    "abemaciclib",
    "abiraterone acetate",
    "ado-trastuzumab emtansine",
    "Afatinib",
    "afatinib dimaleate",
    "Aldesleukin",
    "alectinib",
    "alemtuzumab",
    "alitretinoin",
    "anastrozole",
    "atezolizumab",
    "avelumab",
    "axicabtagene ciloleucel",
    "axitinib",
    "Belimumab",
    "belinostat",
    "bevacizumab",
    "bexarotene",
    "blinatumomab",
    "bortezomib",
    "bosutinib",
    "Brentuximab vedotin",
    "Brigatinib",
    "Cabazitaxel",
    "cabozantinib",
    "Cabozantinib",
    "Canakinumab",
    "Carfilzomib",
    "Ceritinib",
    "Cetuximab",
    "Cobimetinib",
    "copanlisib hydrochloride",
    "Crizotinib",
    "Dabrafenib",
    "daratumumab",
    "Dasatinib",
    "denileukin diftitox",
    "Denosumab",
    "Dinutuximab",
    "durvalumab",
    "elotuzumab",
    "enasidenib mesylate",
    "enzalutamide",
    "erlotinib",
    "everolimus",
    "exemestane",
    "fulvestrant",
    "gefitinib",
    "gemtuzumab ozogamicin",
    "Ibritumomab tiuxetan",
    "ibrutinib",
    "idelalisib",
    "Imatinib",
    "inotuzumab ozogamicin",
    "Ipilimumab",
    "Ixazomib",
    "Lanreotide acetate",
    "Lapatinib",
    "Lenalidomide",
    "Lenvatinib",
    "letrozole",
    "Midostaurin",
    "necitumumab",
    "neratinib",
    "Nilotinib",
    "Niraparib",
    "Nivolumab",
    "obinutuzumab",
    "ofatumumab",
    "Olaparib",
    "olaratumab",
    "osimertinib",
    "Palbociclib",
    "panitumumab",
    "panobinostat",
    "pazopanib",
    "Pembrolizumab",
    "pertuzumab",
    "Ponatinib",
    "pralatrexate",
    "radium 223 dichloride",
    "ramucirumab",
    "regorafenib",
    "Ribociclib",
    "Rituximab",
    "rituximab",
    "rituximab and hyaluronidase human",
    "Romidepsin",
    "Rucaparib",
    "Ruxolitinib",
    "Siltuximab",
    "Sipuleucel-T",
    "sonidegib",
    "Sorafenib",
    "sunitinib",
    "tamoxifen",
    "temsirolimus",
    "tisagenlecleucel",
    "Tocilizumab",
    "toremifene",
    "Tositumomab",
    "trametinib",
    "Trastuzumab",
    "Tretinoin",
    "Vandetanib",
    "vemurafenib",
    "venetoclax",
    "Vismodegib",
    "vorinostat",
    "ziv-aflibercept",
    "verzenio",
    "zytiga",
    "kadcyla",
    "Gilotrif",
    "gilotrif",
    "Proleukin",
    "alecensa",
    "campath",
    "panretin",
    "arimidex",
    "tecentriq",
    "bavencio",
    "yescarta",
    "inlyt",
    "Benlysta",
    "beleodaq",
    "Avastin",
    "targretin",
    "blincyto",
    "velcade",
    "bosulif",
    "Adcetris",
    "Alunbrig",
    "Jevtana",
    "cabometyx",
    "cometriq",
    "Ilaris",
    "Kyprolis",
    "Zykadia",
    "Erbitux",
    "Cotellic",
    "aliqopa",
    "Xalkori",
    "Tafinlar",
    "darzalex",
    "Sprycel",
    "Ontak",
    "Xgeva",
    "Unituxin",
    "Imfinzi",
    "empliciti",
    "idhifa",
    "xtandi",
    "tarceva",
    "afinitor",
    "aromasin",
    "faslodex",
    "iressa",
    "mylotarg",
    "zevalin",
    "imbruvica",
    "zydelig",
    "Gleevec",
    "besponsa",
    "Yervoy",
    "Ninlaro",
    "Somatuline",
    "Tykerb",
    "Revlimid",
    "Lenvima",
    "femara",
    "Rydapt",
    "portrazza",
    "NERLYNX",
    "Tasigna",
    "Zejula",
    "Opdivo",
    "gazyva",
    "arzerra",
    "Lynparza",
    "lartruvo",
    "tagrisso",
    "Ibrance",
    "vecitibix",
    "farydak",
    "votrient",
    "keytruda",
    "perjeta",
    "Iclusig",
    "folotyn",
    "xofigo",
    "cyramza",
    "stivarga",
    "Kisqali",
    "Mabthera",
    "rituxan",
    "rituxan hycela",
    "Istodax",
    "Rubraca",
    "Jakafi",
    "Sylvant",
    "Provenge",
    "odomzo",
    "Nexavar",
    "Sutent",
    "Nolvadex",
    "torisel",
    "kymriah",
    "Actemra",
    "fareston",
    "Bexxar",
    "mekinist",
    "herceptin",
    "vesanoid",
    "Caprelsa",
    "zelboraf",
    "venclexta",
    "erivedge",
    "zolinza",
    "zaltrap"]
jonListSet = getMedWhiteListSet(jonListInitial)


# Create list combinations between ATC/Jon and if med order has or is missing RxNorm code
atcNoRxNorm = stringMatchDrug(atcListSet, none_descriptions) # ATC, no RxNorm
atcWithRxNorm = stringMatchDrug(atcListSet, has_description) # ATC, has RxNorm
jonNoRxNorm = stringMatchDrug(jonListSet, none_descriptions) # Jon, no RxNorm
jonWithRxNorm = stringMatchDrug(jonListSet, has_description) # Jon, has RxNorm


print
print
print "******************"
print "Total Row Count: ", row_count
print "Missing RxNorm Row Total: ", count
print "******************"
print "Number of med orders without RxNorm that string match ATC: ", parseStringMatchList(atcNoRxNorm,0)
print
print "Med Order Name | Count"
parseStringMatchList(atcNoRxNorm,1)
print
print "******************"
print "Number of med orders with RxNorm that string match ATC: ", parseStringMatchList(atcWithRxNorm,0)
print
print "Med Order Name | Count"
parseStringMatchList(atcWithRxNorm,1)
print
print "******************"
print "Number of med orders without RxNorm that string match Jon's list: ", parseStringMatchList(jonNoRxNorm,0)
print
print "Med Order Name | Count"
parseStringMatchList(jonNoRxNorm,1)
print
print "******************"
print "Number of med orders with RxNorm that string match Jon's list: ", parseStringMatchList(jonWithRxNorm,0)
print
print "Med Order Name | Count"
parseStringMatchList(jonWithRxNorm,1)
print "******************"
print "Missing RxNorm Row Total: ", count
print
print "Med Order Name | Count"
medDescription_dic = {x:none_descriptions.count(x) for x in none_descriptions} 
for k,v in sorted(medDescription_dic.items()):
    print k,"|",v
print "******************"




