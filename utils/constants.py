import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

USERNAME: str = os.environ["INSTA_USERNAME"]
PASSWORD: str = os.environ["INSTA_PASSWORD"]

DOWNLOAD_DIRECTORY: Path = Path(__file__).parent.parent / "downloads"
SESSION_DIRECTORY: Path = Path(__file__).parent.parent / "sessions"

# Change the values of this variable to whatever @ instagram you want
TARGET_USERS = {
    "jessicaellenbc",
    "laysmp",
    "marialuiza_santanaa0",
    "anycar0liny",
    "nano.wop",
    "vt.tinvi",
    "dailyyjota",
    "marefonseca_",
    "marafonimille",
    "iingrid_motta",
    "dalvabr_",
    "academiaforcaativa",
    "marcelasilva_015",
    "mariaclara_nadu",
    "_luninh4",
    "vidal_annac",
    "juan_.matos",
    "issaa_mooraes",
    "anabeatriz_2312",
    "luyzavidal_",
    "aninhabastos21",
    "claralombass_",
    "laylla_sa",
    "yasmim4913",
    "yasmimcardossojw",
    "lethiciabello",
    "jokastacoutinho",
    "isbxla._",
    "_hevelincoutinho_",
    "juhfidelis3",
    "marialuiza_gouvea",
    "dudacardoso_31",
    "andrezaa25",
    "myllenacostasr",
    "anaclements.s",
    "giullinha",
    "camilabclr",
    "emilygoncalvess_",
    "lorenaa_azeredo",
    "a_luqueci",
    "lisiatorres",
    "japameirelles",
    "carolttavares",
    "cabral.camille",
    "bru_vignoli",
    "lou_vignolii",
    "dudaazeredooo",
    "samantha_moreira04",
    "raissaadonatto",
    "ferreira_gabriellydasilva",
    "btrzoliveira_",
    "bia_a_pires",
    "maria_clara0liveir4",
    "gabrielcliam",
    "vivih_cristina6464",
    "eurayssa_oliveira_",
    "rodrigo.85",
    "sarahcaastro_",
    "sandy_sarahh",
    "xdx_deboracris",
    "heymyllenaaraujo",
    "bella_oliveira_08",
    "carla_ra_ab",
    "quehpazz_ofc",
    "brenoxalmeida",
    "brendanassif",
    "bruuh_mell",
    "jenneferviannaa",
    "julia.lalmeida",
    "eu.daniel.lima",
    "midia.monteiro1",
    "__jad__.eee",
    "_022_mg_",
    "isaque.schineider",
    "giovana.fagner",
    "rosanesuzart",
    "rosimerigalaxe",
    "xeniamachado",
    "robertaarrabalatelier",
    "roberto_carlos__e_silvia",
    "brunoperoli",
    "cam.ilagomes",
    "rosanepradocarvalho",
    "rosaria.trindade",
    "ellietesantana",
    "sammyfreitasss",
    "carolinaavidal_",
    "lilia.vidal.986",
    "jamartinsz_",
    "carolvidal65",
    "rosamariasodrepessanha",
    "brenda.paula.73",
    "nathanalmeidaofc22",
    "alice_estilosa_",
    "alicesousa.ofc",
    "julia.lalmeida",
    "spooky_aninha",
    "juliappaa",
    "loyanems",
    "haissam_chalhoub",
    "belle.hys",
    "leticiacarvalho_27",
    "jonathan_coutinho01",
    "karenccoelho",
    "riscado_dgr",
    "coutinho_og",
    "leandra_trindade22",
    "almeidalayra234",
    "laysa_almeida16",
    "ll.keren",
    "lucas_.coutinh",
    "carolcastropaes",
    "juuh.amorimm",
    "tati.souza.jed",
    "luv._.soy",
    "david.bebiano.9",
    "gabiargides",
    "julianaargides",
    "thamara_coutinho_",
    "gabibarb_",
    "bele_soares",
    "a_indiaja",
    "k_barroos",
    "mariahsmello",
    "ricciramosmaria",
    "lara.limmma",
    "clarinha_moraees",
    "originaljuliane",
    "izabellacardias",
    "vitorianeustadt",
    "laripelegrinoo",
    "juliagasparchagas",
    "kauanysouzza_",
    "silveirasz",
    "marafonimille",
    "jessicaellenpiercer",
    "gustavosoares_fbj",
    "goulartlila",
    "danieleteles2016",
    "natashagabryela",
    "bazarebrechodaju",
    "aylasakua.aa",
    "mvmantuano",
    "criss.magalhaes_",
    "flavio.taveiros",
    "sidinhopereira",
    "silva.madileine",
    "nick_ali001",
    "lucasys.peres",
    "endhyara",
    "blendoonsalles",
    "_isabellevilla",
    "mincastro1999",
    "majjuu__",
    "fani_pinheiro",
    "mariamatins_",
    "vivian.agnello",
    "odaramouraa",
    "ana_carolina0222",
    "manubrraga",
    "yasmim.maartins",
    "_yasxcr",
    "nandawonderly",
    "natyy_almeida15",
    "iamdudajordao",
    "anapaulinof",
    "juh_jubaa",
    "zeliocanela",
    "jeancastilhoo",
    "juh.baiense",
    "juanmaximoitaunagm",
    "ayslan_whatz",
    "nnico.ly",
    "skysamoon",
    "analu_0306",
    "maria_maglhaesx",
    "liajluna",
    "ruiz_isab",
    "gaabreuu",
    "eujamillymachado",
    "_navalle",
    "kathleen_nail_designer_",
    "ana_caldass",
    "oiemilheme",
    "ray.anneoliiveira",
    "celestehuala",
    "geovanac.chagas",
    "arielcalazans_s",
    "alinedalgobbo",
    "anderson_zzk",
    "kathleen_cardoso0",
    "mari.ferreiirah",
    "isabellecostanail",
    "cauanewr",
    "dayara_beral",
    "gabriellacunhaoliv",
    "evelyncosta1708",
    "alinedalgobbo.nutricionista",
    "juliana_cuidadorainfantil",
    "beth.simeao",
    "eliza_bomfim_tricoche",
    "thayres.figueiredo",
    "canela_saquarema",
    "sarahh__ferreira",
    "jessicaellenpmu",
    "poliana.linhares7",
    "acnunss",
    "zronan_z",
    "sronan_s",
    "beatrizmuniz01",
    "ana_nunsss",
    "sidinhoopereira",
    "rayssa__moraes12",
    "martaoliveira9446",
    "rafa_rodrigues.s",
    "laraluqueci",
    "brunapnl",
    "letygoulart",
    "guilherme_neves7",
    "jessedeabreuca",
    "cortinhas_s",
    "raazziiel",
    "raphaella__nascimento",
    "raphaelgomes0",
    "breno.fxgp",
    "dulia_manuela",
    "dm.garay",
    "laispecanha_",
    "laispecanhasc_",
    "brendo.p",
    "lais021",
    "lais9815",
    "_graziella_01",
    "alebiondine",
    "manoellaaraujo_",
    "lays.cachos",
    "laysa.almeida.37201",
    "jucimar.castilho",
    "juliomelobarber",
    "beatrizz_pmu",
    "parreiras2.4",
    "07_xandd",
    "marciachalhoub",
    "juli.catapano",
    "machadop_th",
    "lygiabitarr",
    "carlosrobert2005",
    "luizsantos_cl",
    "nicol.e0606",
    "maldonadoojessica",
    "luhlua_",
    "luanarreguengo",
    "souzamariiana6",
    "lucasc.soares14",
    "david_bebiano",
    "tatianasantanaolv",
    "ecchioul",
    "ssuellen0",
    "nathan_aguiar77",
    "thaisdejesus.silva",
    "anthony__yy16",
    "artcacauoficial",
    "samuel.frts",
    "samuels.p3",
    "leticiasousa01_",
    "familiasolesurf",
    "acessoriosbybellec",
    "lucas.lops_",
    "rodrig0_0rtega",
    "raquelcbebiano",
    "rosianepaixaonoivas",
    "juli.ana0683",
    "lucianadiasmaquiadora",
    "esteladsantana",
    "joanajordao.jo",
    "drumondjuliag",
    "kaiosnrj",
    "priscila.ssfsilva",
    "coimbra_tiago",
    "fabricio_slack",
    "yasmin_prado.c",
    "danilocostacabeleireiro",
    "dandara.roque",
    "espetinhonopontosaqua",
    "milena_decora",
    "danilocostafamilia",
    "rafa_dos.cortes",
    "momo_oli17",
    "cintiadesouzap",
    "vinicius_dc_silva01",
    "anaassssssssn",
    "esterbaiense",
    "vanessa.veloso83",
    "kaylanedesouzas",
    "davi_salgado1",
    "lash_designerthay",
    "larissachgz",
    "_vieira_lari",
    "marcellybravo",
    "arrabal_victor",
    "brucouttin",
    "evelaine_queiroz",
    "vaniely_silv",
    "anaclaguiar",
    "ique.etty",
    "jack_dias.2",
    "gaabi_0livera",
    "lusoares2",
    "_my_dri",
    "joaobinoo",
    "fernandagenarofoto",
    "srta.fernandez",
    "amandamendes.022",
    "manuelly_madeira",
    "stefany.souza_19",
    "stephanny_cardoso",
    "eu_stephannye",
    "__milenareis__",
    "eumiropereiraa",
    "_freitasyasmin00",
    "ruth_cc7",
    "domenique.__",
    "nicolemulta_",
    "elainemarinho1973",
    "elainewanderley2",
    "clamontc",
    "lorena.carvalh0",
    "giolardy",
    "isaalves121",
    "raissamartinellii",
    "daay_almeiiida",
    "ju_cassano",
    "vidallorenaa",
    "kauanysouzza_",
    "julia_senos",
    "patriciatti",
    "lopes.viit",
    "cabral.camille",
    "hellen.portinelli",
    "laismacedo.atelier",
}
