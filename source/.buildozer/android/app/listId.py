
S001 = [
"479",
"480",
"481",
"482",
"483",
"484",
"485",
"486",
"487",
"488",
"489",
"490",
"491",
"492",
"493",
"512",
"495",
"496",
"497",
"498",
"499",
"478",
"500",
"501",
"502",
"503",
"504",
"505",
"506",
"507",
"508",
"509",
"510",
"511",
"551",
"550",
]
S004 = [
"540",
"541",
"542",
"543",
"544",
"545",
"546",
"547",
"548",
"549", 
]
S005 = [
"1",
"516",
"2",
"3",
"4",
"5",
"6",
"514",
"7",
"8",
"9",
"10",
"11",
"517",
"12",
"13",
"14",
"15",
"16",
"17",
"513",
"18",
"19",
"20",
"21",
"22",
"515",
"456",
"23",
"24",
]
S007 = [
"25",
"26",
"27",
"28",
"29",
"30",
"31",
"32",
"33",
"34",
"35",
"36",
"37",
"38",
"39",
"40",
"41",
"42",
"43",
"44",
]
S008 = [
"45",
"46",
"47",
"48",
"49",
"50",
"51",
"52",
"53",
"54",
"55",
"56",
"57",
"58",
"59",
"60",
"61",
"62",
"63",
"64",
]
S009 = [
"65",
"66",
"67",
"68",
"69",
"70",
"71",
"72",
"73",
"74",
"75",
"76",
"77",
"78",
"79",
"80",
"81",
"82",
"83",
"84",
"85",
"86",
"87",
"88",
"89",
]
S101 = [
"90",
"91",
"92",
"93",
"94",
"95",
"96",
"97",
"98",
"99",
"100",
"101",
"102",
"103",
"104",
"105",
"106",
"107",
"108",
"109",
]
S102 = [
"111",
"112",
"113",
"114",
"115",
"116",
"117",
"118",
"119",
"120",
"121",
"122",
"123",
"124",
"125",
"126",
"127",
"128",
"129",
"130",
]
S103 = [
"132",
"133",
"134",
"135",
"136",
"137",
"138",
"139",
"140",
"141",
"142",
"143",
"144",
"145",
"146",
"147",
"148",
"149",
"150",
"151",
]
S104 = [
"152",
"153",
"154",
"155",
"156",
"157",
"158",
"159",
"160",
"161",
"162",
"163",
"164",
"165",
"166",
"167",
"168",
"169",
"170",
"171",
]
S105 = [
"172",
"173",
"174",
"175",
"176",
"177",
"178",
"179",
"180",
"181",
"182",
"183",
"184",
"185",
"186",
"187",
"188",
"189",
"190",
"191",
]
S201 = [
"192",
"193",
"194",
"195",
"196",
"197",
"198",
"199",
"200",
"201",
"202",
"203",
"204",
"205",
"206",
"207",
"208",
"209",
"210",
"211",
]
S202 = [
"212",
"213",
"214",
"215",
"216",
"217",
"218",
"219",
"220",
"221",
"222",
"223",
"224",
"225",
"226",
"227",
"228",
"229",
"230",
"231",
]
S203 = [
"232",
"233",
"234",
"235",
"236",
"237",
"238",
"239",
"240",
"241",
"242",
"243",
"244",
"245",
"246",
"247",
"248",
"249",
"250",
"251",
]
S204 = [
"252",
"253",
"254",
"255",
"256",
"257",
"258",
"259",
"260",
"261",
"262",
"263",
"264",
"265",
"266",
"267",
"268",
"269",
"270",
"271",
]
S205 = [
"272",
"273",
"274",
"275",
"276",
"277",
"278",
"279",
"280",
"281",
"282",
"283",
"284",
"285",
"286",
"287",
"288",
"289",
"290",
"291",
]
S206 = [
"292",
"293",
"294",
"295",
"296",
"297",
"298",
"299",
"300",
"301",
"302",
"303",
"304",
"305",
"306",
"307",
"308",
"309",
"310",
"311",
]
S207 = [
"312",
"313",
"314",
"315",
"316",
"317",
"318",
"319",
"320",
"321",
"322",
"323",
"324",
"325",
"326",
"327",
"328",
"329",
"330",
"331",
]
S208 = [
"332",
"333",
"334",
"335",
"336",
"337",
"338",
"339",
"340",
"341",
"342",
"343",
"344",
"345",
"346",
"347",
"348",
"349",
"350",
"351",
]
RoomDico = {
        "001":S001,
        "004":S004,
        "005":S005,
        "007":S007,
        "008":S008,
        "009":S009,
        "101":S101,
        "102":S102,
        "103":S103,
        "104":S104,
        "105":S105,
        "201":S201,
        "202":S202,
        "203":S203,
        "204":S204,
        "205":S205,
        "206":S206,
        "207":S207,
        "208":S208}

ROOMLIST = ["001","004","005","007","008","009","101","102","103","104","105",
            "201","202","203","204","205","206","207","208"]

def getRoom(num):
    return RoomDico[num]

machineDico = {
 "agamar":"479",
 "alderaan":"480",
 "antonella":"481",
 "bianca":"482",
 "bilbringi":"483",
 "bolognaise":"484",
 "brunella":"485",
 "calzonne":"486",
 "carmela":"487",
 "classica":"488",
 "corellia":"489",
 "coruscant":"490",
 "dagobah":"491",
 "donatella":"492",
 "endor":"493",
 "erladu":"512",
 "gargantua":"495",
 "gina":"496",
 "giulietta":"497",
 "grandiosa":"498",
 "graziella":"499",
 "helska":"478",
 "honoghr":"500",
 "hoth":"501",
 "linosa":"502",
 "napoletano":"503",
 "reine":"504",
 "religiosa":"505",
 "rosanna":"506",
 "salinca":"507",
 "serena":"508",
 "sicilia":"509",
 "tatooine":"510",
 "verde":"511",
 "verdura":"551",
 "yavin":"550",
 "ausone":"541",
 "chevalblanc":"542",
 "hautbrion":"543",
 "latour":"544",
 "margaux":"545",
 "petrus":"546",
 "rothschild":"547",
 "valandraud":"548",
 "yquem":"549",
 "beatles":"1",
 "bertignac":"516",
 "blackmore":"2",
 "dimeola":"3",
 "diogene":"4",
 "gambale":"5",
 "gilbert":"6",
 "goldman":"514",
 "hackett":"7",
 "hammett":"8",
 "hendrix":"9",
 "holdsworth":"10",
 "jordan":"11",
 "knopfler":"517",
 "malmsteen":"12",
 "mclaughlin":"13",
 "moore":"14",
 "morse":"15",
 "page":"16",
 "queen":"17",
 "reinhardt":"513",
 "riemann":"18",
 "satriani":"19",
 "slash":"20",
 "smith":"21",
 "vanhalen":"22",
 "winston":"515",
 "wylde":"456",
 "young":"23",
 "zappa":"24",
 "bavilk":"25",
 "becks":"26",
 "bernardus":"27",
 "carioca":"28",
 "chimay":"29",
 "florian":"30",
 "kaly":"31",
 "killian":"32",
 "krick":"33",
 "niva":"34",
 "orval":"35",
 "palm":"36",
 "pelican":"37",
 "pietra":"38",
 "primus":"39",
 "saaz":"40",
 "secondus":"41",
 "stella":"42",
 "westmale":"43",
 "yixing":"44",
 "beetlejuice":"45",
 "braque":"46",
 "cezanne":"47",
 "chagall":"48",
 "corot":"49",
 "dali":"50",
 "degas":"51",
 "ernst":"52",
 "gauguin":"53",
 "leger":"54",
 "leonardo":"55",
 "magritte":"56",
 "matisse":"57",
 "millet":"58",
 "miro":"59",
 "modigliani":"60",
 "monet":"61",
 "pissarro":"62",
 "renoir":"63",
 "vangogh":"64",
 "archimede":"65",
 "arthur":"66",
 "buffy":"67",
 "casper":"68",
 "derek":"69",
 "euskadi":"70",
 "excalibur":"71",
 "falcon":"72",
 "flyingv":"73",
 "gibsonsg":"74",
 "hal":"75",
 "hector":"76",
 "jack":"77",
 "jarjar":"78",
 "kay":"79",
 "lespaul":"80",
 "manet":"81",
 "merlin":"82",
 "nikopol":"83",
 "pelinove":"84",
 "penguin":"85",
 "tequila":"86",
 "universe":"87",
 "verone":"88",
 "visual":"89",
 "auchentoshan":"90",
 "blackbush":"91",
 "bowmore":"92",
 "bushmills":"93",
 "caolila":"94",
 "cardhu":"95",
 "glenfiddich":"96",
 "glengarioch":"97",
 "glenmorangie":"98",
 "islay":"99",
 "knockdhu":"100",
 "lagavulin":"101",
 "laphroaig":"102",
 "ledaig":"103",
 "macallan":"104",
 "mortlach":"105",
 "oban":"106",
 "pittyvaich":"107",
 "portellen":"108",
 "tamnavulin":"109",
 "balden":"111",
 "biot":"112",
 "bleriot":"113",
 "bourhis":"114",
 "breguet":"115",
 "bustov":"116",
 "cayley":"117",
 "chanute":"118",
 "cody":"119",
 "curtiss":"120",
 "delagrange":"121",
 "dumont":"122",
 "gasnier":"123",
 "lebris":"124",
 "lilienthal":"125",
 "moy":"126",
 "pilcher":"127",
 "robart":"128",
 "voisin":"129",
 "wright":"130",
 "agenum":"132",
 "aleria":"133",
 "alesia":"134",
 "aluminium":"135",
 "anicium":"136",
 "aquarium":"137",
 "avoranfix":"138",
 "babaorum":"139",
 "beaufix":"140",
 "elevedelix":"141",
 "goudurix":"142",
 "jolitorax":"143",
 "labeldecadix":"144",
 "laudanum":"145",
 "lentix":"146",
 "lutetia":"147",
 "nenjetepus":"148",
 "octodurum":"149",
 "petitbonum":"150",
 "serum":"151",
 "albans":"152",
 "burzamil":"153",
 "cenva":"154",
 "chani":"155",
 "cheonech":"156",
 "daniel":"157",
 "devries":"158",
 "hawat":"159",
 "hayt":"160",
 "holtzman":"161",
 "jamis":"162",
 "jessica":"163",
 "joe":"164",
 "kynes":"165",
 "liet":"166",
 "moneo":"167",
 "patrin":"168",
 "shaddam":"169",
 "vladimir":"170",
 "wensicia":"171",
 "bellonda":"173",
 "corba":"174",
 "dama":"175",
 "feydrautha":"176",
 "ghanima":"177",
 "halleck":"178",
 "idaho":"179",
 "lucila":"180",
 "murbella":"181",
 "noree":"182",
 "odrade":"183",
 "scytale":"184",
 "sheeana":"185",
 "stilgar":"186",
 "talamane":"187",
 "taraza":"188",
 "tegs":"189",
 "tuek":"190",
 "usul":"191",
 "arnaudvidal":"193",
 "bellaud":"194",
 "bessou":"195",
 "camelat":"196",
 "cortet":"197",
 "daubasse":"198",
 "gardenal":"199",
 "garros":"200",
 "girardeau":"201",
 "mistral":"202",
 "montanhagol":"203",
 "mouret":"204",
 "pegulhan":"205",
 "peirevidal":"206",
 "peyrol":"207",
 "puycibot":"208",
 "riquier":"209",
 "ruffi":"210",
 "sordel":"211",
 "blader":"212",
 "bodon":"213",
 "deborn":"214",
 "dubartas":"215",
 "ermengaud":"216",
 "fabre":"217",
 "figueira":"218",
 "folquet":"219",
 "foures":"220",
 "froment":"221",
 "godolin":"222",
 "guilhemix":"223",
 "jasmin":"224",
 "lechapelain":"225",
 "marcabrun":"226",
 "miraval":"227",
 "perbosc":"228",
 "plomet":"229",
 "rudel":"230",
 "ventadorn":"231",
 "data":"233",
 "kira":"234",
 "kirk":"235",
 "mccoy":"236",
 "obrien":"237",
 "odo":"238",
 "picard":"239",
 "pulaski":"240",
 "quark":"241",
 "riker":"242",
 "scotty":"243",
 "spock":"244",
 "sulu":"245",
 "tasha":"246",
 "tchekov":"247",
 "troi":"248",
 "uhura":"249",
 "westly":"250",
 "worf":"251",
 "botero":"252",
 "buffet":"253",
 "cassatt":"254",
 "escher":"255",
 "goya":"256",
 "kandinsky":"257",
 "lautrec":"258",
 "legreco":"259",
 "marquet":"260",
 "morissot":"261",
 "opalka":"262",
 "redon":"263",
 "rembrandt":"264",
 "seurat":"265",
 "signac":"266",
 "tissot":"267",
 "velasquez":"268",
 "vlaminck":"269",
 "watteau":"270",
 "whistler":"271",
 "gandalf":"272",
 "gimli":"273",
 "glorfindel":"274",
 "goldberry":"275",
 "gollum":"276",
 "hoarmurath":"277",
 "indur":"278",
 "khamul":"279",
 "legolas":"280",
 "merry":"281",
 "pallando":"282",
 "pippin":"283",
 "radagast":"284",
 "ren":"285",
 "saruman":"286",
 "shagrat":"287",
 "smaug":"288",
 "theoden":"289",
 "thranduil":"290",
 "uvatha":"291",
 "adunaphel":"292",
 "akhorahil":"293",
 "alatar":"294",
 "aragorn":"295",
 "arwen":"296",
 "beorn":"297",
 "bilbo":"298",
 "bombadil":"299",
 "boromir":"300",
 "celeborn":"301",
 "cirdan":"302",
 "durin":"303",
 "dwar":"304",
 "elrond":"305",
 "eomer":"306",
 "eowyn":"307",
 "ermurazor":"308",
 "faramir":"309",
 "frodo":"310",
 "galadriel":"311",
 "jrenoir":"312",
 "kurosawa":"313",
 "lang":"314",
 "langdon":"315",
 "leone":"316",
 "linder":"317",
 "losey":"318",
 "mizoguchi":"319",
 "murnau":"320",
 "ophuls":"321",
 "pasolini":"322",
 "powell":"323",
 "tati":"324",
 "tourneur":"325",
 "truffaut":"326",
 "vigo":"327",
 "vonsternberg":"328",
 "vonstroheim":"329",
 "welles":"330",
 "wiene":"331",
 "bava":"332",
 "bergman":"333",
 "browning":"334",
 "bunuel":"335",
 "capra":"336",
 "carne":"337",
 "cassavetes":"338",
 "chaplin":"339",
 "clouzot":"340",
 "cocteau":"341",
 "eisenstein":"342",
 "fassbinder":"343",
 "fellini":"344",
 "ford":"345",
 "gance":"346",
 "griffith":"347",
 "hawks":"348",
 "hitchcock":"349",
 "huston":"350",
 "keaton":"351"
}

def findMachine(mach):
    if mach in machineDico:
        return machineDico[mach]
    else:
        print("Erreur: cette machine n'existe pas!")
        return None