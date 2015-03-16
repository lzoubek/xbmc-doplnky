# Usage Tracker #

Usage Tracker je skript, který umožňuje ostatním doplňkům odesílat anonymní data v okamžiku, kdy jsou využity. Vždycky mě zajímaly následující věci:
  * Kolik je vás uživatelů?
  * Který dolněk je nejvíce používán?
  * Jaký operační systém převládá?
  * Kolik % je čechů a kolik slováků?

Povolením zasílání anonymních statistik mi na tyto otázky dáte odpověď.

# Jak to funguje? #

Od aktualizace 30.12.2012 se při prvním spuštění některého z doplňků dotáže, zda chce uživatel povolit zasílání anonymních dat (Ano/Ne).
Od té chvíle je respektováno uživatelovo rozhodnutí, které se dá změnit pouze smazáním nebo úpravou souboru `userdata/addon_data/script.module.stream.resolver/tracking.json`.

Doplněk jedinou funkci:
  * API pro ostatní pluginy, umožňující reportovat využití

# Co je odesíláno? #

Odesílá se zpravidla při přehrátí/stažení videa doplňkem. Odesílá se název doplňku. Na google analytics, se tedy dozvím, že daný doplněk byl použit. Dále se odesílá:
  * verze XBMC
  * operační systém
  * rozližení obrazovky
  * jazykové prosředí
  * identita XBMC instance - unikátní náhodné číslo, které se vygeneruje při prvním spuštění.

# Jaké jsou výsledky? #

Povedlo se mi vytvořit v PHP stránku, která nasosává výsledky z google analytics a prezentuje je. mrkněte [sem](http://jezzovo.net/xbmc-doplnky/stats.php).