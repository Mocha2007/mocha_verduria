# Notes:

* I designed the Viminian flag to be reflective of a rural landscape - a blue bar for the sky, a yellow bar for wheat, and a green bar for a fertile meadow... or something.
* TODO: make "add country checklist" and "add province checklist"

## ADDING A COUNTRY CHECKLIST

1. common/countries.txt
2. common/countries/Xxx.txt
	* Including Color
3. history/countries/XXX - xxx.txt
	* Capital, culture, religion
4. history/provinces/almea/ (add core info to provinces)
5. history/pops/3480.1.1/Xxx.txt
6. localization/verduria.csv (add XXX and XXX_ADJ keys)
7. gfx/flags/ (add the 5 flags)

## ADDING A PROVINCE CHECKLIST
1. map/definition.csv
2. map/provinces.bmp
3. map/positions.txt, climate.txt, continent.txt, region.txt
4. copy file over to provinces/almea/...
5. localization/verduria.csv

## Default Pop Composition:

```
# XXX - 400% -> 100%
XXX = {
	aristocrats = {
		culture = viminian
		religion = animist
		size = 1%
	}

	clergymen = {
		culture = viminian
		religion = animist
		size = 1%
	}

	artisans = {
		culture = viminian
		religion = animist
		size = 5%
	}

	soldiers = {
		culture = viminian
		religion = animist
		size = 1%
	}

	officers = {
		culture = viminian
		religion = animist
		size = 0.1%
	}

	farmers = {
		culture = viminian
		religion = animist
		size = 92.9%
	}

}
```