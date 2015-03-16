Vytvořte soubor **playercorefactory.xml** a umístěte jej do profilu vašeho XBMC (linuxáci ~/.xbmc/userdata, windowsáci C:\USER\AppDATA\Roaming\XBMC\userdata\

```
 <playercorefactory>
 <players>
    <player name="KMPlayer" type="ExternalPlayer" audio="false" video="true">
      <filename>C:\Program Files\The KMPlayer\KMPlayer.exe</filename>
      <args>"{1}" /fullscreen /close</args>
      <hidexbmc>false</hidexbmc>
      <hideconsole>false</hideconsole>
      <warpcursor>none</warpcursor>
    </player>
  </players>
  <rules action="prepend">
   <rule name="streams" internetstream="true">
    <rule name="ulozto" filename=".*uloz.to.*" player="KMPlayer"/>
   </rule>
  </rules>
 </playercorefactory>
```

Vysvětlení:
  * v poduzlu deklarujeme externí přerháváč (může jich být i více), povšimněte obsahu atributu **name**
  * pomocí seznamu pravidel se určí, který přehrávač bude použit. V našem případě mme pravidlo **streams**, které vyhovuje všem internetovým streamům a jeho podpravidlem je pravidlo **ulozto**, které vyhovuje takovým streamům, jež mají v URL slovo **uloz.to**. Je-li toto pravidlo splněno pro konkrétní stream, je použit přehrávač **KMPlayer**

Samozřejmě je nutné mít nainstalovaný KMPlayer, který je možno stáhnout např. [zde](http://www.stahuj.centrum.cz/multimedia/multimedialni_prehravace/kmplayer/)

Je možno použít i jiný přehrávač (vlc, MPlayer nebo Windows Media Player), nicméně Quick-Silver otestoval a doporučuje právě KMPlayer.