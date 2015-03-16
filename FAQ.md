## Které verze XBMC jsou podporovány? ##

Doplňky momentálně běží na XBMC 12.x a 13.

## Doplněk Soubory Online nezobrazuje ulozto captcha ##

Pokud používáte Windows řešení problému je **portable** režim, viz následující otázka.

## Na Windows mi žádný doplněk nejde spustit, co s tím? ##

XBMC má na Windows stále nevyřešenou [chybu](http://trac.xbmc.org/ticket/12220), kdy některé doplňky vůbec nefungují. Je to proto, že v cestě k doplňku se objeví diakritika. Na tuto chybu narazíte na Windows XP snad pokaždé (C:\Documents and Settings\Libor\Data Aplikací\XBMC) na ostatních windows se může objevit, pokud je ve jméně uživatele diakritika.

Řešením je buď přejmenovat uživatele, resp. vytvořit nového, nebo spouštět XBMC v **portable** režimu. V takovém případě XBMC veškerá uživatelská data včetě nainstalovaných doplňků ukládá do místa instalace (C:\Program Files\XBMC). **Portable** režim zapnete přidáním parametru **-p** při spuštění XBMC.

Příkaz ke spuštění tedy vypadá **"C:\Program Files\XBMC\XBMC.exe" -p**

Zástupce pro spuštění XBMC pak bude vypadat takto:

![http://dl.dropbox.com/u/60205468/xbmc_portable_windows.png](http://dl.dropbox.com/u/60205468/xbmc_portable_windows.png)

## Kde najdu log soubor ke XBMC? ##

  * Windows XP hledejte v **C:\Documents and Settings\[uživatel]\Data Aplikací\XBMC**
  * Windows 7 a Vista **C:\Users\[uživatel]\AppData/Roming\XBMC**
  * Linux **~/.xbmc/temp/xbmc.log**
  * Dharma 10.1 v portable režimu **C:\Program Files\XBMC\xbmc.log**
  * Eden v portable režimu **C:\Program Files\XBMC\portable\_data\xbmc.log**
  * AppleTV2 **/private/var/mobile/Library/Preferences/xbmc.log**