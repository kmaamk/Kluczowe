from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.utils import formats


class Question (models.Model):


    ANP = 'Asystent nauczyciela przedszkola'
    S_A = 'Agroturystyka 50+'
    AON = 'Asystent osoby niepełnosprawnej'
    AR = 'Asystent rodziny'
    ASt = 'Asystentka stomatologiczna z elementami implantologii'
    Ch = 'Charakteryzacja'
    CT = 'Coach - trener'
    DWEF = 'Dekorator wnętrz z elementami florystyki'
    D = 'Dietetyka'
    DAR = 'Doula - asystentka rodzącej'
    FloB = 'Florystyka i bukieciarstwo'
    S_FB = 'Florystyka i bukieciarstwo 50+'
    Fot = 'Fotografia z certyfikatem CANON'
    GK = 'Grafika komputerowa'
    HSt = 'Higienistka stomatologiczna'
    S_I = 'Informatyka 50+'
    IF = 'Instruktor fitness'
    JA = 'Język angielski'
    JN = 'Język niemiecki'
    S_K = 'Kosmetyka 50+'
    KE = 'Kosmetyka estetyczna'
    S_Ma = 'Masaż 50+'
    S_OMa = 'Opieka medyczna 50+'
    OMAS = 'Opiekun medyczny z aktywizacją seniora'
    OOS = 'Opiekun osoby starszej'
    OPS = 'Opiekun w domu pomocy społecznej'
    OD = 'Opiekunka dziecięca'
    OS = 'Opiekunka środowiskowa'
    OSI = 'Organizacja sprzedaży internetowej - e-commerce'
    OISiK = 'Organizator imprez ślubnych i konferencyjnych'
    OrRW = 'Ortoptystka - rehabilitacja wzroku'
    PiPS = 'Podologia i pielęgnacja stóp'
    PNwP = 'Pośrednictwo nieruchomości w praktyce'
    S_PiS = 'Prawo i administracja 50+'
    PFiT = 'Produkcja filmowa i telewizyjna'
    S_PFiT = 'Produkcja filmowa i telewizyjna 50+'
    PAM = 'Programowanie aplikacji internetowych i mobilnych'
    PGKES = 'Programowanie gier komputerowych - specjalizacja e-sport'
    PSInt = 'Projektowanie stron internetowych'
    PSl = 'Protetyk słuchu'
    RSM = 'Rejestratorka/Sekretarka medyczna'
    TAZB = 'Technik administracji - zarządzanie biurem'
    TBHP = 'Technik BHP'
    TDTCC = 'Technik dentystyczny z technologią CAD/CAM'
    TEr = 'Technik elektroradiolog'
    TF = 'Technik farmaceutyczny'
    TICM = 'Technik informatyk z certyfikatami Microsoftu'
    TMaF = 'Technik masażysta z elementami fizjoterapii'
    TOp = 'Technik optyk'
    TRKF = 'Technik rachunkowości - księgowość firm'
    TSM = 'Technik sterylizacji medycznej'
    TTi = 'Technik teleinformatyk'
    TUKWS = 'Technik usług kosmetycznych - wellness & spa'
    TW = 'Technik weterynarii'
    TZ = 'Terapeuta zajęciowy'
    TPe = 'Trener personalny'
    WiS = 'Wizaż i stylizacja'
    Z = 'Ziołolecznictwo'

    #formularz wyświetla drugi element z tupli
    base_courses = (( ANP , 'Asystent nauczyciela przedszkola' ) ,
                    ( S_A , 'Agroturystyka 50+' ) ,
                    ( AON , 'Asystent osoby niepełnosprawnej' ) ,
                    ( AR , 'Asystent rodziny' ) ,
                    ( ASt , 'Asystentka stomatologiczna z elementami implantologii' ) ,
                    ( Ch , 'Charakteryzacja' ) ,
                    ( CT , 'Coach - trener' ) ,
                    ( DWEF , 'Dekorator wnętrz z elementami florystyki' ) ,
                    ( D , 'Dietetyka' ) ,
                    ( DAR , 'Doula - asystentka rodzącej' ) ,
                    ( FloB , 'Florystyka i bukieciarstwo' ) ,
                    ( S_FB , 'Florystyka i bukieciarstwo 50+' ) ,
                    ( Fot , 'Fotografia z certyfikatem CANON' ) ,
                    ( GK , 'Grafika komputerowa' ) ,
                    ( HSt , 'Higienistka stomatologiczna' ) ,
                    ( S_I , 'Informatyka 50+' ) ,
                    ( IF , 'Instruktor fitness' ) ,
                    ( JA , 'Język angielski' ) ,
                    ( JN , 'Język niemiecki' ) ,
                    ( S_K , 'Kosmetyka 50+' ) ,
                    ( KE , 'Kosmetyka estetyczna' ) ,
                    ( S_Ma , 'Masaż 50+' ) ,
                    ( S_OMa , 'Opieka medyczna 50+' ) ,
                    ( OMAS , 'Opiekun medyczny z aktywizacją seniora' ) ,
                    ( OOS , 'Opiekun osoby starszej' ) ,
                    ( OPS , 'Opiekun w domu pomocy społecznej' ) ,
                    ( OD , 'Opiekunka dziecięca' ) ,
                    ( OS , 'Opiekunka środowiskowa' ) ,
                    ( OSI , 'Organizacja sprzedaży internetowej - e-commerce' ) ,
                    ( OISiK , 'Organizator imprez ślubnych i konferencyjnych' ) ,
                    ( OrRW , 'Ortoptystka - rehabilitacja wzroku' ) ,
                    ( PiPS , 'Podologia i pielęgnacja stóp' ) ,
                    ( PNwP , 'Pośrednictwo nieruchomości w praktyce' ) ,
                    ( S_PiS , 'Prawo i administracja 50+' ) ,
                    ( PFiT , 'Produkcja filmowa i telewizyjna' ) ,
                    ( S_PFiT , 'Produkcja filmowa i telewizyjna 50+' ) ,
                    ( PAM , 'Programowanie aplikacji internetowych i mobilnych' ) ,
                    ( PGKES , 'Programowanie gier komputerowych - specjalizacja e-sport' ) ,
                    ( PSInt , 'Projektowanie stron internetowych' ) ,
                    ( PSl , 'Protetyk słuchu' ) ,
                    ( RSM , 'Rejestratorka/Sekretarka medyczna' ) ,
                    ( TAZB , 'Technik administracji - zarządzanie biurem' ) ,
                    ( TBHP , 'Technik BHP' ) ,
                    ( TDTCC , 'Technik dentystyczny z technologią CAD/CAM' ) ,
                    ( TEr , 'Technik elektroradiolog' ) ,
                    ( TF , 'Technik farmaceutyczny' ) ,
                    ( TICM , 'Technik informatyk z certyfikatami Microsoftu' ) ,
                    ( TMaF , 'Technik masażysta z elementami fizjoterapii' ) ,
                    ( TOp , 'Technik optyk' ) ,
                    ( TRKF , 'Technik rachunkowości - księgowość firm' ) ,
                    ( TSM , 'Technik sterylizacji medycznej' ) ,
                    ( TTi , 'Technik teleinformatyk' ) ,
                    ( TUKWS , 'Technik usług kosmetycznych - wellness & spa' ) ,
                    ( TW , 'Technik weterynarii' ) ,
                    ( TZ , 'Terapeuta zajęciowy' ) ,
                    ( TPe , 'Trener personalny' ) ,
                    ( WiS , 'Wizaż i stylizacja' ) ,
                    ( Z , 'Ziołolecznictwo' ) ,

                    )
    OD ='Odd'
    BEL = 'BEL'
    BIA = 'BIA'
    BIE = 'BIE'
    BYD = 'BYD'
    CZE = 'CZE'
    GDA = 'GDA'
    GDY = 'GDY'
    GLI = 'GLI'
    GNI = 'GNI'
    GOR = 'GOR'
    GRU = 'GRU'
    JAS = 'JAS'
    JEL = 'JEL'
    KAL = 'KAL'
    KAT = 'KAT'
    KIE = 'KIE'
    KRA = 'KRA'
    LEG = 'LEG'
    LES = 'LES'
    LUB = 'LUB'
    LUI = 'LUI'
    NOS = 'NOS'
    OLS = 'OLS'
    OPO = 'OPO'
    OST = 'OST'
    PIL = 'PIL'
    PIO = 'PIO'
    PLO = 'PLO'
    POZ = 'POZ'
    PUL = 'PUL'
    RAC = 'RAC'
    RAD = 'RAD'
    RYB = 'RYB'
    RZE = 'RZE'
    SLU = 'SLU'
    STA = 'STA'
    SWI = 'SWI'
    SZC = 'SZC'
    TOR = 'TOR'
    TYC = 'TYC'
    WAL = 'WAL'
    WOD = 'WOD'
    WRF = 'WRF'
    ZAM = 'ZAM'
    ZOR = 'ZOR'

    branches = (( OD , '--' ),
                ( BEL , 'BEL' ) ,
                ( BIA , 'BIA' ) ,
                ( BIE , 'BIE' ) ,
                ( BYD , 'BYD' ) ,
                ( CZE , 'CZE' ) ,
                ( GDA , 'GDA' ) ,
                ( GDY , 'GDY' ) ,
                ( GLI , 'GLI' ) ,
                ( GNI , 'GNI' ) ,
                ( GOR , 'GOR' ) ,
                ( GRU , 'GRU' ) ,
                ( JAS , 'JAS' ) ,
                ( JEL , 'JEL' ) ,
                ( KAL , 'KAL' ) ,
                ( KAT , 'KAT' ) ,
                ( KIE , 'KIE' ) ,
                ( KRA , 'KRA' ) ,
                ( LEG , 'LEG' ) ,
                ( LES , 'LES' ) ,
                ( LUB , 'LUB' ) ,
                ( LUI , 'LUI' ) ,
                ( NOS , 'NOS' ) ,
                ( OLS , 'OLS' ) ,
                ( OPO , 'OPO' ) ,
                ( OST , 'OST' ) ,
                ( PIL , 'PIL' ) ,
                ( PIO , 'PIO' ) ,
                ( PLO , 'PLO' ) ,
                ( POZ , 'POZ' ) ,
                ( PUL , 'PUL' ) ,
                ( RAC , 'RAC' ) ,
                ( RAD , 'RAD' ) ,
                ( RYB , 'RYB' ) ,
                ( RZE , 'RZE' ) ,
                ( SLU , 'SLU' ) ,
                ( STA , 'STA' ) ,
                ( SWI , 'SWI' ) ,
                ( SZC , 'SZC' ) ,
                ( TOR , 'TOR' ) ,
                ( TYC , 'TYC' ) ,
                ( WAL , 'WAL' ) ,
                ( WOD , 'WOD' ) ,
                ( WRF , 'WRF' ) ,
                ( ZAM , 'ZAM' ) ,
                ( ZOR , 'ZOR' ) ,
                )

    branch = models.CharField(max_length=150)
    #question_text = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=500)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(default=timezone.now)

    #vote = models.BooleanField(default=False)



    def __str__(self):
        return '{} {}'.format(self.branch,  formats.date_format(self.created_date, "MONTH_DAY_FORMAT"))




# Create your models here.
